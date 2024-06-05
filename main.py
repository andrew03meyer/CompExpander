import sys
import os

sys.path.append(os.getcwd())


import cli.cli as CompExp 

def main():
    # print(len([1,2,3]))
    CompExp.compWriteMenu()

if __name__ == '__main__':
    main()