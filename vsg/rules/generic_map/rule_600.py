
from vsg.rules import token_suffix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.association_element.formal_part)

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis


class rule_600(token_suffix_between_tokens):
    '''
    This rule checks for valid suffixes on generic identifiers in generic maps
    The default generic suffix is *\_g*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic map
       (
         WIDTH => 32,
         DEPTH => 512
       )

    **Fix**

    .. code-block:: vhdl

       generic map
       (
         WIDTH_G => 32,
         DEPTH_G => 512
       )
    '''

    def __init__(self):
        token_suffix_between_tokens.__init__(self, lTokens, lStart, lEnd)
        self.suffixes = ['_g']
