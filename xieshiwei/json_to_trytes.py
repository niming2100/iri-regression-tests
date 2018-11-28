#!/usr/bin/env python3
import math
import json
import operator
from functools import reduce

class binConversionForTrits(object):
    def __init__(self):
        self.RADIX = 3
        self.MAX_TRIT_VALUE = (self.RADIX - 1) / 2
        self.MIN_TRIT_VALUE = -self.MAX_TRIT_VALUE
        self.NUMBER_OF_TRITS_IN_A_BYTE = 5
        self.NUMBER_OF_TRITS_IN_A_TRYTE = 3
        self.BYTE_TO_TRITS_MAPPINGS = [[0 for col in range(0)] for row in range(243)]
        self.TRYTE_TO_TRITS_MAPPINGS = [[0 for col in range(0)] for row in range(27)]
        self.TRYTE_ALPHABET = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.initialization()

    def initialization(self):
        trits = [0] * self.NUMBER_OF_TRITS_IN_A_BYTE
        trits2 = [0] * self.NUMBER_OF_TRITS_IN_A_TRYTE
        for i in range(243):
            for j in range(self.NUMBER_OF_TRITS_IN_A_BYTE):
                trits[j] = trits[j] + 1
                if trits[j] > 1:
                    trits[j] = -1
                else:
                    break
            self.BYTE_TO_TRITS_MAPPINGS[i] = trits[:]
        for i in range(27):
            for j in range(self.NUMBER_OF_TRITS_IN_A_TRYTE):
                trits2[j] = trits2[j] + 1
                if trits2[j] > 1:
                    trits2[j] = -1
                else:
                    break
            self.TRYTE_TO_TRITS_MAPPINGS[i] = trits2[:]

    def getDict(self, json_string):
        # Convert json to a dictionary table
        json_dict = dict()
        json_dict = json.loads(json_string)
        return json_dict

    def fromBinDicToTriDict(self, json_dict):
        new_dict = dict()
        for key in json_dict:
            letter_string = json_dict.get(key)
            trits=list()
            trits_list=list()
            for letter in letter_string:
                index = ord(letter)
                trits = self.BYTE_TO_TRITS_MAPPINGS[index]
                trits_list.append(trits)
            new_dict[key] = trits_list
            return new_dict

        def fromTriDictTotrytes(self, new_dict):
            one_dimensional_list = list()
            two_dimensional_list = list()
            trytes = ""
            for trits_list in new_dict.values():
                one_dimensional_list = reduce(operator.add, trits_list)
                remainder = len(one_dimensional_list) - 3 * int(len(one_dimensional_list) / 3)
                if remainder != 0:
                    if remainder == 1:
                        one_dimensional_list.append(0, 0)
                    if remainder == 2:
                        one_dimensional_list.append(0)
                    # Convert a two-dimensional list to a one-dimensional
                    for i in range(0, len(one_dimensional_list), 3):
                        two_dimensional_list.append(one_dimensional_list[i:i + 3])
                    for values in two_dimensional_list:
                        index_number = self.TRYTE_TO_TRITS_MAPPINGS.index(values)
                        tryte = self.TRYTE_ALPHABET[index_number]
                        trytes += tryte
                else:
                    for i in range(0, len(one_dimensional_list), 3):
                        two_dimensional_list.append(one_dimensional_list[i:i + 3])
                    for values in two_dimensional_list:
                        data = self.TRYTE_TO_TRITS_MAPPINGS.index(values)
                        tryte = self.TRYTE_ALPHABET[data]
                        trytes += tryte
            return trytes

        def helper(self, json_string):
            json_dict = self.getDict(json_string)
            new_dict = self.fromBinDicToTriDict(json_dict)
            return self.fromTriDictTotrytes(new_dict)

        if __name__ == "__main__":
            obj = binConversionForTrits()
            print(obj.helper('{"addr":"i02jsdsil"}'))

