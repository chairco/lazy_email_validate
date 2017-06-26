# -*- coding: utf-8 -*-

import re

from .email_regexp import VALID_ADDRESS_REGEXP


def validate_email(email):
    match = re.match(VALID_ADDRESS_REGEXP, str(email))
    if match == None:
        return False
    else:
        return True

