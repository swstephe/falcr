# -*- coding: utf8 -*-
import csv
import os
from falcr.db.model import Quotes, AppUsers

CWD = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(CWD, 'quotes.csv')) as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        Quotes(**dict(zip(('quote', 'author'), row))).put()

print Quotes.random_quote()
print Quotes.random_quote()
print Quotes.random_quote()
