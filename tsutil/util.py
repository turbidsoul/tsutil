#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-06-18 16:44:49
# @Last Modified by:   Turbidsoul Chen
# @Last Modified time: 2015-02-28 17:52:34

import requests
import json
from datetime import date, timedelta
from calendar import mdays
from functools import wraps


def singleton(cls, *args, **kwargs):
  '''
  singleton decorator
  '''
  instances = {}

  def _singleton():
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]
  return _singleton

def singleton_fun(fun):
  '''
  对方法的返回结果做单例
  使用参数作为key
  '''
  instances = {}
  @wraps(fun)
  def _singleton(*args, **kwargs):
    k = fun.__name__ + '_' + '|'.join(map(lambda it: str(it), args)) + '_' + '|'.join(str(it[0])+str(it[1]) for it in tuple(kwargs))
    if k not in instances:
      instances[k] = fun(*args, **kwargs)
    return instances[k]
  return _singleton

sina = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s'
taobao = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'


def get_location_from_sina(ip):
  """
    {
      "ret":1,
      "start":"58.18.0.0",
      "end":"58.18.15.255",
      "country":"中国",
      "province":"内蒙古",
      "city":"兴安",
      "district":"",
      "isp":"联通",
      "type":"",
      "desc":""
    }
  """
  global sina
  response = requests.get(sina % ip)
  if not response.status_code == 200:
    return
  l = json.loads(response.content)
  if not l['ret'] == 1:
    return
  return ("%s,%s,%s,%s" % (l['country'], l['province'], l['city'], l['isp'])).encode('utf8')


def get_location_from_taobao(ip):
  """
  {
    "code":0,
    "data":{
      "country":"\u65e5\u672c",
      "country_id":"JP",
      "area":"",
      "area_id":"",
      "region":"",
      "region_id":"",
      "city":"",
      "city_id":"",
      "county":"",
      "county_id":"",
      "isp":"",
      "isp_id":"",
      "ip":"58.12.23.23"
    }
  }
  """
  global taobao
  response = requests.get(taobao % ip)
  if not response.status_code == 200:
    return
  l = json.loads(response.content)
  if not l['code'] == 0:
    return
  l = l['data']
  return ("%s,%s,%s,%s,%s" % (l['country'], l['area'], l['region'], l['city'], l['isp'])).encode('utf8')


def get_week_start_end_day():
  """
  Get the week start date and end date
  """
  t = date.today()
  wd = t.weekday()
  return (t - timedelta(wd), t + timedelta(6 - wd))


def get_month_start_end_day():
  """
  Get the month start date a nd end date
  """
  t = date.today()
  n = mdays[t.month]
  return (date(t.year, t.month, 1), date(t.year, t.month, n))

def toint(s):
  return int(s) if s and s.isdigit() else None
