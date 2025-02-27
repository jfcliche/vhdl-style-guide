
from vsg import rule


class Rule(rule.Rule):
    '''
    Class for assigning rules to the naming group.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    '''

    def __init__(self):
        rule.Rule.__init__(self)
        self.phase = 7
        self.groups.append('naming')
        self.configuration_documentation_link = 'configuring_prefix_and_suffix_rules_link'
