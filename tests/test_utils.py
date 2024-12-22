import unittest
from utils.helper import resolve_hostname, is_valid_ip

class TestUtils(unittest.TestCase):
    def test_resolve_hostname(self):
        """Test hostname resolution."""
        self.assertEqual(resolve_hostname("localhost"), "127.0.0.1")

    def test_is_valid_ip(self):
        """Test IP validation."""
        self.assertTrue(is_valid_ip("192.168.1.1"))
        self.assertFalse(is_valid_ip("999.999.999.999"))

if __name__ == "__main__":
    unittest.main()
