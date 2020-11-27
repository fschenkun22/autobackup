"""
common
"""
import shutil
import os
import logging
from conf.settings import LOG_PATH

SUFFIXES = {1000:['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024:['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
def humanReadable_size(size,is_1024_byte=True):
    #mutiple默认是1000
    mutiple=1000 if is_1024_byte else 1024
    #与for遍历结合起来，这样来进行递级的转换
    for suffix in SUFFIXES[mutiple]:
        size/=mutiple
        #直到Size小于能往下一个单位变的数值
        
        if size<mutiple:
            return '{0:.6f}{1}'.format(size,suffix)
    raise ValueError('number too large')  # 抛出异常


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.getsize(os.join(root, name)) for name in files])
    return humanReadable_size(size)

def logging_init():
    logging.basicConfig(filename = LOG_PATH)