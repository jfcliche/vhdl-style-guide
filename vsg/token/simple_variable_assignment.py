
from vsg import parser


class target(parser.target):
    '''
    unique_id = simple_variable_assignment : target
    '''

    def __init__(self, sString):
        parser.target.__init__(self, sString)


class simple_name(parser.simple_name):
    '''
    unique_id = simple_variable_assignment : simple_name
    '''

    def __init__(self, sString):
        parser.simple_name.__init__(self, sString)


class assignment(parser.assignment):
    '''
    unique_id = simple_variable_assignment : assignment
    '''

    def __init__(self, sString):
        parser.assignment.__init__(self, sString)


class semicolon(parser.semicolon):
    '''
    unique_id = simple_variable_assignment : semicolon
    '''

    def __init__(self, sString=';'):
        parser.semicolon.__init__(self)


class aggregate_open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = simple_variable_assignment : aggregate_open_parenthesis
    '''

    def __init__(self, sString):
        parser.open_parenthesis.__init__(self)


class aggregate_comma(parser.comma):
    '''
    unique_id = simple_variable_assignment : aggregate_comma
    '''

    def __init__(self, sString):
        parser.comma.__init__(self)


class aggregate_close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = simple_variable_assignment : aggregate_close_parenthesis
    '''

    def __init__(self, sString):
        parser.close_parenthesis.__init__(self)
