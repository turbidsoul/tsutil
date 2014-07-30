#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-07-18 16:53:33
# @Last Modified 2014-07-19


import re
import time
import platform
from subprocess import PIPE, Popen

from enum import Enum
from util import is_str

if platform.python_version()[:-2] >= '2.7':
    from collections import OrderedDict
else:
    from ordereddict import OrderedDict

_infoPort = re.compile(r"^\s*(.*?)\s*=\s*(.*?)\s*$")


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
            infos = OrderedDict()
            for line in result.split('\n'):
                line = line.strip()
                k, v = _infoPort.match(line).groups()
                if k.startswith('ds['):
                    dskeys = k.split('.')
                    dsname = dskeys[0][3:-1]
                    dskey = dskeys[1]
                    ds = None
                    if dsname in infos:
                        ds = infos[dsname]
                    else:
                        ds = DS()
                        ds.name = dsname
                    v = v.strip('"')
                    if dskey == 'type':
                        ds.ds_type = v
                    elif dskey == 'min':
                        ds.minval = int(v)
                    elif dskey == 'max':
                        ds.maxval = int(v)
                    # elif 
                elif k.startswith('rra['):
                    pass
                else:
                    v = v.strip('"')
                    if v.isdigit():
                        v = int(v)
                    infos[k] = v
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
