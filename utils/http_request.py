# -*- coding: utf-8 -*-
# @Time : 2020/3/28 2:43
# @Author : wangmengmeng
import requests
import hashlib
import json
from config.cfg import *


class HttpRequest:
    def __init__(self):
        self.session = requests.session()
        m = hashlib.md5()
        m.update(password.encode())
        passwd = m.hexdigest()
        params = {"name": username, "password": passwd}
        headers = {'Content-Type': "application/json"}
        self.session.post('http://{}:9999/syscenter/api/v1/currentUser'.format(host), data=json.dumps(params),
                          headers=headers).json()  # 访问swagger需要事先登录

    def http_post(self, url, json=None):
        return self.session.post(url, json=json)   # 这种封装方式只适合入参为json格式的请求，不适用于表单请求

    def http_get(self, url, params=None):
        return self.session.get(url, params=params)
