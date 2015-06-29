#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaza.settings")

    from utils.models import Country
    Country.objects.initialize()
    
    from utils.models import Currency
    Currency.objects.initialize()
