
from vsg.rules.port import port_rule


class rule_011(port_rule):
    '''
    Port rule 011 checks port names have I_, O_ or IO_ prefixes.

         The valid options for self.port_direction are:
            None (default)   No checks are made.
            Prefix           Checks for I_, O_, and IO_ in front of port names.
            Suffix           Checks for _I, _O, and _IO at the end of port names.
    
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add proper prefix or suffix indicating port direction.'
        self.port_direction = None
        self.phase = 7
        self.fixable = False  # This requires the user to fix as this could cover multiple files.

    def analyze(self, oFile):
        if not self.port_direction:
            self.violations = []
        if self.port_direction == 'Prefix':
            self.solution = 'Add proper prefix indicating port direction.'
        if self.port_direction == 'Suffix':
            self.solution = 'Add proper suffix indicating port direction.'

        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and oLine.insideEntity:
                lLine = oLine.lineLower.split()
                if self.port_direction == 'Prefix':
                    if not(lLine[0].startswith('i_') or lLine[0].startswith('o_') or lLine[0].startswith('io_')):
                        self.add_violation(iLineNumber)
                if self.port_direction == 'Suffix':
                    if not(lLine[0].endswith('_i') or lLine[0].endswith('_o') or lLine[0].endswith('_io') or \
                           lLine[0].endswith('_i,') or lLine[0].endswith('_o,') or lLine[0].endswith('_io,')):
                        self.add_violation(iLineNumber)
