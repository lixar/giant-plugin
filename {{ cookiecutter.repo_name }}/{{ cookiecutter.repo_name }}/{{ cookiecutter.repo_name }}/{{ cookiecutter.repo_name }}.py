#!/usr/bin/env python

import jinja2
from openapi_pirate.openapi_pirate import BasePirate
import os

class SwaggerPirate(BasePirate):
        
    def plugin_name(self):
        '''Return the name of the plugin.'''
        return '{{ cookiecutter.library_name }}'
        
    def plugin_command(self):
        '''Returns a tuple containing:
            * the command line argument to execute the plugin,
            * the help documentation describing the command.'''
        return ('{{ cookiecutter.repo_name }}', '{{ cookiecutter.description }}')

    def loader(self):
        '''Returns the Jinja2 template loader for your templates.'''
        path = os.path.dirname(os.path.realpath(__file__))
        return jinja2.FileSystemLoader(os.path.join(path, 'templates'))

    def helpers_loader(self):
        '''Returns the Jinja2 template loader for your template helpers.'''
        path = os.path.dirname(os.path.realpath(__file__))
        return jinja2.FileSystemLoader(os.path.join(path, 'template-res'))

    def customize_env(self, environment):
        '''Call to allow plugin customization of the Jinja2 environment.'''
        pass
        
    def filters(self):
        '''Call to allow plugin customization of available Jinja2 filters.'''
        pass
                
    def tests(self):
        '''Call to allow plugin customization of available Jinja2 tests.'''
        pass