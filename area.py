def rectangle_area(a, b=None):
    if b==None:
        if a>0:
            return print(float(a*a*0.5))
        else:
            return print("Некорректный ввод данных")
    else:
        if a>0 and b>0:
            return print(float(a*b*0.5))
        else:
            return print("Некорректный ввод данных")
    
rectangle_area(10)
print()
rectangle_area(10,-5)
print()
rectangle_area(100,1)
print()
rectangle_area(1022,0)
print()
rectangle_area(14)
print()