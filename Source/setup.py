from cx_Freeze import setup, Executable

exe=Executable(
     script="main.py",
     base="Win32Gui",
     )
includefiles=[]
includes=[]
excludes=[]
packages=["pygame"]
setup(
     version = "1.0",
     description = "Snake clone",
     author = "Joe Zlonicky",
     name = "Snake",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )
