#11718

while True:
    try:
        s=input()
        print(s)
    except EOFError as e:
        break
