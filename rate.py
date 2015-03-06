#!/usr/bin/env python3
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

    def get_word_rate(self, word):
        w = self.get_word(word)
        return w['NO'] if w else None

if __name__ == '__main__':
    wordrate = WordRate()
    while (1):
        word = input("<字> ")

        if word == 'exit':
            exit()

        for w in word:
            rate =  wordrate.get_word_rate(w)
            if rate:
                print('%s, %s' % (w, rate))
            else:
                print(w)
