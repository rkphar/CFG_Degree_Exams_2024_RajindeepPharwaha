import unittest
from Coding_Exam import no_of_handshakes

class TestHandshakes(unittest.TestCase):

    def test_no_handshakes_for_one_person(self):
        self.assertEqual(no_of_handshakes(15), 105, "Should be 105")

    def test_no_handshakes_for_zero_people(self):
        self.assertEqual(no_of_handshakes(0), 0, "Should be 0")

    def test_handshakes_for_two_people(self):
        self.assertEqual(no_of_handshakes(78), 3003, "Should be 3003")

    def test_handshakes_for_three_people(self):
        self.assertEqual(no_of_handshakes(26), 325, "Should be 325")

    def test_handshakes_for_four_people(self):
        self.assertEqual(no_of_handshakes(10), 45, "Should be 45")

if __name__ == '__main__':
