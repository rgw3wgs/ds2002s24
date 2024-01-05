import os

from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/nmagee/ds1002/main/data/unique-ids.txt'
file = 'unique-ids.txt'
urlretrieve(url, file)

with open('unique-ids.txt', 'r') as f:
  for line in f:
    print(line)