# -*- coding: utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='Pynq',
      version=version,
      description="Pynq is a Python-only implementation of LINQ.",
      long_description="""Pynq is a Python-only implementation of LINQ. It uses an Expression Tree based approach to querying any domain (collections, db, etc).""",
      classifiers=["Development Status :: 2 - Pre-Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved",
                   "Natural Language :: English",
                   "Programming Language :: Python :: 2.5"], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Linq Language Integrated Query Python',
      author='Bernardo Heynemann',
      author_email='heynemann@gmail.com',
      url='http://www.pynq.org',
      license='OSI',
      packages=["pynq", "pynq.providers"],
      package_data = {
      },
      include_package_data=False,
      scripts = [],
      zip_safe=True,
      install_requires=[
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
