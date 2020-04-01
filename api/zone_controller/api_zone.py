# -*- coding: utf-8 -*-
# @Time : 2020/3/29 17:58
# @Author : wangmengmeng
from utils.http_request import HttpRequest
from config.cfg import *

r = HttpRequest()


class ApiZone:
    def zoneForReport(self, keyword):
        url = auditcenter_url + '/api/v1/zoneForReport'
        params = {
            "keyword": keyword
        }
        return r.http_get(url, params)
