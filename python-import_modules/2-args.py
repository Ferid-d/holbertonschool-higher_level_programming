#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1  # script adı çıxılacaq

    if argc == 0:
        print("0 arguments.")
    else:
        # argument(s) sözünü düzgün seçirik
        word = "argument" if argc == 1 else "arguments"
        print("{} {}:".format(argc, word))

        # arqumentləri çap edirik
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
