#Sample 9
print("\n")

num = 246
def cal():
    global num
    print(num)
    print(num * 2)
    num +=2

cal()




def cal(num):
    #global num not needed
    print(num)
    print(num * 2)
    num +=2

cal(246)
