# ブラックジャックを作る。
# --------これが基本的一人でやるようなブラックジャックのコード-------------------------------------
import random

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
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
a, b = random.choice(li), random.choice(li)  # プレイヤーのカード
c, d = random.choice(li), random.choice(li)  # ディーラーのカード
ab = a + b  # プレイヤーの合計
cd = c + d  # ディーラーの合計
print(f"プレイヤーのカードは{a}と{b}の{ab}です")
pk = 2  # プレイヤーが引いた回数カウントしていく
dk = 2  # ディーラーが引いた回数カウントしていく
while True:
    if ab == 21:
        print("プレイヤーの勝ち")  # プレイヤーが２１を出した場合
        print(f"ディーラーの数は{c}と{d}の{cd}です")
        break
    elif ab < 21:
        print("もう一度引きますあか？引くならhitを、引かないならstandと入れてください")
        r = input()
        if r == "hit":
            r = random.choice(li)
            ab += r
            pk += 1
            print(f"引いた数は{r}です。今の合計は{ab}です")
            print(f"プレイヤーの引いたカードの枚数は{pk}枚です")
            if ab > 21:
                print("プレイヤーの負け")
                break
        elif r == "stand":
            print(f"プレイヤーの合計は{ab}です。ディーラーのターンに移ります")
            print(f"ディーラーの数は{c}と{d}の{cd}です")
            if cd == 21:
                print("プレイヤーの負け")
            elif ab == 21 and cd == 21:
                print("引き分け")
            elif cd <= 17:
                dr = random.choice(li)
                cd += dr
                dk += 1
                print(f"ディーラーが引いた数は{dr}です。今の合計は{cd}です")
                print(f"ディーラーが引いたカードの枚数は{dk}枚です")
                if cd > 21:
                    print("プレイヤーの勝ち")
                elif cd > ab:
                    print("プレイヤーの負け")
                elif cd == ab:
                    print("引き分け")
                else:
                    print("プレイヤーの勝ち")
            break
        else:
            print("hitかstandで入力してね！！")
    else:
        print("21を超えた、運ないなぁ〜")
        break
# 追加したい要素
# カードを引いた回数と、ディーラー、プレイヤーがどちらも２１の場合引いたカードの数で勝敗が決まるようにする。
# ディーラーが１７以下ならカードをずっと引くようにする。
# １が出た場合は、１１として扱いうかそれとも、１として扱うか自分で選ぶことができるようにする。
# カードの枚数も表示するようにする。
# -------------------ここまでが対人のブラックジャック-----------------------------------
