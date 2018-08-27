# -*- coding: utf -*-
'''
Created on 13 april 2013

@author: vl
'''


class Analyser(object):
    '''
    classdocs
    '''

    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.__filepath = filepath
        self.__data = []

    def load_file(self):
        '''
        Load data from log file
        '''
        log_file = open(self.__filepath, 'r')
        data = log_file.readlines()
        log_file.close()
        for line in data:
            self.append_record(line.split())
        return self

    def append_record(self, record):
        '''
        Append record
        '''
        self.__data.append(record)
        return self

    def get_data(self):
        '''
        Get data
        '''
        return self.__data

    def unique_visitors(self):
        '''
        Return array of unique visitors (ip)
        '''
        # TODO: Написати код який повертає унікальних відвідувачів. Унікальність визначається за IP адресою
        # Всі дані про відвідувачів доступні в self.__data
        visitors = []
        for user in self.__data:
            if user[0] not in visitors:
                visitors.append(user[0])
        return visitors

    def all_visitors(self):
        '''
        Return array of visitors and count of visits
        '''
        # TODO: Вивести кількість всіх відвідувачів та кількість відвідувань

        visitors_count = str(len(self.unique_visitors()))
        visits_count = str(len(self.__data))
        visitors = (visitors_count, visits_count)
        return visitors

    def visitors_by_resources(self):
        '''
        Return dictionary of visitors and resources count
        '''
        visitors = dict()
        for record in self.__data:
            if visitors.has_key(record[0]):
                visitors[record[0]] += 1
            else:
                visitors[record[0]] = 1

        return visitors

    def resources_by_countries(self):
        '''
        Return dictionary of resources and coutries from which it's was loaded
        '''
        # TODO: Вивести словник ресурсів і країни з яких вони відвідувались

        resources = {}

        for row in self.__data:
            if resources.has_key(row[2]):
                resources[row[2]] += 1
            resources.setdefault(row[2], 1)
        """
            uncomment the code below to get dictionary of resources and countries
        """
            # if row[1] in resources.keys():
            #     if row[2] not in resources.get(row[1], []):
            #         resources[row[1]].append(row[2])
            # else:
            #         resources.setdefault(row[1], []).append(row[2])

        return resources
