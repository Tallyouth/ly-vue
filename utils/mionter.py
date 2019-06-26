# -*- coding:utf-8 -*-

import psutil
import os
import re
import codecs


# 判断进程是否存在
def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return True
            break
    else:
        return False


def file_name(file_dir):
    list_path = []
    list_file = []
    for root, dirs, files in os.walk(file_dir):
        for file_read in files:
            if '.py' in file_read:
                try:
                    spider_text = root + '/' + file_read
                    f = codecs.open(spider_text, encoding='utf-8')
                    lines = f.readlines()
                    for line in lines:
                        name_spider = re.findall("name = '(.*?)'", line)
                        if len(name_spider) != 0:
                            list_path.append(spider_text)
                            list_file.append(name_spider[0])
                except UnicodeDecodeError:
                    print('文件读取失败{}'.format(spider_text))
    dic = dict(map(lambda x, y: [x, y], list_file, list_path))
    return dic


if __name__ == "__main__":
    # disk = input("process:")
    # if judgeprocess(disk):
    #     print(1)
    print(file_name('D:/mionter/utils'))
