SublimeLinter-contrib-djlint
================================

[![Build Status](https://travis-ci.com/christopherpickering/SublimeLinter-contrib-djlint.svg?branch=master)](https://travis-ci.com/christopherpickering/SublimeLinter-contrib-djlint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [djlint](https://pypi.org/manage/project/djlint/releases/) for linting Django Templates.


## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `djlint` is installed on your system.

```sh
pip install djlint
```

In order for `djlint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

Warnings can be ignored from the sublimelinter settings:

```json
// SublimeLinter Settings - User
{
    "linters": {
       "djlint": {
          "ignore": "W013"
       }
    }
}

```

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
