#!/usr/bin/python3
import re

username_regex  = re.compile(r'^[a-z]+\.[a-z]+$')
domain_regex    = re.compile(r'^[a-zA-Z0-9u00a1-\uffff0-]{2,}\.[a-zA-Z0-9u00a1-\uffff0-]{2,}(\S*)$')

def is_username(string):
    return False if not username_regex.match(string) else True

def is_domain(string):
    return False if not domain_regex.match(string) else True
