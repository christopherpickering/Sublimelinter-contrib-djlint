"""Sublimelinter plugin for djlint."""
import re

from SublimeLinter.lint import WARNING, PythonLinter


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

    cmd = "djlint ${file} ${args} --quiet"
    defaults = {
        "selector": "text.html, text.html.base, text.html.django, text.html.jinja2, text.html.njk, text.html.handlebars",
        "--ignore=,": "",
    }
    line_col_base = (1, 0)

    default_type = WARNING
    multiline = False
    re_flags = re.IGNORECASE
    regex = (
        r"[ ]*?(?:(?P<code>\w+\d+))\s"
        r"(?P<line>\d+):"
        r"(?P<col>\d+)\s(?P<message>.+)"
    )
    temp_suffix = "html"
