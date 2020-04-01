# -*- coding: utf-8 -*-
# @Time : 2020/3/25 11:48
# @Author : wangmengmeng
import os

host = '10.1.1.120'
port = 9999
auditcenter_url = 'http://{}:{}/auditcenter'.format(host, port)
username = 'admin'
password = 'ipharmacare'
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
suite_path = os.path.join(proj_path, 'testsuite')
config_path = os.path.join(proj_path, 'config')
testcases_path = os.path.join(proj_path, 'testcases')
api_path = os.path.join(proj_path, 'api')
xls_path = os.path.join(proj_path, 'xlscase_file')
