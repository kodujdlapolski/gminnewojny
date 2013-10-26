import csv
import re
import bisect

def _depolonize(text):
    is_unicode = False
    if type(text) == unicode:
        is_unicode = True
        text = text.encode('utf-8')

    polish_letters_map = {"\xc4\x84": "A", "\xc4\x86": "C",
                          "\xc4\x98": "E", "\xc5\x81": "L", "\xc5\x83": "N", "\xc3\x93": "O",
                          "\xc5\x9a": "S", "\xc5\xb9": "Z", "\xc5\xbb": "Z", "\xc4\x85": "a",
                          "\xc4\x87": "c", "\xc4\x99": "e", "\xc5\x82": "l", "\xc5\x84": "n",
                          "\xc3\xB3": "o", "\xc5\x9b": "s", "\xc5\xba": "z", "\xc5\xbc": "z"}
    for from_what, to_what in polish_letters_map.iteritems():
        text = text.replace(from_what, to_what)

    return unicode(text, 'utf-8') if is_unicode else text

def _normalize(text):
    return _depolonize(text).lower()

class Cities:

    def __init__(self):
        self._city_to_population = {}
        self._population_to_city = {}
        self._populations = []

        no_digits_re = re.compile('[^\d]')

        with open('data/cities.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                city = unicode(row[0], 'utf-8')
                population = int(no_digits_re.sub("", row[4]))

                self._city_to_population[_normalize(city)] = population
                self._populations.append(population)
                if population in self._population_to_city:
                    self._population_to_city[population].append(city)
                else:
                    self._population_to_city[population] = [city]

            self._populations.sort()

    def get_population_for_city(self, city):
        return self._city_to_population[_normalize(city)]

    def get_some_city_for_population(self, population):
        return self._population_to_city[population][0]

    def get_similar_city(self, city):
        population = self.get_population_for_city(city)

        if len(self._population_to_city[population]) > 1:
            # We could easily do without this loop, but hopefully there won't be too many
            # cities with the same population 
            for other_city in self._population_to_city[population]:
                if other_city != city:
                    # Other city with exactly the same population exists 
                    return other_city
        else:
            index = bisect.bisect_left(self._populations, population)
            if index > 0:
                return self.get_some_city_for_population(self._populations[index - 1])
            else:
                return self.get_some_city_for_population(self._populations[index + 1])


cities = Cities()

