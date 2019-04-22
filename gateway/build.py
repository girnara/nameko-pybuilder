"""
    A Gateway Service to integrate with orders and products service using nameko event dispatcher and
    built with pybuilder.
"""

from pybuilder.core import use_plugin, init, Author

use_plugin('filter_resources')

use_plugin('python.core')
use_plugin('python.coverage')
use_plugin('python.pyfix_unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.pydev')
use_plugin('python.distutils')

name = 'nameko-gateway'
authors = [Author('Abhay Girnara', 'girnara.abhay@gmail.com')]
license = 'Test License, Version 2.0'
summary = 'Gateway Service for Interacting multiple micro-services internally'
url = 'https://github.com/girnara/nameko-pybuilder'
version = '1.0.0'


default_task = ['clean','install_dependencies', 'analyze', 'publish']


@init
def set_properties (project):
    project.build_depends_on('coverage')
    project.build_depends_on('pyassert')
    project.build_depends_on('pyfix')
    project.build_depends_on('nameko')
    project.depends_on('marshmallow')
    project.depends_on('werkzeug')
    project.set_property('coverage_break_build', False)
    project.set_property('dir_source_main_python', 'gateway')
    project.set_property('flake8_break_build', False)
