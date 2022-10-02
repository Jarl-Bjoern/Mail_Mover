# Rainer Herold
# Version 0.1
# 17.01.2022

try:
    from os import mkdir, makedirs, remove, rename, system, walk
    from os.path import exists, join
    from re import finditer
    from shutil import copy, SameFileError, SpecialFileError, ReadError, RegistryError, Error, ExecError
    from sys import exit
    from time import sleep
except ModuleNotFoundError as e:
    input(f"Das Modul {e} wurde nicht gefunden.\n\nBitte wenden Sie Sich an den Entwickler.\n\nZum Verlassen, bitte mit Enter bestaetigen.")
