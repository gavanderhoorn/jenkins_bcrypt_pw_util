#!/usr/bin/env python

# Copyright (c) 2018, G.A. vd. Hoorn
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import argparse

_OS_EX_USAGE=64
_OS_EX_UNAVAILABLE=69

try:
    import bcrypt
except:
    sys.stderr.write("Cannot import bcrypt library, do you have it installed?\n")
    sys.exit(_OS_EX_UNAVAILABLE)

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose')
parser.add_argument('PASSWORD', help='Plain text to hash.')
args = parser.parse_args()

plaintext = args.PASSWORD.encode('UTF-8')

# https://gist.github.com/Voronenko/d50fc04cbbf26dfed37d
# https://pypi.python.org/pypi/bcrypt/3.1.0
pw = bcrypt.hashpw(plaintext, bcrypt.gensalt(10, prefix=b"2a"))

if args.verbose:
    print ("plaintext : {}".format(plaintext.decode('UTF-8')))
    print ("hash      : {}".format(pw.decode('UTF-8')))
    #print ("check     : {}".format("passed" if bcrypt.checkpw(plaintext, pw) else "failed"))
else:
    print (pw.decode('UTF-8'))
