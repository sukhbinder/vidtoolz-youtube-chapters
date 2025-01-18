# vidtoolz-youtube-chapters

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-youtube-chapters.svg)](https://pypi.org/project/vidtoolz-youtube-chapters/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-youtube-chapters?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-youtube-chapters/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-youtube-chapters/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-youtube-chapters/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-youtube-chapters/blob/main/LICENSE)

Write formated youtube chapters with text inputs

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-youtube-chapters
```
## Usage

type ``vid chapters --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-youtube-chapters
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
