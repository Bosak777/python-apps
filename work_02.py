import time
import random
import mysql.connector
import datetime

dt_now = datetime.datetime.now()
print(dt_now)

# MySQLサーバーへの接続情報
conn = mysql.connector.connect(
    host="localhost", user="root", password="bosaklong", 
    database="python_reflexes"
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
plnm = input("プレイヤー名を入力してください")
# id,カラム名　record_time(何秒なのか),started_at(いつやったのか)
# プレイヤーの名前を入れる(カラム名　player_name)
# 作成するテーブル名　work2_py
cursor = conn.cursor()
# データ挿入のリクエスト
insert_query = "insert into work2_py(record_time, player_name) "
"values(%s, %s)"
data = (timediff, plnm)
#  クエリ実装
cursor.execute(insert_query, data)
#  変更を反映
conn.commit()
cursor.execute("select * from work2_py")
rows = cursor.fetchall()
cursor.execute("select * from work2_py order by record_time asc limit 5")
asc = cursor.fetchall()
cursor.execute("select * from work2_py order by record_time asc limit 1")
bast = cursor.fetchall()
# 結果の表示
for row in rows:
    print(row)
print("========ここから上位5人です=========")
for a in asc:
    print(a)
print("========ここから最速記録です=========")
for b in bast:
    print(b)
#  データを削除して１から開始
# cursor.execute("truncate table work2_py")

# cursor.close()
# conn.close()

# print("データをリセットしました！（AUTO_INCREMENTも1から）")
