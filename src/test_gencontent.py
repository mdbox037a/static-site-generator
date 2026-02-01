import unittest

from gencontent import extract_title


class TestGenContent(unittest.TestCase):
    def test_et_normal(self):
        expected_result = "site heading"
        markdown = "# site heading\n\nhere is some text content"
        self.assertEqual(extract_title(markdown), expected_result)

    def test_et_2_h1(self):
        expected_result = "real h1"
        markdown = "# real h1\n\n# extra h1"
        self.assertEqual(extract_title(markdown), expected_result)

    def test_et_spaces_h1(self):
        expected_result = "site heading"
        markdown = " #  site heading  "
        self.assertEqual(extract_title(markdown), expected_result)


if __name__ == "__main__":
    unittest.main()
