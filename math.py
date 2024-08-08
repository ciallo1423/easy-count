import random
import operator
import winsound
import os
# 定义四则运算
operations = {
    '+': operator.add,
    '-': operator.sub,
    '×': operator.mul,
}

def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(list(operations.keys()))
    #确保不会产生负数
    if op == '-':
        num1 = num1 + num2
    question = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    return question, answer

def main():
    correct_answers = 0
    total_questions = 20
    i=0

    while i<20:
        question, answer = generate_question()
        print(f"问题 {i + 1}: {question} = ?")
        
        while True:
            try:
                user_answer = int(input("你的答案: "))
                if user_answer == answer：
                    print("正确!")
                    winsound.Beep(1000, 500)  # 发出提示音，频率1000Hz，持续500ms
                    i+= 1
                    break
                else:
                    print("错误，请再试一次。")
                    break
            except ValueError:
                print("请输入一个有效的数字。")

    print(f"游戏结束！")
    os.system("pause")

if __name__ == "__main__":
    main()
