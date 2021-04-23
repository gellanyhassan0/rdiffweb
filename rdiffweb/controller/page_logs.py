# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2021 rdiffweb contributors
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

import logging

import cherrypy
from rdiffweb.controller import Controller, validate_int, validate_date
from rdiffweb.controller.dispatch import poppath

# Define the logger
logger = logging.getLogger(__name__)


@poppath()
class LogsPage(Controller):

    @cherrypy.expose
    def default(self, path, limit='10', date=None, file=None):
        """
        Called to show every graphs
        """
        limit = validate_int(limit)
        if date is not None:
            date =  validate_date(date)

        repo_obj = self.app.store.get_repo(path)

        # Read log file data
        data = None
        try:
            if file == 'backup.log':
                data = repo_obj.backup_log.tail()
            elif file == 'restore.log':
                data = repo_obj.restore_log.tail()
            elif date:
                try:
                    data = repo_obj.error_log[date].tail()
                except KeyError:
                    raise cherrypy.HTTPError(400, _('Invalid date.'))
        except FileNotFoundError:
            # If the file doesn't exists, swallow the error.
            pass
            
        
        # Get error log list
        if limit < len(repo_obj.error_log):
            error_logs = repo_obj.error_log[:-limit - 1:-1]
        else:
            error_logs = repo_obj.error_log

        params = {
            'repo': repo_obj,
            'limit': limit,
            'date':date,
            'file': file,
            'data': data,
            'error_logs': error_logs
        }
        return self._compile_template("logs.html", **params)
