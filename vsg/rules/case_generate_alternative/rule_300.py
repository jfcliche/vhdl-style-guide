
from vsg import deprecated_rule


class rule_300(deprecated_rule.Rule):
    '''
    The function of this rule has been superseded with comment indent updates and is handled by rule comment_010.
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self)
        self.message.append('The function of rule ' + self.unique_id + ' is covered by rule comment_010.')
