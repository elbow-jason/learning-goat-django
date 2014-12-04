from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """docstring for SmokeTest"""

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

    def test_bad_assertion(self):
        self.assertEqual(True, False)
