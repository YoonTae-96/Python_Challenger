#1번 사용자의 이름을 입력받아 출력하기
first_name = input()
print("Hello " + first_name)

#2번 사용자의 이름과 성을 구분해서 입력받고 출력하기
first_name = input()
last_name = input()
print("Hello " + first_name + " " + last_name)

#3번 print 한줄로 문장 \n 출력해주기
print("What do you call a beer with no teeth?\nA Gummy bear!")

#4번 2개의 숫자을 입력 받아서, 그 합을 출력하기
num1, num2 = map(int, input().split())
print("The totoal is ", num1 + num2)

#5번 총 3개의 숫자를 입력 받아서 (첫번째 + 두번째) * 세번째
num1, num2, num3 = map(int, input().split())
print("The total is ", (num1 + num2) * num3)

#6번 남은 피자 조각수 구하기
input_pizza = int(input())
eat_pizza = int(input("Eat pizza num: "))
print("Rest pizza num: ", input_pizza - eat_pizza)

#7번 계산 뿜빠이 하기
Bill = int(input("Bill: "))
people = int(input("How many people?: "))
print("per person Pay: ", Bill / people)

#8번 이름과 나이를 입력받되, 나이 +1 해서 출력하기
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name + " next birthday you will be", age + 1)

#9번 일수을 입력 받아 그떄까지 남은 시간, 분, 초 구하기
day = input("Day: ")
hours = day * 24
minutes = hours * 60
seconds = minutes * 60
print("In", day, "days there are...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

#10번 Kg -> 파운드 단위로 바꾸기
# 1kg = 2.204 파운드
weight = float(input("Enter your weight: "))
print("Return value: ", round(weight * 2.204, 4))

#11번 사용자 친화적인 문제에~?
input_num, num = map(int, input().split())
print("result:", input_num // num)
