#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbf
import gminy
import par_mapper
import cities
import os
import cPickle

def generate_expenditures():
    table = dbf.Table('data/Rb28s.dbf')
    table.open()

    par_data = par_mapper.get_par('data/par_input.txt')
    rozdzial_data = par_mapper.get_par('data/rozdzial_input.txt')
    gminy_data = gminy.getGminy(gminy.WORKBOOK)
    
    result = {}

    for record in table:
        wk_pk_gk = gminy.WkPkGkToStr(record['wk'], record['pk'], record['gk'])
        
        try:
            gminy_record = gminy_data[wk_pk_gk]
            par_record = par_data[int(record['par'])]
            rozdzial   = rozdzial_data[int(record['rozdzial'])]
        except KeyError:
            continue

        planned = record['r1']
        executed = record['r4']
        
        gmina_type = gminy_record[2]
        gmina_name = gminy_record[1]
        gmina_key = gminy_record[0]
        
        if gmina_key not in result:
            result[gmina_key] = {}
        
        expense_data = par_record
        if expense_data not in result[gmina_key]:
            result[gmina_key][expense_data] = [0.0, 0.0]
            
        result[gmina_key][expense_data][0] += planned
        result[gmina_key][expense_data][1] += executed
        
        result[gmina_key]['__name'] = gmina_name

    return result

CACHE_FILE_NAME = 'data.cache'
if os.path.isfile(CACHE_FILE_NAME):
    print 'Loading cached data from', CACHE_FILE_NAME
    with open(CACHE_FILE_NAME, 'r') as f:
        DATA = cPickle.load(f)
else:
    print 'Cache file doesn\'t exist, data will be generated...'
    DATA = generate_expenditures()
    print 'Saving generated data to a cache file...'
    with open(CACHE_FILE_NAME, 'w') as f:
        cPickle.dump(DATA, f)
    print 'Done with data.'


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


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_data_for_gmina(u'Kraków'))
