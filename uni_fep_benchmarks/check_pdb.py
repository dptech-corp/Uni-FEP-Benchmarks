import os
import glob

def check_pdb(dir_path):
    pdb_file = glob.glob(os.path.join(dir_path, "*.pdb"))
    sdf_file = glob.glob(os.path.join(dir_path, "*.sdf"))
    if not pdb_file or not sdf_file:
        print(dir_path)

def main():
    dirs = [d for d in glob.glob("*") if os.path.isdir(d)]
    for dir in dirs:
        check_pdb(dir)

if __name__ == "__main__":
    main()
