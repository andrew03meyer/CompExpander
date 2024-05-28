import sys
import os

sys.path.append(os.getcwd())


import cli.cli as CompExp 

def main():
    CompExp.compWriteMenu()

if __name__ == '__main__':
    main()