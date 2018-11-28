import unittest
from json_to_trytes import json_to_trytes

class test_json_to_trytes(unittest.TestCase):

    def test_get_dict(self):
        d=json_to_trytes()
        json_dict =d.get_dict('{"addr":"is2l"}')
        self.assertEqual(json_dict,{u'addr': u'is2l'})

    def test_bindict_to_tridict(self):
        d=json_to_trytes()
        new_dict=d.bindict_to_tridict({u'addr': u'is2l'})
        self.assertEqual(new_dict,{u'addr': [[1, -1, 0, 1, 1], [-1, 0, 1, 1, 1], [0, -1, 0, -1, 1], [1, 0, 0, 1, 1]]})

    def test_tridict_to_trytes(self):
        d=json_to_trytes()
        trytes=d.tridict_to_trytes({u'addr': [[1, -1, 0, 1, 1], [-1, 0, 1, 1, 1], [0, -1, 0, -1, 1], [1, 0, 0, 1, 1]]})
        self.assertEqual(trytes,"XUKRE9C")

if __name__=="__main__":
    unittest.main()
