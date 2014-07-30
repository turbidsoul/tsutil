#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-07-30 10:07:05
# @Last Modified by:   Turbidsoul Chen
# @Last Modified time: 2014-07-30 10:14:44



def quick_sorted(lst, func=lambda a, b: cmp(a, b), reversed=False):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    before = []
    after = []
    for s in lst[1:]:
        res = func(s, pivot)
        if res > 0:
            after.append(s)
        else:
            before.append(s)
    before = quick_sorted(before, func=func)
    after = quick_sorted(after, func=func)
    if reversed:
        return (before + [pivot] + after)[::-1]
    else:
        return before + [pivot] + after
