
a = int(input("Adja meg az első számot:"))
b = int(input("Adja meg a második számot:"))
m = input("Milyen műveletel szeretne végrehajtani? (+, -, *, /): ")

print(m) 

if m == "+":
    o = a + b
    print(f'A két szám összege: {o} ')
elif m == "-":
    o = a - b
    print(f'A két szám különbsége: {o} ')
elif m == "*":
    o = a * b
    print(f'A két szám szorzata: {o} ')
elif m == "/":
    o = a / b
    print(f'A két szám hányadosa: {o} ')  

