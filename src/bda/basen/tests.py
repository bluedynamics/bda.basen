# -*- coding: utf-8 -*-
from pprint import pprint

import doctest
import unittest


optionflags = (
    doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.REPORT_ONLY_FIRST_FAILURE
)

TESTFILES = ["tests.rst"]


def test_suite():
    return unittest.TestSuite(
        [
            doctest.DocFileSuite(
                file, optionflags=optionflags, globs={"pprint": pprint}
            )
            for file in TESTFILES
        ]
    )


if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")  # pragma NO COVERAGE
