import time
import random

print("合図が出たらenterを押す")

sec = random.uniform(1,10)
time.sleep(sec)
print("押せぇぇぇ！！！！")
start = time.time()
e = input()
end = time.time()
time_diff = end - start
timediff = "{:.4}".format(time_diff)
if time_diff < 0.01:
    print("合図が出る前に押すな〜不正するな！！")
    pass
else:
    print(f"あなたの反応速度は:{timediff}秒です。")

 

 