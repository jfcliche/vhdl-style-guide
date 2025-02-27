
from vsg.rule_group import blank_line
from vsg import parser
from vsg import violation


class blank_line_above_line_starting_with_token(blank_line.Rule):
    '''
    Checks for a blank line above a line starting with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line above should appear
    '''

    def __init__(self, lTokens, lAllowTokens=None):
        blank_line.Rule.__init__(self)
        self.lTokens = lTokens
        if lAllowTokens is None:
            self.lAllowTokens = []
        else:
            self.lAllowTokens = lAllowTokens
        self.style = 'require_blank_line'
        self.configuration.append('style')
        self.configuration_documentation_link = 'configuring_blank_lines_link'

    def _get_tokens_of_interest(self, oFile):
        if self.style == 'require_blank_line':
            return oFile.get_line_above_line_starting_with_token(self.lTokens, bIncludeComments=False)
        elif self.style == 'no_blank_line':
            return oFile.get_blank_lines_above_line_starting_with_token(self.lTokens)

    def _set_allow_tokens(self):
        return

    def _analyze(self, lToi):
        self._set_allow_tokens()
        if self.style == 'require_blank_line':
            _analyze_require_blank_line(self, lToi, self.lAllowTokens)
        elif self.style == 'no_blank_line':
            _analyze_no_blank_line(self, lToi, self.lAllowTokens)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['action'] == 'Insert':
            lTokens.append(parser.carriage_return())
            lTokens.append(parser.blank_line())
            oViolation.set_tokens(lTokens)
        elif dAction['action'] == 'Remove':
            oViolation.set_tokens([])


def _analyze_require_blank_line(self, lToi, lAllowTokens):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if _is_allowed_token(lAllowTokens, lTokens):
                continue
            if len(lTokens) == 1:
                if isinstance(lTokens[0], parser.blank_line):
                    continue
            sSolution = 'Insert blank line above'
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            dAction = {}
            dAction['action'] = 'Insert'
            oViolation.set_action(dAction)
            self.add_violation(oViolation)


def _analyze_no_blank_line(self, lToi, lAllowTokens):
        for oToi in lToi:
            sSolution = 'Remove blank lines'
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            dAction = {}
            dAction['action'] = 'Remove'
            oViolation.set_action(dAction)
            self.add_violation(oViolation)


def _is_allowed_token(lAllowTokens, lTokens):
    bSkip = False
    for oAllowToken in lAllowTokens:
        for oToken in lTokens:
            if isinstance(oToken, oAllowToken):
                bSkip = True
                break
        if bSkip:
           break
    if bSkip:
        return True
    return False
