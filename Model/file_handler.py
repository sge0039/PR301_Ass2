try:
    import pickle
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    print(ImportError)


class FileHandler:
    def __init__(self):
        self.root = Tk()

    def load_from_file(self):
        """
        >>> file_handler = FileHandler()
        >>> file_handler.load_from_file()
        ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        """
        file_name = self.get_file_name()
        with open(file_name, 'r') as f:
            return f.readlines()

    def write_to_file(self, new_file_name, new_file_content):
        """
        >>> f_name = 'doctest_load'
        >>> f_content = 'class LevelEditor:\\n    def __init__(self, block):\\n        self.all_my_blocks = block\\n' \
        '\\n    def get_block(self):\\n        pass\\n'
        >>> file_handler = FileHandler()
        >>> file_handler.get_folder_dir()
        >>> file_handler.write_to_file(f_name, f_content)
        >>> file_handler.load_from_file()
        ['class LevelEditor:\\n', '    def __init__(self, block):\\n', '        self.all_my_blocks = block\\n', '\\n', \
'    def get_block(self):\\n', '        pass\\n']
        """
        folder_location = self.root.directory
        file_location = folder_location + '/' + new_file_name
        with open(file_location + '.py', 'w') as f:
            f.write(new_file_content)

    def write_to_pickle(self, new_file_name, new_file_content):
        folder_location = self.root.directory
        file_location = folder_location + '/' + new_file_name
        with open(file_location + '.pickle', 'wb') as f:
            pickle.dump(new_file_content, f)

    def get_file_name(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select PlantUML",
                                                        filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        assert self.root.filename, 'No file selected'
        return self.root.filename

    def get_folder_dir(self):
        self.root.directory = filedialog.askdirectory(title="Select Save Folder Location")
        assert self.root.directory, 'No save folder selected'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # doctest.testmod(verbose=True)
