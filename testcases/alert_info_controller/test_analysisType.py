# -*- coding: utf-8 -*-
# @Time : 2020/3/28 23:32
# @Author : wangmengmeng
from api.alert_info_controller.api_analysisType import ApiAnalysisType
from pprint import pprint


class TestAnalysisType:
    def test_analysisType(self):
        res = ApiAnalysisType().analysisType()
        pprint(res.json())
        str = "res.json()['data'] is not None"
        assert res.status_code == 200
        assert eval(str)
