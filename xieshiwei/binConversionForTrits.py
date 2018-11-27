#!/usr/bin/env python3
import math
import json

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
                # Find the corresponding index in the ascll table
                index = ord(letter)
                # Returns the corresponding balanced ternary
                trits = self.BYTE_TO_TRITS_MAPPINGS[index]
                trits_list.append(trits)
            new_dict[key]=trits_list
        return new_dict

    def helper(self, json_string):
        json_dict = self.getDict(json_string)
        new_dict = self.fromBinDicToTriDict(json_dict)
        return new_dict

if __name__ == "__main__":
    obj = binConversionForTrits()
    print(obj.helper('{"addr":"lld0j"}'))




