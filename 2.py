#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    dict1 = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
        }

    dict_items = dict1.items()
    new_dict = {}

    for key, value in dict_items:
        new_dict.setdefault(value, key)

    print(new_dict)
