import unittest
from binConversionForTrits import binConversionForTrits

class TestbinForTrits(unittest.TestCase):

    def test_getDict(self):
        d=binConversionForTrits()
        json_dict =d.getDict('{"addr":"is2l"}')
        self.assertEqual(json_dict,{u'addr': u'is2l'})

    def test_fromBinDicToTriDict(self):
        d=binConversionForTrits()
        new_dict=d.fromBinDicToTriDict({u'addr': u'is2l'})
        self.assertEqual(new_dict,{u'addr': [[1, -1, 0, 1, 1], [-1, 0, 1, 1, 1], [0, -1, 0, -1, 1], [1, 0, 0, 1, 1]]})

if __name__=="__main__":
    unittest.main()
