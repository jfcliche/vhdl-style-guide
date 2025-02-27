
from vsg import token

from vsg.rules import check
from vsg.rules import fix
from vsg.rules import tokens_of_interest as toi
from vsg.rules import utils as rules_utils

from vsg.rule_group import structure

from vsg.vhdlFile import utils


class multiline_procedure_call_structure(structure.Rule):
    '''
    This rule checks the structure of multiline constraints.
    '''

    def __init__(self):
        structure.Rule.__init__(self)
        self.phase = 1
        self.lTokenPairs = None
        self.configuration_documentation_link = None

        self.first_open_paren = 'ignore'
        self.configuration.append('first_open_paren')
        self.last_close_paren = 'ignore'
        self.configuration.append('last_close_paren')
        self.association_list_comma = 'ignore'
        self.configuration.append('association_list_comma')
        self.association_element = 'ignore'
        self.configuration.append('association_element')
        self.ignore_single_line = 'no'
        self.configuration.append('ignore_single_line')

    def _get_tokens_of_interest(self, oFile):
        return toi.get_tokens_bounded_by(self.lTokenPairs, oFile)

    def _analyze(self, lToi):
        for oToi in lToi:
            if rules_utils.is_single_line(oToi) and utils.convert_yes_no_option_to_boolean(self.ignore_single_line):
                continue

            _check_first_open_paren(self, oToi)
            _check_last_close_paren(self, oToi)
            _check_association_list_comma(self, oToi)
            _check_association_element(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        fix.fix_violation(oViolation)


def _check_first_open_paren(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.first_open_paren, token.procedure_call.open_parenthesis)


def _check_last_close_paren(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.last_close_paren, token.procedure_call.close_parenthesis)


def _check_association_list_comma(self, oToi):

    check.add_new_line_and_remove_new_line(self, oToi, self.association_list_comma, token.association_list.comma)


def _check_association_element(self, oToi):

    check.add_new_line_and_remove_new_line_after(self, oToi, self.association_element, token.procedure_call.open_parenthesis)
    check.add_new_line_and_remove_new_line_after(self, oToi, self.association_element, token.association_list.comma)
