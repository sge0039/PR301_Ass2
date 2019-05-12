import unittest
from Model.uml_interpreter import UmlInterpreter


class UmlInterpreterTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # Arrange
        content = [
                '@ startuml\n',
                '\n',
                'Player -- Test\n',
                '\n',
                'class Player{\n',
                'Player: Test\n',
                'x: Integer\n',
                'y: Integer\n',
                'move()\n',
                'canMove(): Boolean\n',
                '}\n',
                '\n',
                '@enduml\n'
        ]
        interp = UmlInterpreter()
        expected_result = [{'attribute': ['x:Integer', 'y:Integer'], 'class': 'Player',
                            'method': ['move()', 'canMove():Boolean'], 'relationship': ['Player:Test']}]
        # Act
        actual_result = interp.uml_decoder(content)
        # Assert
        self.assertEqual(actual_result, expected_result, 'Expected to be a List of Strings')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # with more details
    # unittest.main()
    # Arrange
    # Act
    # Assert
