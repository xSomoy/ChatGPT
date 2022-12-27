import cx_Freeze
print("This Program uses 'cx_Freeze' libary\n But No additional Dependence Option in not included")
foo = input('Py Script Name: ')
var = input('Exe File Name: ')

executables = [cx_Freeze.Executable(foo)]

cx_Freeze.setup(
    name=var,
    options={"build_exe": {"packages": ["os"],}},
    executables=executables
)
