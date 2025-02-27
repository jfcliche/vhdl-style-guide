

from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_020(Rule):
    '''
    This rule checks a label and the colon are on the same line.

    **Violation**

    .. code-block:: vhdl

       label
       :

    **Fix**

    .. code-block:: vhdl

       label :
    '''

    def __init__(self):
        Rule.__init__(self, lTokens)
        self.subphase = 3
