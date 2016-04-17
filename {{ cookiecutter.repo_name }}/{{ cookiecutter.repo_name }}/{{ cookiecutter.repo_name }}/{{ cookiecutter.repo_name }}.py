#!/usr/bin/env python

import jinja2
from giant.giant_base import BaseGiant{{ cookiecutter.project_type|capitalize }}
import os

class SwaggerPirate(BaseGiant{{ cookiecutter.project_type|capitalize }}):

    def custom_variables(self):
        '''Additional variables to make available to your templates.'''
        return {
            'generated_citation': 'Plugin generated using giant-plugin!',
        }

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