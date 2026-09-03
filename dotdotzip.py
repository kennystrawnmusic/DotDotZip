import tomllib
from zipfile import ZipFile
from argparse import ArgumentParser

def version_from_pyproject_toml():
    try:
        with open("pyproject.toml", "rb") as f:
            pyproject_data = tomllib.load(f)
            return pyproject_data.get("project", {}).get("version", "Unknown")
    except FileNotFoundError:
        return "Unknown"

def main():
    parser = ArgumentParser(description=f"DotDotZip v. {version_from_pyproject_toml()}")
    
    parser.add_argument("--traverse-count", type=int, default=5, help="Number of '../' sequences to prepend")
    parser.add_argument("--zip-name", type=str, required=True, help="Name of the output ZIP archive")
    parser.add_argument("--prepend-path", type=str, required=True, help="Extra path to prepend")
    parser.add_argument("--pack-files", type=str, nargs='+', required=True, help="Names of files to pack")
    
    args = parser.parse_args()
    
    traverse_str = '../'*args.traverse_count
    
    with ZipFile(args.zip_name, 'w') as zf:
        for file_name in args.pack_files:
            try:
                zf.write(file_name, arcname=f"{traverse_str}{args.prepend_path}{file_name}")
            except FileNotFoundError:
                print(f"Error: The file '{file_name}' does not exist.")

if __name__ == '__main__':
    main()