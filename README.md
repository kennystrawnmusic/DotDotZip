After having viewed some interesting content including a [NahamSec video](https://youtu.be/4sKlbMiGWAw) on a little-known technique for hiding path traversals inside ZIP files and hearing that Python can pull that off, I just had to try creating a tool for generating such payloads.

The result, of course, is this: a tool for creating the perfect upload packer.

# Installation

```
pipx install git+https://github.com/kennystrawnmusic/DotDotZip
```

# Usage

```
$ python3 dotdotzip.py --help
usage: dotdotzip.py [-h] [--traverse-count TRAVERSE_COUNT] --zip-name ZIP_NAME
                    --prepend-path PREPEND_PATH
                    --pack-files PACK_FILES [PACK_FILES ...]

DotDotZip v. 0.2.2

options:
  -h, --help            show this help message and exit
  --traverse-count TRAVERSE_COUNT
                        Number of '../' sequences to prepend
  --zip-name ZIP_NAME   Name of the output ZIP archive
  --prepend-path PREPEND_PATH
                        Extra path to prepend
  --pack-files PACK_FILES [PACK_FILES ...]
                        Names of files to pack
```

Example:

```
$ python3 dotdotzip.py --zip-name test.zip --prepend-path '/Users/realkstrawn93/Desktop' --traverse-count 15 --pack-files pyproject.toml
```