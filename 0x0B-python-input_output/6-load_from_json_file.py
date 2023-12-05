#!/usr/bin/python3
"""Crates a JSON"""
import json


def load_from_json_file(filename):
    """Make obj from JSON file"""
    with open(filename) as f:
        return json.load(f)
