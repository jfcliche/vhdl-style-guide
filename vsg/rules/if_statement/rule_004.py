
from vsg import parser
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([parser.close_parenthesis, token.if_statement.then_keyword])


class rule_004(Rule):
    '''
    This rule checks for a single space between the ) and the **then** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      if (a = '1')then

      if (a = '1')    then

    **Fix**

    .. code-block:: vhdl

      if (a = '1') then

      if (a = '1') then
    '''
    def __init__(self):
        Rule.__init__(self, lTokens)
