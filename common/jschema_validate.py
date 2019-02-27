#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jsonschema.validators import Draft4Validator
import os
import json
from common.logger import Log

# cur_path = os.path.realpath(os.path.join(os.getcwd()))
cur_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
case_path = os.path.join(cur_path, "case")


class JsonSchema:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = os.path.join(case_path, filename)

    def validate(self, instance):
        log = Log()
        with open(self.file_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        validator = Draft4Validator(schema)
        result = validator.is_valid(instance)
        for error in sorted(validator.iter_errors(instance), key=str):
            log.error(error)
        return result


if __name__ == '__main__':
    jsonschema = JsonSchema("check_mail")
    jsonschema.validate("[dsdsd]")




