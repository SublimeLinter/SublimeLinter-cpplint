#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2013 NotSqrt
#
# License: MIT
#

"""This module exports the Cpplint plugin class."""

from SublimeLinter.lint import Linter, util


class Cpplint(Linter):

    """Provides an interface to cpplint."""

    syntax = 'c++'
    cmd = ('cpplint', '*', '@')
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)'
    tempfile_suffix = '.cpp'
    error_stream = util.STREAM_BOTH  # errors are on stderr
    defaults = {
        '--filter=,': '',
    }

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that the error:
            No copyright message found.
            You should have a line: "Copyright [year] <Copyright Owner>"  [legal/copyright] [5]
        that appears on line -1 can be displayed.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is not None and int(line) is -1 and message:
            line = 0

        return match, line, col, error, warning, message, near
