def swap_case(s):
    num = ''
    for i in s:
        if i == i.lower():
            num += i.upper()
        elif i == i.upper():
            num += i.lower()
    return num

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)