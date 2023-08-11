def greeting():
    print("hello world")
    return

greeting()




def pack(uno, dos, tres):
    return(uno, dos, tres)

print(pack(1,2,3))

def eat_lunch(list):
    if len(list) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

eat_lunch(["chips","biscuit","cherries","turkey"])