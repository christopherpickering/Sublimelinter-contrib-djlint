"""Sublimelinter plugin for djlint."""
import re

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

    cmd = "djlint ${temp_file} *"
    defaults = {
        "selector": "text.html, text.html.django, text.html.jinja2, text.html.njk, text.html.handlebars",
        "--ignore=,": "",
    }
    line_col_base = (1, 0)

    multiline = True
    re_flags = re.IGNORECASE
    regex = (
        r"^\s+?(?:(?P<warning>\w+\d+))\s"
        r"(?P<line>\d+):"
        r"(?P<col>\d+)\s(?P<message>.+)"
    )
    tempfile_suffix = "html"
