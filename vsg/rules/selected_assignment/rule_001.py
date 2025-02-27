
from vsg import token

from vsg.rules import remove_carriage_return_after_token as Rule

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.with_keyword)
lTokens.append(token.selected_force_assignment.with_keyword)
lTokens.append(token.selected_variable_assignment.with_keyword)
lTokens.append(token.selected_waveform_assignment.with_keyword)


class rule_001(Rule):
    '''
    This rule checks the **with** keyword is on the same line as the expression.

    **Violation**

    .. code-block:: vhdl

       with
         mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, lTokens, bInsertSpace=True)
        self.solution = 'Removed carraige returns after with keyword'
