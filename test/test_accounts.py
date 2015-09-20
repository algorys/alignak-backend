#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import unittest2
import requests
import json


class TestBAccounts(unittest2.TestCase):

    def test_Auth_Activated(self):
        ret = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_nousername_nopassword(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={})
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_nousername(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={'password': 'test'})
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_nopassword(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={'username': 'test'})
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_wrongusername(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={'username': 'test', 'password': 'admin'})
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_wrongpassword(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={'username': 'admin', 'password': 'test'})
        self.assertEqual(ret.status_code, 401)
        self.assertEqual(ret.json(), {"_status": "ERR", "_error": {"message": "Please provide proper credentials", "code": 401}})

    def test_login_successfull(self):
        ret = requests.post('http://127.0.0.1:5000/login', json={'username': 'admin', 'password': 'admin'})
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.json(), {u'token': u'1442583404086-8179e10c-f505-408a-bf30-86c85a8dc2d3'})
