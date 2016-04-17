#!/usr/bin/env python

full_name = "{{ cookiecutter.full_name }}"
email = "{{ cookiecutter.email }}"
language = "{{ cookiecutter.project_language }}"
framework = "{{ cookiecutter.project_framework }}"
project_type = "{{ cookiecutter.project_type }}"
repo_name = "{{ cookiecutter.repo_name }}"
command = "{{ cookiecutter.command }}"
version = "{{ cookiecutter.version }}"
copyrightholder = "{{ cookiecutter.copyrightholder }}"
description = "{{ cookiecutter.description }}"
company = "{{ cookiecutter.company }}"
website = "{{ cookiecutter.website }}"
library_name = "{{ cookiecutter.library_name }}"

import re
import sys


constraints = [
  ('^[\w]+$', repo_name, 'repo_name must contain alphanumeric characters and "_" only.'),
  ('^.{2,}$', repo_name, 'repo_name must not be "_" only.'),
  ('^([a-z0-9]+-)*[a-z0-9]+$', command, 'command must be lowercase, numbers and dashes.'),
  ('^.+$', language, 'language must be set.'),
  ('^.+$', framework, 'framework must be set.'),
  ('(client|server)$', project_type, 'framework must be set.'),
  ('^[\w]+$', library_name, 'library_name must contain alphanumeric characters and "_" only.'),
]

for regex, value, message in constraints:
  if not re.match(regex, value):
    print(message)
    sys.exit(1)

