#    Copyright 2014 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from fnmatch import fnmatch
import os


def iterfiles(dir_path, file_pattern):
    """Returns generator where each item is a path to file, that satisfies
    file_patterns condtion

    :param dir_path: path to directory, e.g /etc/puppet/
    :param file_pattern: unix filepattern to match files
    """
    for root, dirs, file_names in os.walk(dir_path):
        for file_name in file_names:
            if fnmatch(file_name, file_pattern):
                yield os.path.join(root, file_name)
