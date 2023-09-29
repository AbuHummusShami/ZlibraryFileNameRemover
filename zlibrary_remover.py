import os
import sys

EXTENSION = ' (Z-Library)'
def main():
    DIR = str(input("Enter folder path: "))

    DIR = DIR.replace("\\", "/")
    try:
        DIR_LIST = os.listdir(DIR)
    except FileNotFoundError:
        print("Enter valid folder directory")
        return
    this = os.path.basename(sys.argv[0])
    i = 0
    for file in DIR_LIST:
        src = DIR + file
        name = DIR + file.replace(EXTENSION, '')
        if file == this:
            pass
        else:
            try:
                if EXTENSION in file:
                    os.rename(src, name)
                    print(f"Filtered {file} --> {file.replace(EXTENSION, '')}")
                    i+=1
            except x:
                print(x)
    if i > 0:
        print(f"\nFiltering complete! {i} file(s) were filtered")
    else:
        print(f"No files were found with '{EXTENSION.strip()}' found in their names.")

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()
