from SublimeLinter.lint import Linter, util


class Cpplint(Linter):
    cmd = ('cpplint', '${args}', '${file}')
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)'
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH  # errors are on stderr
    defaults = {
        'selector': 'source.c, source.c++',
        '--filter=,': '',
        '--linelength=,': '',
    }

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that the error:
            No copyright message found.
            You should have a line: "Copyright [year] <Copyright Owner>"  [legal/copyright] [5]
        that appears on line 0 (converted to -1 because of line_col_base), can be displayed.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is not None and line == -1 and message:
            line = 0

        return match, line, col, error, warning, message, near
