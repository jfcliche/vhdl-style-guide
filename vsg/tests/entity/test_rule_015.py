
import os
import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_015_test_input.vhd'))

lExpected_add = []
lExpected_add.append('')
utils.read_file(os.path.join(sTestDir, 'rule_015_test_input.fixed_add.vhd'), lExpected_add)

lExpected_remove = []
lExpected_remove.append('')
utils.read_file(os.path.join(sTestDir, 'rule_015_test_input.fixed_remove.vhd'), lExpected_remove)


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_015_add(self):
        oRule = entity.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '015')
        self.assertEqual(oRule.groups, ['structure', 'structure::optional'])

        lExpected = [8, 12, 16, 20, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_015_add(self):
        oRule = entity.rule_015()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_015_remove(self):
        oRule = entity.rule_015()
        oRule.action = 'remove'

        lExpected = [4]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_015_remove(self):
        oRule = entity.rule_015()
        oRule.action = 'remove'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
