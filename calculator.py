
def szam_1():    
    try: 
        a = int(input("Adja meg az első számot:"))   
    except:
        print("Nem számot adott meg, kérem számot adjon meg!")
        return szam_1()
            
    
#b = int(input("Adja meg a második számot:"))
#m = input("Milyen műveletel szeretne végrehajtani? (+, -, *, /): ")

#print(m) 

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

def szam_1(a: int):
    a = int(input("Adja meg az első számot:"))

szam_1(a)