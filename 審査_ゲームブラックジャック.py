# ブラックジャックを作る。
# --------これが基本的一人でやるようなブラックジャックのコード-------------------------------------
import random
import mysql.connector

# print("ルール説明")
# print("最初に２枚のカードが配られます。")
# print("そこから数字を引くか、引かないかを選択します。そして、合計が２１に近い方が勝ちです。")
# print("出た数字が２１を超えたら負けです。")
# a, b = random.randint(1, 12), random.randint(1, 12)
# print(a)
# print(b)
# t = a + b
# print(f"最初の数字は{a}と{b}の{t}です。")
# while True:
#     if t == 21:
#         print("お前、うんいいな")
#         break
#     elif t < 21:
#         print("もう一度引きますか？引くならyesを、引かないならnoと入れてください")
#         r = input()
#         if r == "yes":
#             r = random.randint(1, 12)
#             t += r
#             print(f"引いた数字は{r}です。今の合計は{t}です")
#             if r > 21:
#                 print("21を超えた、運ないなぁ〜")
#                 break
#         elif r == "no":
#             break
#         else:
#             print("yesかnoで入力してね！！")
#     else:
#         print("２１を超えた、運ないなぁ〜")
#         break


# -------------------ここからは、対人のブラックジャック-----------------------------------
# mysqlサーバーへの接続情報
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='bosaklong',
    database='python_game'
)
# 接続確認
if conn.is_connected():
    print("mysqlサバーに接続成功！！")
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
a, b = random.choice(li), random.choice(li)  # プレイヤーのカード
c, d = random.choice(li), random.choice(li)  # ディーラーのカード
ab = a + b  # プレイヤーの合計
cd = c + d  # ディーラーの合計
win = "勝ち"
lose = "負け"
dra = "引き分け"
pyl = "プレイヤー"
dea = "ディーラー"
print(f"プレイヤーのカードは{a}と{b}の{ab}です")
pk = 2  # プレイヤーが引いた回数カウントしていく
dk = 2  # ディーラーが引いた回数カウントしていく
while True:
    if ab == 21:
        print(pyl + win)  # プレイヤーが２１を出した場合
        print(f"{dea}の数は{c}と{d}の{cd}です")
        break
    elif ab < 21:
        print("もう一度引きますあか？引くならhitを、引かないならstandと入れてください")
        r = input()
        if r == "hit":
            r = random.choice(li)
            ab += r
            pk += 1
            print(f"引いた数は{r}です。今の合計は{ab}です")
            print(f"{pyl}の引いたカードの枚数は{pk}枚です")
            if ab > 21:
                print(pyl + lose)
                print(dea + win)
                break
        elif r == "stand":
            print(f"{pyl}の合計は{ab}です。{dea}のターンに移ります")
            print(f"{dea}の数は{c}と{d}の{cd}です")
            if cd == 21:
                print(pyl + lose)
            elif ab == 21 and cd == 21:
                print(dra)
            elif cd <= 17:
                dr = random.choice(li)
                cd += dr
                dk += 1
                print(f"{dea}が引いた数は{dr}です。今の合計は{cd}です")
                print(f"{dea}が引いたカードの枚数は{dk}枚です")
                if cd > 21:
                    print(pyl + win)
                elif cd > ab:
                    print(pyl + lose)
                elif cd == ab:
                    print(dra)
            break
        else:
            print("hitかstandで入力してね！！")
    else:
        print("21を超えた、運ないなぁ〜")
        break
cursor = conn.cursor()

# データ挿入のクエリ
insert_query = "insert into blackjack_app(id, blackjack_game) values(%s,%s)"
if ab > 21:
    data = (None, "lose")
elif cd > 21:
    data = (None, "win")
elif ab > cd:
    data = (None, "win")
elif ab == cd:
    data = (None, "draw")
else:
    data = (None, "lose")
# 勝率のデータ挿入のクエリ

# クエリ実装　executeはsql文を使いときに必ず使うコード
cursor.execute(insert_query, data)
# 変更を反映
conn.commit()

cursor.execute("select * from blackjack_app")
rows = cursor.fetchall()
# 結果の表示
for row in rows:
    print(row)

cursor.execute(insert_query, data)
conn.commit()

# 挿入されたIDを取得
# new_id = cursor.lastrowid
# print("新しいID:", new_id)
# 勝敗の集計
# fetchone()[0]でタプルの要素の０番目をとるだから例えば（９,”win”,None）だったら０番目の９をとる
cursor.execute("SELECT COUNT(*) FROM blackjack_app")
total_games = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM blackjack_app WHERE blackjack_game = 'win'"
    )
win_games = cursor.fetchone()[0]
# 勝率計算
if total_games > 0:
    win_rate = win_games / (total_games-1) * 100
    print(f"これまでの試合数: {(total_games-1)}")
    print(f"勝ち数: {win_games}")
    win_rate = (f"{win_rate:.1f}")
    print(f"勝率: {win_rate}%")
else:
    print("まだ試合データがありません")
#  データを削除して１から開始
reset = input("データをリセットしますか？リセットするならyesと入力してください")
if reset == "yes":
    cursor.execute("truncate table blackjack_app")

    cursor.close()
    conn.close()

    print("データをリセットしました！（AUTO_INCREMENTも1から）")
else:
    print("データはリセットされていません")
# 追加したい要素
# データベース　python_game
# テーブル名　blackjack_app
# カラム名勝敗　blackjack_game
# カラム名勝率　blackjack_winningrate　
# カードを引いた回数と、ディーラー、プレイヤーがどちらも２１の場合引いたカードの数で勝敗が決まるようにする。
# ディーラーが１７以下ならカードをずっと引くようにする。
# １が出た場合は、１１として扱いうかそれとも、１として扱うか自分で選ぶことができるようにする。
# カードの枚数も表示するようにする。
# -------------------ここまでが対人のブラックジャック-----------------------------------
