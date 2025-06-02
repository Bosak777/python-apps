print("test")

print("input_line")
import random
r = random.randint(1,100)
print(r)
p = "大不正解　もう一度試してみて！"
print("1~100までの数字を当ててください")
if r < 50:
    print("50未満です")
else:
    print("50以上です")
for i in range(5):
     w = int(input())
     print(f"あなたが入力した数字は、{w}です。")
     if w == r:
          print("大正解！！")
          break
     elif r < 25:
        print("そのランダムな数字は、25未満です")
        print(p)
     elif r > 75 :
        print("そのランダムな数字は、75より大きいです")
        print(p)
     else:
        print(p)
        if r >= 25 and r < 50:
            print("25~49の間です")
        elif r <= 75 and r >=50:
            print("50~75の間です")
        elif r < 25 and r <= 10:
            print("１の桁です")
            
            

 

 