import unittest

ar_to_rome = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I", 0: ""}

def arabske_na_rimske(ar):
    if ar > 0 and ar < 4: 
        return ar * "I"


class TestArabskeNaRimske(unittest.TestCase):
    def test_one(self):
        self.assertEqual(arabske_na_rimske(1), "I")

    def test_five(self):
        self.assertEqual(arabske_na_rimske(5), "V")

    def test_ten(self):
        self.assertEqual(arabske_na_rimske(10), "X")

    def test_three(self):
        self.assertEqual(arabske_na_rimske(3), "III")

    def test_six(self):
        self.assertEqual(arabske_na_rimske(6), "VI")

    def test_assert_not_one_if_not_one(self):
        self.assertNotEqual(arabske_na_rimske(2), "I")
  
   

    # ze je to z "rimska abeceda"
    # ze dojde k prevodu
    # ze oboje pracuje v decimalni soustave
