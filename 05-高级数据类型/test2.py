#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import unittest

class V2exAPITest(unittest.TestCase):

    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        # querystring = {"name": "php"}
        for node_name in ['python', 'php', 'qna', 'random']:

            response = requests.request("GET", url, params={'name': node_name}).json()
            self.assertEqual(response['name'], node_name)

if __name__ == '__main__':

    unittest.main()


