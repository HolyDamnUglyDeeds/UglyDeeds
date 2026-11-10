#!/usr/bin/env python3
from random import randint, random
from pathlib import Path

css = Path('style.org.css')
main = Path('main.org.md')

print(css.read_text(encoding='utf8'))