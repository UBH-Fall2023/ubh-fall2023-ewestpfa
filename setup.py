import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "requests","PIL"],
    "zip_include_packages": ["tkinter", "requests","PIL"]
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="boyidiot's Neural Network",
    version="0.1",
    description="Our dad joke slinging chat bot",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)