"""Sublimelinter plugin for djlint."""
from SublimeLinter.lint import PythonLinter


class Djlint(PythonLinter):
    """Djlint interface.

    Regex output
    ============

    bad.html.dj
    ===============================
    E001 1:1 Variables should be wrapped in a single whitespace. {%this%}
    E001 1:1 Variables should be wrapped in a single whitespace. {%this%}
    E001 2:4 Variables should be wrapped in a single whitespace. is}}


    """

    cmd = "djlint ${temp_file}"
    defaults = {
        "selector": "text.html.django",
    }
    line_col_base = (1, 0)
    multiline = True
    regex = (
        r"^(?:(?P<error>E\d+)|(?P<warning>W\d+))\s"
        r"(?P<line>\d+):"
        r"(?P<col>\d+)\s(?P<message>.+)"
    )
    tempfile_suffix = "html"
