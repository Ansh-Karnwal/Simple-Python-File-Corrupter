import os
from pathlib import Path
class FileCorrupter:
    def __init__(self, filedir, filename):
        self.filedir = filedir
        self.filename = filename
        self.corrupt_file()
    def corrupt_file(self):
        old_file = os.path.join(self.filedir, self.filename)
        if '.' in self.filename:
            fileext = self.filename.split('.')[1]
        self.filename = self.filename[:self.filename.rindex('.')]
        new_file = os.path.join(self.filedir, f"{self.filename}.txt")
        os.rename(old_file, new_file)
        with open(Path(f"{self.filedir}{self.filename}.txt"), 'w'):
            pass
        next_file = os.path.join(self.filedir, f"{self.filename}.{fileext}")
        os.rename(new_file, next_file)
        
filenameobj = input("Enter the full file name: ")
filedirobj = input("Enter the file directory (remember to add \ at the end): ")
FileCorrupterobj = FileCorrupter(filedirobj, filenameobj)