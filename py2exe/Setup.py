import cx_Freeze
import os

print("This Program uses 'cx_Freeze' libary\nBut No additional Dependence Option in not included")

foo = input('Py Script Name: ')
var = input('Exe File Name: ')

executables = [cx_Freeze.Executable(foo)]

cx_Freeze.setup(
    name=var,
    options={"build_exe": {"packages": ["os"],}},
    executables=executables
)
# Clearing the Screen
os.system('cls')
print('You EXE file is here >> \\build\exe.win-amd64-3.10\\' + var + '.exe' )