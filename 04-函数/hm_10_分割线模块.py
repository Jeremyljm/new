#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_line(char,times):

    print(char * times)


def print_lines(char,times):

    row = 0

    while row < 5:

        print_line(char, times)

        row += 1

# print_lines('%',60)

name = "黑马程序员"