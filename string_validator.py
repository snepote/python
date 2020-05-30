#!/usr/bin/python3
import re

username_regex  = re.compile(r'^[a-z]+\.[a-z]+$')
domain_regex    = re.compile(r'^[a-z0-9]+\.?[a-z-0-9]+(\.[a-z]{2,})+$')

def is_username(string):
    return False if not username_regex.match(string) else True

def is_domain(string):
    if len(string) > 253:
        return False
    return False if not domain_regex.match(string) else True
