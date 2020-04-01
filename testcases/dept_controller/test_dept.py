# -*- coding: utf-8 -*-
# @Time : 2020/3/28 11:32
# @Author : wangmengmeng
from api.dept_controller.api_dept import ApiDept
import pytest
from pprint import pprint
from utils.handle_json import read_data
from config.cfg import *


def get_data_deptForReport():
    data = read_data('../data/dept_controller/deptForReport.json')
    pprint(data)
    arrs = []
    for v in data.values():
        arrs.append((v.get('request').get("url"),
                     v.get('request').get("params"),
                     v.get('status_code')
                     ))
    return arrs


class TestDept:
    @pytest.mark.parametrize("url,params,status_code", get_data_deptForReport())
    def test_deptForReport(self, url, params,status_code):
        url = auditcenter_url + url
        res = ApiDept().deptForReport(url, params)
        assert res.status_code == status_code



if __name__ == '__main__':
    data = get_data_deptForReport()
    print(data)
