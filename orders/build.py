#   flask-hello-world
#   Copyright 2012-2013 Michael Gruber, Alexander Metzner
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    A simple flask application tested using pyassert and pyfix and
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

name = 'nameko-orders'
authors = [Author('Abhay Girnara', 'girnara.abhay@gmail.com')]
license = 'Test License, Version 2.0'
summary = 'Orders management service for creating/retrieving the orders'
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
    project.depends_on('sqlalchemy')
    project.depends_on('alembic')
    project.depends_on('nameko_sqlalchemy')
    project.depends_on('psycopg2')
    project.set_property('coverage_break_build', False)
    project.set_property('dir_source_main_python', 'orders')
    project.set_property('flake8_break_build', False)
