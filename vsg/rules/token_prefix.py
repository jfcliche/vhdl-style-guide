
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import naming


class token_prefix(naming.Rule):
    '''
    Checks the prefix for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, lTokens):
        naming.Rule.__init__(self)
        self.lTokens = lTokens
        self.prefixes = None
        self.configuration.append('prefixes')
        self.fixable = False
        self.disable = True
        self.exceptions = []
        self.configuration.append('exceptions')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        lPrefixLower = []
        for sPrefix in self.prefixes:
            lPrefixLower.append(sPrefix.lower())

        lExceptionsLower = []
        for sException in self.exceptions:
            lExceptionsLower.append(sException.lower())

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_value().lower()
            if sToken in lExceptionsLower:
                continue

            bValid = False
            for sPrefix in lPrefixLower:
                if sToken.startswith(sPrefix.lower()):
                    bValid = True
            if not bValid:
                sSolution = 'Prefix ' + lTokens[0].get_value() + ' with one of the following: ' + ', '.join(self.prefixes)
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if oViolation.get_action() == 'remove_whitespace':
            oViolation.set_tokens([lTokens[1]])
        elif oViolation.get_action() == 'adjust_whitespace':
            lTokens[0].set_value(lTokens[1].get_indent() * self.indent_size * ' ')
            oViolation.set_tokens(lTokens)
        elif oViolation.get_action() == 'add_whitespace':
            rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent() * self.indent_size)
            oViolation.set_tokens(lTokens)
