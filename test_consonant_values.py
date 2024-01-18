import unittest


def highest_value_consonant_substring(s):
    def sub_string(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)
    
    #remove vowels
    consonant_str = ''.join(char for char in s if char not in 'aeiou')

    #split into substring consonant
    consonant_substrings = consonant_str.split('a') 

    #calculate the consonant substring and maximum
    return max(sub_string(sub) for sub in consonant_substrings)

class TestHighestValueConsonantSubstring(unittest.TestCase):
    def test_highest_value(self):
        self.assertEqual(highest_value_consonant_substring("zodiacs"), 26)
        self.assertEqual(highest_value_consonant_substring("hello"), 24)
        self.assertEqual(highest_value_consonant_substring("programming"), 34)
        self.assertEqual(highest_value_consonant_substring("python"), 69)

    def test_empty_string(self):
        self.assertEqual(highest_value_consonant_substring(""), 0)

    def test_single_character(self):
        self.assertEqual(highest_value_consonant_substring("a"), 0)
        self.assertEqual(highest_value_consonant_substring("z"), 26)
        self.assertEqual(highest_value_consonant_substring("b"), 2)


if __name__ == '__main__':
    unittest.main()
