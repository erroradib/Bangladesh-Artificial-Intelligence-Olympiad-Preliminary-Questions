# Adnan Adib

numWord = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

INPUT = int(input())



for x in range(INPUT):
    num1, operator, num2 = input().split()
    
    num1_value = numWord[num1]
    num2_value = numWord[num2]
    
    if operator == "plus":
        result = num1_value + num2_value
    else: 
        result = num1_value - num2_value
    
    result = max(0, min(result, 10))
    
    for key, value in numWord.items():
        if value == result:
            print(key)
            break
