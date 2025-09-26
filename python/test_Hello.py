import unittest
from hello import say_hello  

class TestSayHello(unittest.TestCase):
    def test_say_hello_returns_hello_world(self):
        expected = "Hello World"
        result = say_hello()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
