#!/usr/bin/python
 # -*- coding: utf-8 -*-

from pprint import pprint

def get_par(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            space = line.find(' ')
            if space != -1:
                try:
                    par = int(line[:space])
                    result[par] = line[space:]
                except ValueError:
                    pass
    return result

if __name__ == '__main__':
    pprint(get_par('par_input.txt'))
