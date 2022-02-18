import os, shutil
from win32com.shell import shell, shellcon
first_path ='C:/Windows/Temp'
second_path = 'C:/Users/Sergey/AppData/Local/Temp'
A = os.listdir(first_path)
B = os.listdir(second_path)
for remove_files in A: #first_path
    file_path = os.path.join(first_path, remove_files)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except:
        pass
for remove_files in B: #second_path
    file_path = os.path.join(second_path, remove_files)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except:
        pass
def empty(confirm=False, show_progress=True, sound=True):
    flags = 0
    if not confirm:
        flags |= shellcon.SHERB_NOCONFIRMATION
    if not show_progress:
        flags |= shellcon.SHERB_NOPROGRESSUI
    if not sound:
        flags |= shellcon.SHERB_NOSOUND
    shell.SHEmptyRecycleBin(None, None, flags)

empty()
