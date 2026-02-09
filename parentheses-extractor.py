version = '0.0.1'
print(f"괄호 안 값 추출기\nver {version}")

def test(Input):
    if '(' in Input:
        if ')' in Input:
            a = Input.find("(")
            b = Input.find(")")
            value = Input[(a + 1):b]
            return value
        else:
            raise ValueError("(가 있으면 )도 필요")
    else:
        raise ValueError("( 필요")

while True:
    user_input = input("Enter the Text\n")
    try:
        print(test(user_input))
    except ValueError as e:
        print(f"오류: {e}")
