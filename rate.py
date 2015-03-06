#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

class WordRate:
    def __init__(self):
        with open('rate.csv') as csvfile:
            self._reader = dict()
            for row in csv.DictReader(csvfile):
                self._reader[row['DWORD']] = [row['NO'], row['BUSHO'], row['JBIHUA']]

    def get_word(self, word):
        try:
            return self._reader[word]
        except KeyError:
            return None

    def get_word_rate(self, word):
        w = self.get_word(word)
        return w[0]

    def get_word_busho(self, word):
        w = self.get_word(word)
        return w[1]

    def get_word_jbihua(self, word):
        w = self.get_word(word)
        return w[2]

if __name__ == '__main__':
    wordrate = WordRate()
    while (1):
        word = input("<字> ")

        if word == 'exit':
            exit()

        for w in word:
            l =  wordrate.get_word(w)
            if l:
                print('%s, %s, %s, %s' % (w, l[0], l[1], l[2]))
            else:
                print(w)
