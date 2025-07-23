import random


r = random.randint(1, 100)
print(r)
p = "大不正解　もう一度試してみて！"
print("1~100までの数字を当ててください")
if r < 50:
    print("50未満です")
else:
    print("50以上です")
count = 0
for i in range(5):
    w = int(input())
    count += 1
    print(f"あなたが入力した数字は、{w}です。")
    if w == r:
        print(f"大正解！！{count}回で当てました。")
        break
    else:
        print("大不正解！！もう一度")
        if w < r:
            print(f"その数は{w}より大きい")
        else:
            print(f"その数は{w}はより小さい")
if w == r:
    pass
else:
    print("もう一回やりますか〜？？やるなら yes をやめるならww no を:")
    w = input()
    if w == "yes":
        count = 5
        for i in range(5):
            print("では数字を入力してください")
            w = int(input())
            count += 1
            print(f"あなたが入力した数字は、{w}です")
            if w == r:
                print(f"大正解！！{count}回で当てました")
                break
            else:
                print("大不正解！！残念")
                if r < 25:
                    print("25より小さいです")
                elif r > 75:
                    print("75より大きいです")
                else:
                    print("25〜75の間です")
    else:
        print("また挑戦しにこいよ！")

print(f"正解は{r}でした。")
