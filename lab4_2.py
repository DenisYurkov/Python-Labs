import random
import matplotlib.pyplot as ppt

def lab4_2():
    x = [i for i in range(1, 11)]
    y = []
    lst=[]
    
    n = 0
    while n!=10000:
        lst.append(random.randint(1, 10))
        n+=1
    
    for _ in x:
        y.append(lst.count(_))
    
    ppt.bar(x, y, label="Resut", color="#993300")
    ppt.show()
    
lab4_2()