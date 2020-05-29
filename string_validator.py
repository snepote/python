#!/usr/bin/python3
import re

class StringValidator:
    username_regex  = re.compile("^[a-z]+\.[a-z]+$")
    domain_regex    = re.compile("^[a-zA-Z0-9u00a1-\uffff0-]{2,}\.[a-zA-Z0-9u00a1-\uffff0-]{2,}(\S*)$")

    @staticmethod
    def __match(regex, string):
        return False if not regex.match(string) else True

    def is_username(__self__, string):
        return __self__.__match(__self__.username_regex, string)

    def is_domain(__self__, string):
        return __self__.__match(__self__.domain_regex, string)
