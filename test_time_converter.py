import unittest

def time_conversion(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
       
    else :
        if hour != 12:
            hour += 12
       
    return f"{hour}{minute}"


class TestTimeConversion(unittest.TestCase):
    def test_valid_time_conversion(self):
        # Test valid inputs and expected output
        self.assertEqual(time_conversion(11, 30, "am"), "1130")
        self.assertEqual(time_conversion(12, 0, "pm"), "1200")
        self.assertEqual(time_conversion(1, 45, "pm"), "1345")

if __name__ == "__main__":
    unittest.main()