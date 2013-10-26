import xlrd

WORKBOOK = 'data/slownik_jst_2013.xls'

def WkPkGkToStr(wk, pk, gk):
    return unicode(wk).replace('.0', '') + unicode(pk).replace('.0', '') + unicode(gk).replace('.0', '')

def getGminy(slownik_path):
    book = xlrd.open_workbook(slownik_path, encoding_override='utf-8')
    data = {}
    sheet = book.sheets()[0]
    names = sheet.col(0)
    wks   = sheet.col(1)
    pks   = sheet.col(2)
    gks   = sheet.col(3)
    types = sheet.col(6)
    for i in range(len(sheet.col(0))):
        name = names[i]
        wk   = wks[i]
        pk   = pks[i]
        gk   = gks[i]
        type_ = types[i]
        
        try:
            data[WkPkGkToStr(wk.value, pk.value, gk.value)] = (name.value.lower(), name.value, type_.value)
        except:
            print 'FAULT:', name, wk, pk, gk
    
    return data

if __name__ == '__main__':
    print getGminy(WORKBOOK)
