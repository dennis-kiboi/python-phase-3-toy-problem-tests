import unittest


def exactly_two_positive(a, b, c):
    count = 0
    if a > 0 :
        count += 1
    if b > 0 :
        count += 1
    if c > 0 :
        count += 1
    
    if count ==2:
        return True
    else:
        return False    
    # return count    


class TestExactlyTwoPositive(unittest.TestCase):
    def test_two_positive(self):
        self.assertTrue(exactly_two_positive(3, -1, 5))
        self.assertTrue(exactly_two_positive(-2, 4, 1))
        self.assertTrue(exactly_two_positive(1, 2, -3))

    def test_not_two_positive(self):
        self.assertFalse(exactly_two_positive(-2, -4, 0))
        self.assertFalse(exactly_two_positive(0, 0, -1))
        self.assertFalse(exactly_two_positive(-1, -2, -3))
        self.assertFalse(exactly_two_positive(1, 2, 3))


if __name__ == '__main__':
    unittest.main()
