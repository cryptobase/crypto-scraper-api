#!/usr/bin/env python

import argparse
from os import listdir
from os.path import isfile, join
import re
import sys
import csv

class Generator:
    def __init__(self, path='/Users/wilelb/test'):
        self.path=path

    def list_files(self):
        p = re.compile('(.+)\.(.+)-(.+)-(.+)\.csv')
        files = []
        for f in listdir(self.path):
            if isfile(join(self.path, f)) and p.match(f):
                files.append(f)
        return files

    def generate(self):
        p = re.compile('(.+)\.(.+)-(.+)-(.+)\.csv')
        result = {}
        for f in self.list_files():
            m = p.match(f)
            if m:
                val = m.group(1)
                year = str(m.group(2))
                month = str(m.group(3))
                day = str(m.group(4))
                if year not in result:
                    result[year] = {}
                    result[year][month] = {}
                    result[year][month][day] = {}
                    result[year][month][day]['exchanges'] = [val]
                elif month not in result[year]:
                    result[year][month] = {}
                    result[year][month][day] = {}
                    result[year][month][day]['exchanges'] = [val]
                elif day not in result[year][month]:
                    result[year][month][day] = {}
                    result[year][month][day]['exchanges'] = [val]
                else:
                    result[year][month][day]['exchanges'].append(val)
        return result

    def last(self, days=10):
        list = self.generate()
        for year in list:
            for month in list[year]:
                for day in list[year][month]:
                    for exchange in list[year][month][day]['exchanges']:
                        filename = '%s.%s-%s-%s.csv' % (exchange, year, month, day)
                        list[year][month][day][exchange] = self.load_stats_from_file(filename)
        return list

    def load_stats_from_file(self, file):
        stats = {
            'num': 0,
            'volume': 0,
            'smallest': 0,
            'largest': 0,
            'lowest_price': 0,
            'highest_price': 0,
            'buys': 0,
            'sells': 0
        }

        f = open(join(self.path, file), 'rb')
        try:
            reader = csv.reader(f)
            for row in reader:
                type = row[3]
                amount = float(row[4])
                price = float(row[5])

                stats['num'] += 1
                if type == 'buy':
                    stats['buys'] += 1
                elif type == 'sell':
                    stats['sells'] += 1
                stats['volume'] += amount
                if amount < stats['smallest']:
                    stats['smallest'] = amount
                elif amount > stats['largest']:
                    stats['largest'] = amount
                if price < stats['lowest_price']:
                    stats['lowest_price'] = price
                elif price > stats['highest_price']:
                    stats['highest_price'] = price
        finally:
            f.close()

        return stats

if __name__ == '__main__':
    gen = Generator()
    print(gen.last())
