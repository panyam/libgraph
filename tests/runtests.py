#!/usr/bin/env python

import unittest
import test_graph, test_bfs

suite1 = unittest.TestLoader().loadTestsFromTestCase(test_graph.Tests)
suite2 = unittest.TestLoader().loadTestsFromTestCase(test_bfs.Tests)
alltests = unittest.TestSuite([suite1, suite2])
unittest.TextTestRunner(verbosity=2).run(alltests)
