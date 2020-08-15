
from vsg.vhdlFile.classify import concurrent_procedure_call_statement
from vsg.vhdlFile.classify import process_statement
from vsg.vhdlFile.classify import concurrent_signal_assignment_statement
from vsg.vhdlFile.classify import concurrent_assertion_statement


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_statement ::= [§ 11.1]
        block_statement
      | process_statement
      | concurrent_procedure_call_statement
      | concurrent_assertion_statement
      | concurrent_signal_assignment_statement
      | component_instantiation_statement
      | generate_statement
      | *PSL*_PSL_Directive
    '''

    if concurrent_assertion_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if process_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if not dVars['concurrent_procedure_call_statement']:
        if concurrent_signal_assignment_statement.tokenize(oObject, iObject, lObjects, dVars):
            return True

    if concurrent_procedure_call_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    concurrent_signal_assignment_statement.clear_flags(dVars)
    concurrent_assertion_statement.clear_flags(dVars)
    concurrent_procedure_call_statement.clear_flags(dVars)
    process_statement.clear_flags(dVars)
