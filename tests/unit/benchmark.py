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

import sys
import time 
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq import From

ITERATIONS = 50000

def main():
    class OtherValue(object):
        def __init__(self, value):
            self.value = value
            
    class OneValue(object):
        def __init__(self, value):
            self.value = OtherValue(value)

    start_time = time.time()
    
    fixed_col = [OneValue(1), OneValue(2), OneValue(3)]
    
    for i in range(ITERATIONS):
        total = From(fixed_col).avg("item.value.value")

    print "AVG FIXED COL OPERATION - %d iterations took %.2f" % (ITERATIONS, (time.time() - start_time))

    dynamic_col = [OneValue(item) for item in range(ITERATIONS/2)]

    start_time = time.time()

    for i in range(2):
        total = From(dynamic_col).avg("item.value.value")

    print "AVG %d ITEMS OPERATION - 2 iterations took %.2f" % (ITERATIONS/2, (time.time() - start_time))

if __name__ == '__main__':
    sys.exit(main())


