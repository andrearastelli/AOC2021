import unittest

from AOC2021.day_12.p1 import build_paths, list_networks

class TestBase(unittest.TestCase):

    def test_first_example(self):
        source = [
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end",
        ]

        paths = build_paths(source)
        networks = list(list_networks(paths))

        results = [
            "start,A,b,A,c,A,end",
            "start,A,b,A,end",
            "start,A,b,end",
            "start,A,c,A,b,A,end",
            "start,A,c,A,b,end",
            "start,A,c,A,end",
            "start,A,end",
            "start,b,A,c,A,end",
            "start,b,A,end",
            "start,b,end",
        ]
        self.assertListEqual(networks, results)
