from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from movies.models import Country
import json
import os

# Minimal, safe population script for the Country model.
# Place this file in movies/management/commands/populate_country.py
# Usage:
#   python manage.py populate_country
#   python manage.py populate_country --file /path/to/countries.json
#
# Optional JSON file format:
#   ["United States", "Canada", "Mexico"]
#   or
#   [{"name": "United States", "code": "US"}, {"name": "Canada", "code": "CA"}]

DEFAULT_COUNTRIES = [
    {"name": "United States", "code": "US"},
    {"name": "Canada", "code": "CA"},
    {"name": "United Kingdom", "code": "GB"},
    {"name": "France", "code": "FR"},
    {"name": "Germany", "code": "DE"},
    {"name": "Spain", "code": "ES"},
    {"name": "Italy", "code": "IT"},
    {"name": "Japan", "code": "JP"},
    {"name": "China", "code": "CN"},
    {"name": "India", "code": "IN"},
    {"name": "Australia", "code": "AU"},
    {"name": "Brazil", "code": "BR"},
    {"name": "Mexico", "code": "MX"},
    {"name": "Russia", "code": "RU"},
    {"name": "South Korea", "code": "KR"},
    {"name": "Netherlands", "code": "NL"},
    {"name": "Sweden", "code": "SE"},
    {"name": "Norway", "code": "NO"},
    {"name": "Denmark", "code": "DK"},
    {"name": "Poland", "code": "PL"},
]

class Command(BaseCommand):
    help = "Populate Country table (uses the Country model)."

    def add_arguments(self, parser):
        parser.add_argument(
            '--file', '-f',
            dest='file',
            help='Optional JSON file with country names or objects to import',
            default=None
        )
        parser.add_argument(
            '--commit',
            action='store_true',
            help='Actually save changes (default: will save). Included for parity; no dry-run implemented.',
        )

    def _model_fields(self):
        # return a set of simple writable field names on the model we can populate
        meta = Country._meta
        field_names = set()
        for f in meta.get_fields():
            # skip relations and auto fields
            if getattr(f, 'auto_created', False):
                continue
            name = getattr(f, 'name', None)
            if not name:
                continue
            # skip many-to-many and related fields
            if getattr(f, 'many_to_many', False) or getattr(f, 'one_to_many', False):
                continue
            field_names.add(name)
        return field_names

    def _normalize_input(self, data):
        """
        Accepts:
          - list of strings -> convert to {"name": string}
          - list of dicts -> keep as-is
        """
        normalized = []
        for item in data:
            if isinstance(item, str):
                normalized.append({"name": item})
            elif isinstance(item, dict):
                normalized.append(item)
            else:
                # ignore unknown types
                continue
        return normalized

    def handle(self, *args, **options):
        file_path = options.get('file')
        # load input
        if file_path:
            if not os.path.exists(file_path):
                raise CommandError(f"File not found: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as fh:
                try:
                    raw = json.load(fh)
                except Exception as exc:
                    raise CommandError(f"Failed to parse JSON file: {exc}")
            items = self._normalize_input(raw)
            if not items:
                self.stdout.write(self.style.WARNING("No valid country entries found in file; using defaults."))
                items = DEFAULT_COUNTRIES
        else:
            items = DEFAULT_COUNTRIES

        model_fields = self._model_fields()
        created = 0
        updated = 0
        skipped = 0

        with transaction.atomic():
            for entry in items:
                # Build kwargs only from model fields to avoid errors
                kwargs = {}
                # prefer 'name' key presence for lookup; fallback to 'code' if present
                lookup = {}
                if 'name' in entry and 'name' in model_fields:
                    lookup['name'] = entry['name']
                elif 'code' in entry and 'code' in model_fields:
                    lookup['code'] = entry['code']
                else:
                    # cannot determine unique lookup field; skip
                    skipped += 1
                    continue

                for k, v in entry.items():
                    if k in model_fields:
                        kwargs[k] = v

                obj, was_created = Country.objects.update_or_create(defaults=kwargs, **lookup)
                if was_created:
                    created += 1
                else:
                    # update_or_create may have updated fields
                    updated += 1

        self.stdout.write(self.style.SUCCESS(f"Countries processed: created={created}, updated={updated}, skipped={skipped}"))