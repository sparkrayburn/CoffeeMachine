test = input()
tests = int(test)
object = []

def functions(list):
    count = 0
    try:
        r = list[0] % list[1]
    except:
        print("-1")
    else:
        while r >1:
            r = r / list[2]

            if list[0] % list[1] % list[2] != 0:
                count -=\
                    1
                r= 1
            else:
                count += 1
        if list[0] < list[1]:
            count = -1
        elif list[0] == list[1]:
            count = 0
        print(count)



for _ in range(int(test)):
    inp = list(map(int, input().split()))
    object.append(inp)


i = 0
while tests >= 1:
    functions(object[i])
    i += 1
    tests -= 1












