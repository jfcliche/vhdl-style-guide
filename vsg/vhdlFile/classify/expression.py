
from vsg import parser

from vsg.vhdlFile import utils

from vsg.token import direction


def classify(iToken, lObjects):
    '''
    expression ::=
        condition_operator primary
      | logical_expression
    '''
    return utils.assign_token(lObjects, iToken, parser.todo)


def classify_until(lUntils, iToken, lObjects, oType=parser.todo):
    '''
    expression ::=
        condition_operator primary
      | logical_expression
    '''
    iCurrent = iToken
    iStop = len(lObjects) - 1
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    iPrevious = 0
    while iCurrent < iStop:
        if iCurrent == iPrevious:
            break
        iPrevious = iCurrent
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        if utils.token_is_open_parenthesis(iCurrent, lObjects):
           iOpenParenthesis += 1
        if utils.token_is_close_parenthesis(iCurrent, lObjects):
           iCloseParenthesis += 1

        if iOpenParenthesis < iCloseParenthesis:
            break
        elif lObjects[iCurrent].get_value().lower() in lUntils:
            if utils.token_is_close_parenthesis(iCurrent, lObjects):
                if iOpenParenthesis == iCloseParenthesis:
                    utils.assign_token(lObjects, iCurrent, parser.close_parenthesis)
                    iCurrent += 1
                    continue
                else:
                    break
            elif utils.token_is_comma(iCurrent, lObjects):
                if iOpenParenthesis == iCloseParenthesis:
                    break
                else:
                    utils.assign_token(lObjects, iCurrent, parser.comma)
                    iCurrent += 1
            else:
                break
        else:
            utils.assign_special_tokens(lObjects, iCurrent, oType)
            iCurrent += 1
    return iCurrent
