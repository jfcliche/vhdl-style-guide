
from vsg.rules.generic import generic_rule

import re


class rule_005(generic_rule):
    '''Generic rule 005 checks for a single space after the colon in a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
