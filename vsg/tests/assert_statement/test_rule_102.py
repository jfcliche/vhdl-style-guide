
import os
import unittest

from vsg.rules import assert_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_102_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_102_test_input.fixed.vhd'), lExpected)


class test_assert_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_102(self):
        oRule = assert_statement.rule_102()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'assert')
        self.assertEqual(oRule.identifier, '102')

        lExpected = [6, 14, 20, 26]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_102(self):
        oRule = assert_statement.rule_102()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
