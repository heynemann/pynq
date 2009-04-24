#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Guard(object):
    @classmethod
    def against_empty(cls, argument, message=None):
        if argument is None or str(argument) == "":
            raise ValueError(message and message or "One of the arguments is required and was not filled.")

    @classmethod
    def accepts(cls, argument, types, message=None):
        argument_is_of_types = False
        for argument_type in types:
            if isinstance(argument, argument_type):
                argument_is_of_types = True
                break

        if not argument_is_of_types:
            error_message = "One of the arguments should be of types %s and it isn't."
            raise ValueError(message and message or error_message % ", ".join([str(tp) for tp in types]))
