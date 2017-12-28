SublimeLinter-cpplint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-cpplint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-cpplint)

This linter plugin for SublimeLinter provides an interface to [cpplint](https://pypi.python.org/pypi/cpplint). It will be used with files that have the “C++” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `cpplint` is installed on your system. To install `cpplint`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `cpplint` by typing the following in a terminal:
   ```
   [sudo] pip install cpplint
   ```

In order for `cpplint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional settings for SublimeLinter-cpplint

|Setting|Description|
|:------|:----------|
|filter|A comma-separated list of category-filters to apply|
|linelength|The allowed line length (with cpplint >= 0.0.6)|

``filter`` can be a single string (anywhere) or array of strings (anywhere but inline).
