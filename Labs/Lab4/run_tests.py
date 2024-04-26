import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("./tests", pattern="*_test.py")
    unittest.TextTestRunner().run(suite)

