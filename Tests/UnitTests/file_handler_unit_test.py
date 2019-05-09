import unittest
from Model.file_handler import FileHandler


class FileHandlerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        file_name = 'InputOutputFiles/unit_test.txt'
        file_handler = FileHandler()
        expected_result = ['@startuml\n', 'class LevelEditor{\n', '  allMyBlocks\n', '  getBlock()\n', '}\n',
                           '@enduml']
        # Act
        actual_result = file_handler.load_from_file(file_name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_02(self):
        # Arrange
        file_handler = FileHandler()
        expected_result = ['@startuml\n', 'class LevelEditor{\n', '  allMyBlocks\n', '  getBlock()\n', '}\n',
                           '@enduml']
        # Act
        actual_result = file_handler.load_from_file()
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_03(self):
        # Arrange
        file_name = 'unit_test_load'
        file_content = 'class LevelEditor:\n    def __init__(self, block):\n        self.all_my_blocks = block\n\
\n    def get_block(self):\n        pass\n'
        file_dir = 'InputOutputFiles'
        file_handler = FileHandler()
        expected_result = ['class LevelEditor:\n', '    def __init__(self, block):\n',
                           '        self.all_my_blocks = block\n', '\n', '    def get_block(self):\n', '        pass\n']
        # Act
        file_handler.get_folder_dir(file_dir)
        file_handler.write_to_file(file_name, file_content)
        actual_result = file_handler.load_from_file(file_dir + '/' + file_name + '.py')
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_04(self):
        # Arrange
        file_name = 'unit_test_load'
        file_content = 'class LevelEditor:\n    def __init__(self, block):\n        self.all_my_blocks = block\n\
\n    def get_block(self):\n        pass\n'
        file_dir = 'InputOutputFiles'
        file_handler = FileHandler()
        expected_result = ['class LevelEditor:\n', '    def __init__(self, block):\n',
                           '        self.all_my_blocks = block\n', '\n', '    def get_block(self):\n',
                           '        pass\n']
        # Act
        file_handler.get_folder_dir()
        file_handler.write_to_file(file_name, file_content)
        actual_result = file_handler.load_from_file(file_dir + '/' + file_name + '.py')
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_05(self):
        # Arrange
        file_name = 'unit_test_load'
        file_content = 'class LevelEditor:\n    def __init__(self, block):\n        self.all_my_blocks = block\n\
\n    def get_block(self):\n        pass\n'
        file_dir = 'InputOutputFiles'
        file_handler = FileHandler()
        expected_result = ['€\x03X|\x00\x00\x00class LevelEditor:\n', '    def __init__(self, block):\n',
                           '        self.all_my_blocks = block\n', '\n', '    def get_block(self):\n',
                           '        pass\n', 'q\x00.']
        # Act
        file_handler.get_folder_dir(file_dir)
        file_handler.write_to_pickle(file_name, file_content)
        actual_result = file_handler.load_from_file(file_dir + '/' + file_name + '.pickle')
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert
