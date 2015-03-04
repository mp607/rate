#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class WordRate:
    def __init__(self):
        with open('rate.csv') as csvfile:
            self._reader = list(csv.DictReader(csvfile))

    def get_word(self, word):
        for row in self._reader:
            if word == row['DWORD']:
                return row

if __name__ == '__main__':
    wordrate = WordRate()
    while (1):
        word = raw_input("<字> ")
        w =  wordrate.get_word(word)
        if w:
            print w['NO']
        else:
            exit()
