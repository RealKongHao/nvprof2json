#!/usr/bin/env python
# coding=utf-8

import json
import os

#kernel = {'0': ts_max, '1': ts_rank, '2': movavg. '3': signedpower, '4': fabsA, '5': stddev}
result = {'0': 0}

for i in range(0,6):
    cmd = "nvprof -o foo.nvvp --force-overwrite ~/TSbench/GPUbench/test/test 1000 5000 "
    cmd = cmd + str(i)
    p = os.popen(cmd)
    p.close()

    cmd1 = "python nvprof2json.py foo.nvvp >foo.json"
    p1 = os.popen(cmd1)
    p1.close()

    with open('foo.json', 'r') as f:
        data = json.load(f)

    for j in range(len(data)):
        if 'ts_max' in data[j]["name"]:
            #print ("%d ns" % data[j]["dur"])
            result[str(i)] = data[j]["dur"]
            break

for k in range(0,6):
    print ("kernel %d: %d ns" %(k, result[str(k)]))
