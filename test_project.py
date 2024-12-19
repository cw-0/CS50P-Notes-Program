import pytest
import os
import stat
from unittest import mock
from project import openpy, open_read_only, openpyfiles, clear_console





# ---- OPEN PY ----

def test_openpy():
    file_path = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\calculator.py"
    with mock.patch("subprocess.run") as mock_run:
        openpy(file_path)

        mock_run.assert_called_once_with(["python", "-m", "idlelib.idle", file_path])


def test_openpy_ERROR():
    error_file_path = r"D:\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\Errorcalculator.py"

    with pytest.raises(FileNotFoundError):
        openpy(error_file_path)




# ---- OPEN READ ONLY ----

def test_open_read_only():
    file_path = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\calculator.py"
    with mock.patch("subprocess.run") as mock_run, mock.patch("os.chmod") as mock_chmod:
        open_read_only(file_path)

        mock_run.assert_called_once_with(["python", "-m", "idlelib.idle", file_path])
        mock_chmod.assert_called_once_with(file_path, stat.S_IREAD)

def test_open_read_only_ERROR():
    error_file_path = r"D:\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\Errorcalculator.py"

    with pytest.raises(FileNotFoundError):
        open_read_only(error_file_path)





# ---- OPEN PY FILES ----

def test_openpyfiles():
    with mock.patch("project.openpy") as mock_openpy:
        file_1 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\calculator.py"
        file_2 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\test_calculator.py"
        
        openpyfiles(file_1, file_2)

        mock_openpy.assert_any_call(file_1)
        mock_openpy.assert_any_call(file_2)

        assert mock_openpy.call_count == 2

def test_openpyfiles_ERROR():
    # 2 Error Files
    with mock.patch("project.openpy") as mock_openpy:
        file_1 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\Errorcalculator.py"
        file_2 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\Errortest_calculator.py"
        
        with pytest.raises(FileNotFoundError):
            openpyfiles(file_1, file_2)

    # 1 Error File
    with mock.patch("project.openpy") as mock_openpy:
        file_1 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\calculator.py"
        file_2 = r"D:\VScode\Projects\CS50\Final Project\Assets\Week 0 Basics of Python and Terminal\Calculator\Errortest_calculator.py"
        
        with pytest.raises(FileNotFoundError):
            openpyfiles(file_1, file_2)

        mock_openpy.assert_any_call(file_1)

        assert mock_openpy.call_count == 1






# ---- CLEAR CONSOLE ----

def test_clear_console():
    with mock.patch("os.system") as mock_system:
        if os.name == "nt":
            clear_console()
            mock_system.assert_called_once_with("cls")
        else:
            clear_console
            mock_system.assert_called_once_with("clear")