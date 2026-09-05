import os
from idaes_ui import fv


def main():
    os.fork()
    fv.visualize()
    print("hello world", os.getpid())


if __name__ == "__main__":
    main()
