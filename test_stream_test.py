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






"""
dict = {}
with open('test_data.json', 'r') as f:
    top_data = json.load(f)

    for a in top_data['hits']:
        if a.get('images'):
            d = {'thumbnail':{
                'credit': a['images'][0]['credit'],
                'format': a['images'][0]['format'],
                'height': a['images'][0]['height'],
                'image_id': a['images'][0]['image_id'],
                'revision': a['images'][0]['revision'],
                'src_image_url': a['images'][0]['src_image_url'],
                'width': a['images'][0]['width']
                }}
    top_data['hits'].insert(0, d)

#print(top_data)

#        self.assertEqual(get_username(dummy_user), 'john')
wf = open('output.txt', 'w')
wf.write(str(top_data))
wf.close()
"""
