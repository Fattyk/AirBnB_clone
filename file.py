#!/usr/bin/env python3
"""Add a file to test pycodestyle compliant"""
from datetime import datetime


def print_datetime():
    """Print the current naive datetime"""
    print(datetime.now())


print_datetime()
