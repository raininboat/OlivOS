# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/L10NAPI.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2023, OlivOS-Team
@Desc      :   None
'''

import copy

import OlivOS

def getText(key:str, spec:list):
    return getTextByL10N(key, spec, OlivOS.L10NDataAPI.flagL10NSelection)

def getTextByL10N(key:str, spec:list, L10N:str):
    res = 'N/A'
    flagL10N = OlivOS.L10NDataAPI.flagL10NSelectionDefault
    flagL10NDefault = OlivOS.L10NDataAPI.flagL10NSelectionDefault
    if L10N in OlivOS.L10NDataAPI.dictL10NSTR:
        flagL10N = L10N
    if key in OlivOS.L10NDataAPI.dictL10NSTR[flagL10N]:
        res = formatSTR(OlivOS.L10NDataAPI.dictL10NSTR[flagL10N][key], spec)
    elif key in OlivOS.L10NDataAPI.dictL10NSTR[flagL10NDefault]:
        res = formatSTR(OlivOS.L10NDataAPI.dictL10NSTR[flagL10NDefault][key], spec)
    return res

def formatSTR(value:str, spec:list):
    res = value
    specRes = copy.deepcopy(spec)
    try:
        for i in range(OlivOS.L10NDataAPI.formatOffsetLimit):
            try:
                res = res.format(*specRes)
                break
            except:
                specResLen = len(specRes)
                specRes.append('{%d}' % specResLen)
    except:
        res = value
    return res
