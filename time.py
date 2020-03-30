import time

def sleep(sleep_time=2):
    print("Start : %s" % time.ctime())
    time.sleep(sleep_time)
    print("End : %s" % time.ctime())

sleep(4)
# 调试 ${sleep(4)}