#!/usr/bin/env python

import unittest
import test_graph, test_bfs, test_algos

alltests = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(test_graph.Tests),
        unittest.TestLoader().loadTestsFromTestCase(test_bfs.Tests), 
        unittest.TestLoader().loadTestsFromTestCase(test_algos.Tests)
    ])
unittest.TextTestRunner(verbosity=2).run(alltests)
