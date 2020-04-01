# -*- coding: utf-8 -*-
# @Time : 2020/3/28 23:29
# @Author : wangmengmeng
from utils.http_request import HttpRequest
from config.cfg import *

r = HttpRequest()


class ApiAnalysisType:
    def analysisType(self):
        url = auditcenter_url + '/api/v1/analysisType'
        return r.http_get(url)
