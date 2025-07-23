import random  # ランダム
import time  # 時間を計測する
import re  # 文字のパターンを調べる

words = [
    "mrs,greenapple",
    "yoasobi",
    "official髭男dism",
    "backnumber",
    "bts",
    "vaundy",
    "あいみょん",
    "優里",
    "kinggnu",
    "ado",
    "米津玄師",
]
word = random.choice(words)  # ランダムにアーティスト名を選ぶ
word_list = list(word)  # 選んだものをリストにする
mojisuu = ["_"] * len(word_list)  # ワードの列の文だけ＿をつける
print(word)  # あとでごめんとアウトする
print("ハングマンゲーム")
print("日本で再生数が多い曲のアーティスト名です")
difficult = input("難易度を選んでください(easy/normal/hard):")  # 難易度の設定
if difficult == "easy":
    max_miss = 15
elif difficult == "hard":
    max_miss = 8
else:
    max_miss = 10
print(max_miss, "間違えたらゲームオーバーです")
print()


def eiwa(word):  # def関数で英語か日本語かを検出する
    has_japanese = bool(re.search(r"[\u3040-\u30FF\u4E00-\u9FFF]", word))
    # 日本語の検出　boolはTureかどうか
    has_english = bool(re.search(r"[a-zA-Z]", word))  # 英語の検出

    if has_japanese and not has_english:
        # and notで日本語が含まれている{かつ(and)}英語が含まれていない(not)
        return "これはひらがな、漢字、カタカナ名だけのアーティストです"
    elif has_japanese and has_english:  # andはどちらもTureの場合
        return "日本語と英語が混ざったアーティストです"
    elif has_english:  # 英語の場合
        return "英字だけのアーティスト名です"


print(eiwa(word))
print("単語:", " ".join(mojisuu))  # join()でリストを戻す
print("アーティスト名がわかったら入力するところに”わかった”と入力してください")
used_word = []
start = time.time()  # timeで時間を数える
misu = 0
while "_" in mojisuu:  # mojisuuに＿が含まれていたらループする
    itimoji = input("１文字入力してください")
    if itimoji == "わかった":
        kotae = input("答えを入力してください")
        if kotae == word:
            print("正解です")
            print("ミスの回数" + str(misu) + "/" + str(max_miss))
            end = time.time()  # エンドでtimeのカウントを終了
            print("クリア時間は、", round(end - start, 0), "秒です")
            # roundで四捨五入して、２で小数点第２まで出す
            break
        else:
            print("違います")
            misu += 1
            if misu >= max_miss:
                print("ゲームオーバーです。正解は、", word)
                break
    for i in range(len(word_list)):
        if itimoji == word_list[i]:  # 入力された文字がwordの中に入っていたら
            mojisuu[i] = itimoji  # 文字をitimojiに変える
    if itimoji != "わかった":
        used_word.append(itimoji)  # 空のリストに１文字入力した文字をappendで追加する

    if itimoji != "わかった" and itimoji not in word_list:
        # わかったと入力されていないかつword_listにitimojiが含まれていなかったら
        misu += 1
        if misu >= max_miss:
            print("ゲームオーバーです。正解は,", word)
            break
    print("単語", " ".join(mojisuu))
    print("使用した単語:", ",".join(used_word))
    print("ミスの回数" + str(misu) + "/" + str(max_miss))
    print()  # 一行あける

if "_" not in mojisuu:  # 文字に＿が含まれていない場合
    end = time.time()
    print("正解です")
    print("クリア時間は、", round(end - start, 0), "秒です")
