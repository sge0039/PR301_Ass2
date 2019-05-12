from Tests.UnitTests.class_maker_unit_test import ClassMakerTest
from Tests.UnitTests.file_handler_unit_test import FileHandlerTest
from Tests.UnitTests.validate_data_unit_test import ValidateDataTest
from Tests.UnitTests.view_unit_test import ViewTest
from Tests.UnitTests.uml_interpreter_unit_test import UmlInterpreterTest

import unittest
import coverage


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(ClassMakerTest))
    the_suite.addTest(unittest.makeSuite(FileHandlerTest))
    the_suite.addTest(unittest.makeSuite(ValidateDataTest))
    the_suite.addTest(unittest.makeSuite(ViewTest))
    the_suite.addTest(unittest.makeSuite(UmlInterpreterTest))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    cov = coverage.Coverage(omit='*test.py')
    cov.start()
    runner.run(test_suite)
    cov.stop()
    cov.save()

    cov.html_report()
