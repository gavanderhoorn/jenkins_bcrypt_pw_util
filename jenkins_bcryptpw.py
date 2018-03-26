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

_OS_EX_USAGE=64
_OS_EX_UNAVAILABLE=69

try:
    import bcrypt
except:
    sys.stderr.write("Cannot import bcrypt library, do you have it installed?\n")
    sys.exit(_OS_EX_UNAVAILABLE)

if len(sys.argv) != 2:
    from os.path import basename
    sys.stderr.write("USAGE: {} PASSWORD\n".format(basename(sys.argv[0])))
    sys.exit(_OS_EX_USAGE)

plaintext = sys.argv[1].encode('UTF-8')

# https://gist.github.com/Voronenko/d50fc04cbbf26dfed37d
# https://pypi.python.org/pypi/bcrypt/3.1.0
pw = bcrypt.hashpw(plaintext, bcrypt.gensalt(10, prefix=b"2a"))

print ("plaintext : {}".format(plaintext.decode('UTF-8')))
print ("hash      : {}".format(pw.decode('UTF-8')))
print ("check     : {}".format("passed" if bcrypt.hashpw(plaintext, pw) else "failed"))
