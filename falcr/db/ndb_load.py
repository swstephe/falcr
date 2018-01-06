# -*- coding: utf8 -*-
import csv
import os
from falcr.config import ROOT
from falcr.db.model import Quotes


def init_data():
    with open(os.path.join(ROOT, 'data', 'quotes.csv')) as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            Quotes(**dict(zip(('quote', 'author'), row))).put()


def test_data():
    print Quotes.random_quote()
    print Quotes.random_quote()
    print Quotes.random_quote()
