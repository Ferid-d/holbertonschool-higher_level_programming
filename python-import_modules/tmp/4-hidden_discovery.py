#!/usr/bin/python3
import sys
import importlib.util

if __name__ == "__main__":
    # hidden_4.pyc faylının yolunu göstəririk
    file_path = "/tmp/hidden_4.pyc"

    # modul obyekti yaratmaq
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # modulun bütün atributlarını çap etmək
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
