"""
Run a collection of unit and integration tests on TsuserverDR.
It does not create any active accessible servers, but instead just merely
simulates client connections and actions.
"""

import sys
import unittest

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    else:
        pattern = 'test*.py'

    TEST_SUITE = unittest.TestLoader().discover('.', pattern=pattern)
    tester = unittest.TextTestRunner(verbosity=1, failfast=True)
    results = tester.run(TEST_SUITE)

    wrong = results.errors + results.failures
    if wrong:
        notification = 'TEST.PY FAILED'
        raise AssertionError(notification)