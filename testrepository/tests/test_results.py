#
# Copyright (c) 2010 Testrepository Contributors
#
# Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
# license at the users choice. A copy of both licenses are available in the
# project source as Apache-2.0 and BSD. You may not use this file except in
# compliance with one of these two licences.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# license you chose for the specific language governing permissions and
# limitations under that license.

from testtools import TestCase, TestResult

from testrepository.results import TestResultFilter


class ResultFilter(TestCase):

    def test_addSuccess_increases_count(self):
        result = TestResult()
        filtered = TestResultFilter(result)
        filtered.startTest(self)
        filtered.addSuccess(self)
        filtered.stopTest(self)
        self.assertEqual(1, result.testsRun)
