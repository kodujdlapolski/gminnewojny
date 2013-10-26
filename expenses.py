#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbf
import gminy
import par_mapper
import cities

def generate_expenditures():
    table = dbf.Table('data/Rb28s.dbf')
    table.open()

    par_data = par_mapper.get_par('data/par_input.txt')
    gminy_data = gminy.getGminy(gminy.WORKBOOK)
    
    result = {}

    for record in table:
        wk_pk_gk = gminy.WkPkGkToStr(record['wk'], record['pk'], record['gk'])
        
        try:
            gminy_record = gminy_data[wk_pk_gk]
            par_record = par_data[int(record['par'])]
        except KeyError:
            continue

        planned = record['r1']
        executed = record['r4']
        
        gmina_type = gminy_record[2]
        gmina_name = gminy_record[1]
        gmina_key = gminy_record[0]
        
        if gmina_key not in result:
            result[gmina_key] = {}
        
        result[gmina_key][par_record[0:-1]] = (planned, executed)
        result[gmina_key]['__name'] = gmina_name

    return result

DATA = generate_expenditures()

def get_data_for_gmina(gmina, planned=False):
    gmina = gmina.lower()
    if not gmina in DATA:
        return
    gmina_info = DATA[gmina]
    result = {}
    for attr in gmina_info:
        if planned:
            result[attr] = gmina_info[attr][1]
        else:
            result[attr] = gmina_info[attr][0]
    
    return result

def get_similar_gmina(gmina):
    return cities.cities.get_similar_city(gmina)

print get_data_for_gmina('GRODZISK MAZOWIECKI')
print get_data_for_gmina('JAWORZNO')
