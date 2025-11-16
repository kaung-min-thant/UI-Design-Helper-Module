import unittest
import design_tools

class TestUIDesignChecks(unittest.TestCase):

    # 1. Test for Text Length Logic (is_text_fit)
    def test_is_text_fit(self):
        """
        Verifies that text validation for UI elements works correctly.
        """
        # Scenario A: Text is very short.
        self.assertTrue(design_tools.is_text_fit("Short text."), "Length of 15 should be True.")

        # Scenario B: Text is too long.
        self.assertFalse(design_tools.is_text_fit("This is the long text."), "Length over 15 should be False.")


    # 2. Test for Responsive Padding Logic (calculate_padding)
    def test_responsive_padding_calculation(self):
        """
        Verifies that padding calculations are correct for different screen sizes. (Base unit is 8px)
        """
        # Scenario 1: Mobile Screen (< 600px)
        self.assertEqual(design_tools.calculate_padding(screen_size=599), 16, "Mobile padding should be 16px.")
        
        # Scenario 2: Tablet Screen (600px <= size < 1200px)
        self.assertEqual(design_tools.calculate_padding(screen_size=768), 24, "Tablet padding should be 24px.")
        
        # Scenario 3: Desktop Screen (>= 1200px)
        self.assertEqual(design_tools.calculate_padding(screen_size=1920), 32, "Desktop padding should be 32px.")


if __name__ == '__main__':
    unittest.main()
