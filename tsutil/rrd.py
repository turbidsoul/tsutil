#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-07-18 16:53:33
# @Last Modified 2014-07-19


import time
from subprocess import Popen, PIPE
from enum import Enum
from util import is_str


class RRDError(Exception):
    pass


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
            self.rrd_file,
            '--start', str(self.start),
            '--step', str(self.step),
        ]

        if self.no_overwrite:
            cmd.append('--no-overwrite')

        for ds in self.dataSources:
            cmd.append(str(ds))

        for rra in self.rras:
            cmd.append(str(rra))
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        result, error = p.communicate()
        if len(error) > 0:
            return (False, error)
        else:
            return True
    def info(self):
        cmd = [
            'rrdtool',
            'info',
            self.rrd_file
        ]

        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        result, error = p.communicate()
        if len(error) > 0:
            return (False, error)
        else:
            infos = {}
            for line in result.split('\n'):
                line.split('=')
            return (True, result)

    def first(self):
        cmd = [
            'rrdtool',
            'first',
            self.rrd_file
        ]

        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        result, error = p.communicate()
        if len(error) > 0:
            return (False, error)
        else:
            return (True, int(result))

    def last(self):
        cmd = [
            'rrdtool',
            'last',
            self.rrd_file
        ]

        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        result, error = p.communicate()
        if len(error) > 0:
            return (False, error)
        else:
            return (True, int(result))
        



if __name__ == '__main__':
    r = RRD('c:/test.rrd')
    ok, result = r.last()
    print(ok)
    print(result)
