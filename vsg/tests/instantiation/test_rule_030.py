
import unittest

from vsg.rules import instantiation


class test_rule(unittest.TestCase):

    def test_rule_030(self):
        oRule = instantiation.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'instantiation')
        self.assertEqual(oRule.identifier, '030')
        self.assertTrue(oRule.deprecated)
