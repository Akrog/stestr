# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License

"""Report stats about a repository. Current vestigial."""

import os
import sys

from stestr.repository import file as file_repo


def get_cli_help():
    pass


def set_cli_opts(parser):
    pass


def run(self):
    # TODO(mtreinish): Add a CLI opt to set repo type
    repo = file_repo.RepositoryFactory().open(os.getcwd())
    sys.stdout.write('%s=%s' % ('runs', repo.count()))
    return 0
