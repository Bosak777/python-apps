import random

# # 単語リスト（必要なら増やしてOK）
# words = ["apple", "banana", "grape", "orange", "mango", "cherry", "melon"]

# # ランダムな単語を選ぶ
# word = random.choice(words)
# guessed = ["_"] * len(word)
# used_letters = []
# mistakes = 0
# max_mistakes = 6

# print("★ ハングマンゲーム ★")
# print("英単語を1文字ずつ当ててね！")

# while mistakes < max_mistakes and "_" in guessed:
#     print("\n単語:", " ".join(guessed))
#     print(f"使った文字: {', '.join(used_letters)}")
#     print(f"ミス: {mistakes} / {max_mistakes}")

#     guess = input("文字を1つ入力: ").lower()

#     if len(guess) != 1 or not guess.isalpha():
#         print("1文字の英字を入力してください。")
#         continue
#     if guess in used_letters:
#         print("その文字はもう使っています。")
#         continue

#     used_letters.append(guess)

#     if guess in word:
#         print("正解！")
#         for i in range(len(word)):
#             if word[i] == guess:
#                 guessed[i] = guess
#     else:
#         print("不正解…")
#         mistakes += 1

# # 結果
# if "_" not in guessed:
#     print("\n🎉 おめでとう！単語を当てたよ！:", word)
# else:
#     print("\n😢 ゲームオーバー！正解は:", word)
import time
import re

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
word = random.choice(words)
word_list = list(word)
mojisuu = ["_"] * len(word_list)
print(word)  # あとでごめんとアウトする
print("ハングマンゲーム")
print("日本で再生数が多い曲のアーティスト名です")
difficulty = input("難易度を選んでください(easy/normal/hard):")
if difficulty == "easy":
    max_miss = 15
elif difficulty == "hard":
    max_miss = 8
else:
    max_miss = 10
print(max_miss, "間違えたらゲームオーバーです")
print()


def eiwa(word):
    has_japanese = bool(re.search(r"[\u3040-\u30FF\u4E00-\u9FFF]", word))
    has_english = bool(re.search(r"[a-zA-Z]", word))

    if has_japanese and not has_english:
        return "これはひらがな、漢字、カタカナ名だけのアーティストです"
    elif has_japanese and has_english:
        return "日本語と英語が混ざったアーティストです"
    elif has_english:
        return "英語だけのアーティスト名です"


print(eiwa(word))
print("単語:", " ".join(mojisuu))
print("アーティスト名がわかったら入力するところに”わかった”と入力してください")
used_word = []
start = time.time()
misu = 0
while "_" in mojisuu:
    itimoji = input("１文字入力してください")
    if itimoji == "わかった":
        kotae = input("答えを入力してください")
        if kotae == word:
            print("正解です")
            print("ミスの回数" + str(misu) + "/" + str(max_miss))
            end = time.time()
            print("クリア時間は、", round(end - start, 2), "秒です")
            break
        else:
            print("違います")
            misu += 1
            if misu >= max_miss:
                print("ゲームオーバーです。正解は、", word)
                break
    for i in range(len(word_list)):
        if itimoji == word_list[i]:
            mojisuu[i] = itimoji
    if itimoji != "わかった":
        used_word.append(itimoji)

    if itimoji != "わかった" and itimoji not in word_list:
        misu += 1
        if misu >= max_miss:
            print("ゲームオーバーです。正解は,", word)
            break
    print("単語", " ".join(mojisuu))
    print("使用した単語:", ",".join(used_word))
    print("ミスの回数" + str(misu) + "/" + str(max_miss))
    print()

if "_" not in mojisuu:
    end = time.time()
    print("正解です")
    print("クリア時間は、", round(end - start, 2), "秒です")
