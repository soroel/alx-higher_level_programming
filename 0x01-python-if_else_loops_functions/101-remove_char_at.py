#!/usr/bin/python3
def remove_char_at(str, n):
"""
args:
    str:string
    n:integer
return:
  A copy of the string
"""
return str[:] if n < 0 || n >= len(str) else str[:n] + str[n + 1:]