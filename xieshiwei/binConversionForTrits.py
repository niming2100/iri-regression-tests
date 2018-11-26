#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import json

class binConversionForTrits(object):
    def __init__(self):
        self.BYTE_TO_TRITS_MAPPINGS = [[0 for col in range(0)] for row in range(243)]
        self.TRYTE_TO_TRITS_MAPPINGS = [[0 for col in range(0)] for row in range(27)]
        self.TRYTE_ALPHABET = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.initialization()

    def initialization(self):
        RADIX = 3
        MAX_TRIT_VALUE = (RADIX - 1) / 2
        MIN_TRIT_VALUE = -MAX_TRIT_VALUE
        NUMBER_OF_TRITS_IN_A_BYTE = 5
        NUMBER_OF_TRITS_IN_A_TRYTE = 3
        trits = [0] * NUMBER_OF_TRITS_IN_A_BYTE
        trits2 = [0] * NUMBER_OF_TRITS_IN_A_TRYTE
        for i in range(243):
            for j in range(NUMBER_OF_TRITS_IN_A_BYTE):
                trits[j] = trits[j] + 1
                if trits[j] > 1:
                    trits[j] = -1
                else:
                    break
            self.BYTE_TO_TRITS_MAPPINGS[i] = trits[:]
        for i in range(27):
            for j in range(NUMBER_OF_TRITS_IN_A_TRYTE):
                trits2[j] = trits2[j] + 1
                if trits2[j] > 1:
                    trits2[j] = -1
                else:
                    break
            self.TRYTE_TO_TRITS_MAPPINGS[i] = trits2[:]

    def getDict(self, json_string):
        # 将json转换为字典表
        json_dict = dict()
        json_dict = json.loads(json_string)
        return json_dict

    def fromBinDicToTriDict(self, json_dict):
        new_dict = dict()
        # trits = list()
        triss = list()
        for key in json_dict:
            stri = json_dict.get(key)
            for c in stri:
                trits=list()
                # 将字符串转换为二进制
                tmp = bin(ord(c)).replace("0b", '')
                # 转为十进制
                t = int(tmp, 2)
                # 十进制转为三进制
                if t < 0:
                    while t != 0:
                        tmp1 = math.floor(round(t / 3, 1) + 0.5)
                        t = tmp1
                        trit = t - (tmp1 * 3)
                        trits.append(trit)
                    # print(trits)
                else:
                    while (t != 0):
                        tmp1 = math.floor(round(t / 3, 1) + 0.5)  # 圆整
                        trit = t - (tmp1 * 3)  # 取余
                        trits.append(trit)
                        t = tmp1
                    # print(trits)
                        triss.append(trits)
                print(triss)
            new_dict[key] = trits
        return new_dict

    # def fromTriDictToTrytes(self, new_dict):
    #     for trits in new_dict:
    #         for i in range trits:
    #             tryteNumber = self.TRYTE_TO_TRITS_MAPPINGS.index(trits)
    #             tryte = self.TRYTE_ALPHABET[tryteNumber]
    #         trytes = str.join(tryte)

    def helper(self, json_string):
        json_dict = self.getDict(json_string)
        new_dict = self.fromBinDicToTriDict(json_dict)
        # return self.fromTriDictToTrytes(new_dict)

if __name__ == "__main__":
    obj = binConversionForTrits()
    print(obj.helper('{"addr":"dj"}'))




