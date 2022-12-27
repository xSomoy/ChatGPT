import cx_Freeze

executables = [cx_Freeze.Executable("script.py")]

cx_Freeze.setup(
    name="Executable Name",
    options={"build_exe": {"packages": ["os"],}},
    executables=executables
)
