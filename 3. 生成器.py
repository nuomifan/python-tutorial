import time


start = time.time()


mylist = (x for x in range(1000)) #生成器不占内存


print(type(mylist))


for i in mylist:
    print(i)
    
end = time.time()
a1 = end - start


start = time.time()


mylist = [x for x in range(1000)] #生成器不占内存


print(type(mylist))


for i in mylist:
    print(i)
    
end = time.time()

a2 = end - start