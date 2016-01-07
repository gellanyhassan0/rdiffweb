#!/usr/bin/python
# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2015 Patrik Dufresne Service Logiciel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Created on Dec 29, 2015

@author: Patrik Dufresne
"""

from __future__ import unicode_literals

import logging
import unittest

from rdiffweb.test import WebCase


class HistoryPageTest(WebCase):

    login = True

    reset_app = True

    reset_testcases = True

    def _history(self, repo):
        return self.getPage("/history/" + repo + "/")

    def test_history(self):
        self._history(self.REPO)
        self.assertInBody("2014-11-01 20:51:18")
        self.assertInBody("2014-11-01 20:18:11")
        self.assertInBody("2014-11-01 20:12:45")
        self.assertInBody("2014-11-01 18:07:19")
        self.assertInBody("2014-11-01 16:30:50")
        self.assertInBody("2014-11-01 16:30:22")
        self.assertInBody("2014-11-01 15:51:29")
        self.assertInBody("2014-11-01 15:51:15")
        self.assertInBody("2014-11-01 15:50:48")
        self.assertInBody("2014-11-01 15:50:26")
        self.assertInBody("2014-11-01 15:49:47")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
