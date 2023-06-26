import re

phrase = " Do  or do   not   there   is  no try   "

phrase_no_space = re.sub(r'\s+', '', phrase);

print(phrase)

print(phrase_no_space)