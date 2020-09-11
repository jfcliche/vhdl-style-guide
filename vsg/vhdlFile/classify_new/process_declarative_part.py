

from vsg.vhdlFile.classify_new import process_declarative_item

'''
    process_declarative_part ::=
        { process_declarative_item }
'''


def detect(iToken, lObjects):
    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = process_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
