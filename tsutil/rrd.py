#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-07-18 16:53:33
# @Last Modified by:   Turbidsoul Chen
# @Last Modified time: 2014-07-19 17:41:19


import time
import subprocess
from enum import Enum
from util import is_str


class DSType(Enum):
    GAUGE = 'GAUGE'
    COUNTER = 'COUNTER'
    DERIVE = 'DERIVE'
    ABSOLUTE = 'ABSOLUTE'
    COMPUTE = 'COMPUTE'


class CF(Enum):
    AVERAGE = 'AVERAGE'
    MIN = 'MIN'
    MAX = 'MAX'
    LAST = 'LAST'


class DS(object):

    def __init__(self, name, ds_type, heartbeat, minval='U', maxval='U'):
        self.name = name
        if is_str(ds_type):
            ds_type = DSType.value_of(ds_type.upper())
        self.ds_type = ds_type
        self.heartbeat = heartbeat
        self.minval = minval
        self.maxval = maxval

    def __str__(self):
        return 'DS:%s:%s:%s:%s:%s' % (self.name, self.ds_type.name,
                                      str(self.heartbeat), str(self.minval),
                                      str(self.maxval))

    def __repr__(self):
        return self.__str__()



class RRA(object):
    def __init__(self, cf, xff, steps, rows):
        if is_str(cf):
            cf = CF.value_of(cf)
        self.cf = cf
        self.xff = xff
        self.steps = steps
        self.rows = rows

    def __str__(self):
        return "RRA:%s:%.1f:%d:%d" % (self.cf.name, self.xff, self.steps,
                                       self.rows)

    def __repr__(self):
        return self.__str__()

class RRD(object):

    def __init__(self, rrd_file, start=int(time.time())-10, step=300,
                 dataSources=[], rras=[], no_overwrite=False, mode='w'):
        self.rrd_file = rrd_file
        self.start=start
        self.step=step
        self.dataSources = dataSources
        self.rras = rras
        self.no_overwrite = no_overwrite
        self.mode=mode
        if self.mode == 'r':
            pass


    def create(self):
        cmd = [
            'rrdtool',
            'create',
            '--start', str(self.start),
            '--step', str(self.step),
        ]

        if self.no_overwrite:
            cmd.append('--no-overwrite')

        for ds in self.dataSources:
            cmd.append(str(ds))

        for rra in self.rras:
            cmd.append(str(rra))
        print(cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(p)
        output = p.communicate()
        print(output)




if __name__ == '__main__':
    dss = [
        DS('test1', DSType.COUNTER.name, 60),
        # DS('test2', DSType.GAUGE.name, 60)
    ]
    rras = [
        RRA(CF.AVERAGE, xff=0.5, steps=60, rows=24),
        # RRA(CF.MAX, xff=0.5, steps=60, rows=24)
    ]
    r = RRD('c:/test.rrd', dataSources=dss, rras=rras)
    r.create()
