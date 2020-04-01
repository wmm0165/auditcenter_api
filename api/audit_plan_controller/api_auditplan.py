# -*- coding: utf-8 -*-
# @Time : 2020/3/29 14:11
# @Author : wangmengmeng
from config.cfg import *
from utils.http_request import HttpRequest

r = HttpRequest()


class ApiAuditPlan:

    def auditplan_add(self, name):
        """新增审方方案"""
        url = auditcenter_url + "/api/v1/auditPlan"
        json_data = {
            "name": name,
            "category": 2,
            "createdTime": 1585463097182,
            "modifiedTime": 1585463097182,
            "recipeSource": "0",
            "deptList": [],
            "doctorList": [],
            "groupList": [],
            "isOuvas": 0,
            "isPivas": 0,
            "minStay": "",
            "maxStay": "",
            "minAge": "",
            "maxAge": "",
            "ageUnit": "岁",
            "costTypes": "",
            "patientCondition": "",
            "iptWardList": [],
            "weekList": [],
            "startTime": "00:00",
            "endTime": "23:59"
        }
        return r.http_post(url,json=json_data)

    def auditplan_view(self):
        """查看审方方案"""
        pass

    def auditplan_modify(self):
        """修改审方方案"""
        pass

    def auditplan_del(self):
        """删除审方方案"""
        pass

    def auditplan_list(self):
        """方案列表"""
        pass


if __name__ == '__main__':
    ap = ApiAuditPlan()
    print(ap.auditplan_add("测试脚本123").json())
