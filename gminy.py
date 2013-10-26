import xlrd

workbook = 'slownik_jst_2013.xls'

def getGminy():
    book = xlrd.open_workbook(workbook, encoding_override='utf-8')
    data = {}
    sheet = book.sheets()[0]
    names = sheet.col(0)
    wks   = sheet.col(1)
    pks   = sheet.col(2)
    gks   = sheet.col(3)
    for i in range(len(sheet.col(0))):
        name = names[i]
        wk   = wks[i]
        pk   = pks[i]
        gk   = gks[i]
        try:
            data[unicode(wk.value).replace('.0', '') + unicode(pk.value).replace('.0', '') + unicode(gk.value).replace('.0', '')] = (name.value, )
        except:
            print 'FAULT:', name, wk, pk, gk
    
    return data

if __name__ == '__main__':
    print getGminy()