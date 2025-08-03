# test_cybermatrix.py
"""
Tests for CyberMatrix module.
"""

import unittest
from cybermatrix import CyberMatrix

class TestCyberMatrix(unittest.TestCase):
    """Test cases for CyberMatrix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CyberMatrix()
        self.assertIsInstance(instance, CyberMatrix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CyberMatrix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
