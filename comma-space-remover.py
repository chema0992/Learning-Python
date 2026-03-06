def commadel(inputs):
    return inputs.replace(",", "")

def spacingdel(inputs):
    return inputs.replace(" ", "")

print("쉼표&공백 제거기 ver 1.0")
while True:
    user_input = input("공백 or 쉼표 제거할 문자(종료는 -1): ")
    if user_input == '-1':
        break
    mode = input("공백, 쉼표 중 제거할 문자 특수 기호로 입력(둘 다는 아무 문자): ")
    if mode == ' ':
        output = spacingdel(user_input)
    elif mode == ',':
        output = commadel(user_input)
    else:
        output = commadel(user_input)
        output = spacingdel(output)
    print(output)
