
from vsg.rules import multiline_procedure_call_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.procedure_call.procedure_name, token.concurrent_procedure_call_statement.semicolon])
lTokenPairs.append([token.procedure_call.procedure_name, token.procedure_call_statement.semicolon])


class rule_003(Rule):
    '''
    This rule checks the structure of procedure calls.

    |configuring_multiline_procedure_call_statement_rules_link|

    **Violation**

    .. code-block:: vhdl

       connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

    **Fix**

    .. code-block:: vhdl

       connect_ports(
         port_1 => data,
         port_2 => enable,
         port_3 => overflow,
         port_4 => underflow
       );

    .. _procedure_call_whitespacing_rules:
    '''

    def __init__(self):
        Rule.__init__(self)
        self.lTokenPairs = lTokenPairs
