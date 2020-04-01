# -*- coding: utf-8 -*-
# @Time : 2020/3/28 13:31
# @Author : wangmengmeng
from utils.http_request import HttpRequest

r = HttpRequest()


class ApiDept:
    def childrenDept(self, url, zoneId, keyword):
        pass

    def deptAllActual(self, type, zoneId, keyword):
        pass

    def deptForReport(self, url, params):
        return r.http_get(url, params)

    def deptTree(self, url, **kwargs):
        return r.http_get(url, **kwargs)

    def deptList(self, type, zoneId, keyword):
        pass
