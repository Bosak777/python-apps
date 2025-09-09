import time
import random
import mysql.connector
import datetime

dt_now = datetime.datetime.now()
print(dt_now)

# MySQLサーバーへの接続情報
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='bosaklong',
    database='python_reflexes'
)

# 接続確認
if conn.is_connected():
    print("MySQLサーバーに接続成功！")


print("合図が出たらenterを押す")

sec = random.uniform(1, 10)
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
# id,カラム名　record_time(何秒なのか),started_at(いつやったのか)
# 作成するテーブル名　work2_py
cursor = conn.cursor()
# データ挿入のリクエスト
insert_query = "insert into work2_py(id, record_time) values(%s,%s)"
data = (None, timediff)
#  クエリ実装
cursor.execute(insert_query, data)
#  変更を反映
conn.commit()
cursor.execute("select * from work2_py")
rows = cursor.fetchall()
# 結果の表示
for row in rows:
    print(row)
#  データを削除して１からかいし
# cursor.execute("truncate table work2_py")

# cursor.close()
# conn.close()

# print("データをリセットしました！（AUTO_INCREMENTも1から）")
