import time
import json
import random
import string
import os, sys
import requests
import collections
import urllib.request
from bs4 import BeautifulSoup

nu = '\033[0m'
re = '\033[1;31m'
gr = '\033[1;32m'
cy = '\033[1;36m'

def write(in_text):
	for char in in_text:
		time.sleep(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
write(f"\n{gr}[+]{re} Thanks for using my tool...")
print("\n------------------------")
print("\nsupport us to make more tools")
print("\n------------------------")
print('\n')
