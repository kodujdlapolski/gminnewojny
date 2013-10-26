#!/usr/bin/python

import dbf

import gminy
import par_mapper

def generate_expenditures():
    table = dbf.Table('data/Rb28s.dbf')
    table.open()

    par_data = par_mapper.get_par('par_input.txt')
    gminy_data = gminy.getGminy(gminy.WORKBOOK)
    
    result = []

    for record in table[1:100]:
        wk_pk_gk = gminy.WkPkGkToStr(record['wk'], record['pk'], record['gk'])
        
        try:
            gminy_record = gminy_data[wk_pk_gk]
            par_record = par_data[int(record['par'])]
        except KeyError:
            continue

        result.append((gminy_record, par_record, record))

    return result

#generate_expenditures()
