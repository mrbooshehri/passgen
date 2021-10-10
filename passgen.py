#! /usr/bin/env python

import random
import sys
import re
import os

# Constants
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
number = "1234567890"
symbol = "!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

# Default options
up, low, num, sym, clipboard = True, True, True, True, False
length = 20

# Help
help = "Password generator v1.0\nBy defaults generated password has 20 characters contains uppercase, lowercase, number, and symbol. \
\nOther options\n-nu\tno uppercase\n-nl\tno lowercase\n-nn\tno number\n-ns\tno symbols\n-NUM custom length. ex -14\n-c\tcopy to clipboard"

# Input arguments
args = sys.argv
len_regex = '^-\d+'

if (len(args) > 5):
    print("error: too much input arguments")
    exit

for arg in args:
  if arg == '-nu':
      up = False
  if arg == '-nl':
      low = False
  if arg == '-nn':
      num = False
  if arg == '-ns':
      sym = False
  if arg == '-h':
      print(help)
  if re.match(len_regex, arg):
      length = int(arg[1:])
  if arg == '-c':
      clipboard =True

# Making phrase
phrase = ""

if up:
    phrase += uppercase
if low:
    phrase += lowercase
if num:
    phrase += number
if sym:
    phrase += symbol

# Generate password
password = ''.join(random.choices(phrase, k=length))
print(password)
if clipboard:
    os.system(f"echo \"{password}\" | xsel -bi")
