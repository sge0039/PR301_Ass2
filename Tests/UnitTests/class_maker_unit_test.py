import unittest
from Model.class_maker import ClassMaker


class ClassMakerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        name = ''
        c_maker = ClassMaker()
        expected_result = ''
        # Act
        actual_result = c_maker.file_name(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_02(self):
        # Arrange
        name = 'AllCapsDays'
        c_maker = ClassMaker()
        expected_result = 'all_caps_days'
        # Act
        actual_result = c_maker.file_name(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_03(self):
        # Arrange
        name = 'AllCapsDays'
        c_maker = ClassMaker()
        expected_result = 'class AllCapsDays:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_04(self):
        # Arrange
        name = 'newZealand'
        c_maker = ClassMaker()
        expected_result = 'class NewZealand:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_05(self):
        # Arrange
        name = 'thequickbrownfox'
        c_maker = ClassMaker()
        expected_result = 'class Thequickbrownfox:\n'
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_06(self):
        # Arrange
        name = []
        c_maker = ClassMaker()
        expected_result = ''
        # Act
        actual_result = c_maker.attribute_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_07(self):
        # Arrange
        name = ['']
        c_maker = ClassMaker()
        expected_result = '    def __init__(self):\n        self.\n'
        # Act
        actual_result = c_maker.attribute_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_08(self):
        # Arrange
        name = ['allMyBlocks:Float', 'allMyWalls:String']
        c_maker = ClassMaker()
        expected_result = '    def __init__(self):\n        self.all_my_blocks: float\n        self.all_my_walls: str\n'
        # Act
        actual_result = c_maker.attribute_maker(name)
        print(actual_result)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_09(self):
        # Arrange
        name = ['Thequickbrownfox']
        c_maker = ClassMaker()
        expected_result = AttributeError
        # Act
        actual_result = c_maker.class_maker(name)
        # Assert
        self.assertRaises(expected_result, actual_result)
        # self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_10(self):
        # Arrange
        name = 'notType'
        c_maker = ClassMaker()
        expected_result = 'not_data_type'
        # Act
        actual_result = c_maker.get_data_type(name)
        # Assert
        self.assertEqual(expected_result, actual_result)
        # self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_11(self):
        # Arrange
        name = ['one:two', 'abd:xyz']
        c_maker = ClassMaker()
        expected_result = ['one: two', 'abd: xyz']
        # Act
        actual_result = c_maker.get_rel_type(name)
        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_12(self):
        # Arrange
        name = 'Hello:World'
        c_maker = ClassMaker()
        expected_result = TypeError
        # Act
        actual_result = c_maker.get_rel_type(name)
        # Assert
        self.assertRaises(expected_result, actual_result)
        # self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')

    def test_13(self):
        # Arrange
        name = ['hello: world']
        c_maker = ClassMaker()
        expected_result = '        self.hello: world\n'
        # Act
        actual_result = c_maker.relationship_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a Strings')

    def test_14(self):
        # Arrange
        name = ['hello():String']
        c_maker = ClassMaker()
        expected_result = '    def hello(self):\n        return str\n\n'
        # Act
        actual_result = c_maker.method_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a Strings')

    def test_15(self):
        # Arrange
        name = ['getBlock(inputAge, inputName)']
        c_maker = ClassMaker()
        expected_result = '    def get_block(self, input_age,  input_name):\n        pass\n\n'
        # Act
        actual_result = c_maker.method_maker(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a Strings')

    def test_16(self):
        # Arrange
        name = {'class': 'person', 'attribute': ['name:String'], 'method': ['movement():Boolean'],
                'relationship': ['one:two']}
        c_maker = ClassMaker()
        class_name = 'class Person:\n'
        attributes = '    def __init__(self):\n        self.name: str\n        self.one: two\n\n'
        methods = '    def movement(self):\n        return bool\n\n'
        expected_result = {'file_name': 'person', 'file_content': class_name + attributes + methods}
        # Act
        actual_result = c_maker.class_designer(name)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a Strings')

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert
