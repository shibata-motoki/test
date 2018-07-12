import unittest
import pytest
from unittest import mock
import json

from test_stream import get_image

"""
class TestGetImagedata(unittest.TestCase):
    def test__get(self):
        dummy_image = mock.Mock()
"""

class TestGetImagedata(unittest.TestCase):
    def test_get_image(self):
        dummy_image = mock.Mock()
        dummy_image.top_data = {'hits': [{
          'images': [{
              'credit': '',
              'expires_at': null,
              'format': 'jpg',
              'height': 1564,
              'image_id': 'DSXMZO3270807006072018000001',
              'src_image_url': 'https://imgix-proxy.n8s.jp/DSXMZO3270807006072018000001-2.jpg',
              'width': 1564
              }]}]}
        assert get_image(dummy_data) == {'hits': [{'thumbnail':{
            'credit': '',
            'format': 'jpg',
            'height': 1564,
            'image_id': 'DSXMZO3270807006072018000001',
            'revision': a['images'][0]['revision'],
            'src_image_url': 'https://imgix-proxy.n8s.jp/DSXMZO3270807006072018000001-2.jpg',
            'width': 1564
            }}][{
          'images': [{
              'credit': '',
              'format': 'jpg',
              'height': 1564,
              'image_id': 'DSXMZO3270807006072018000001',
              'src_image_url': 'https://imgix-proxy.n8s.jp/DSXMZO3270807006072018000001-2.jpg',
              'width': 1564
              }]}]}


if __name__ == '__main__':
    unittest.main()
