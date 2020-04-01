# -*- coding: utf-8 -*-
# @Time : 2020/3/29 18:01
# @Author : wangmengmeng
import pytest
from api.zone_controller.api_zone import ApiZone


class TestZone:
    @pytest.mark.parametrize("keyword,expected", [(None, "res.json() is not None"), ("鼓楼医院", "not res.json() is None")])
    def test_zoneForReport(self, keyword, expected):
        res = ApiZone().zoneForReport(keyword)
        assert eval(expected)
