import pickle as p 
fname="book.dat"
def create():
    f =open(fname,'wb')
    while True: 
        s=[]
        Bno=int(input("Enter the book number: "))
        s.append(Bno)
        Bname=input("Enter the book name: ")
        s.append(Bname)
        Author=input("Enter the author name: ")
        s.append(Author)
        price=int(input("Enter the price: "))
        s.append(price)
        p.dump(s,f)
        c=input("Do you want to continue?")
        if c.upper()=="N": 
            break 
    f.close()
    
def display(): 
    f = open(fname,'rb') 
    s=[]
    try: 
        while True: 
            s=p.load(f)
            print(s)
    except EOFError: 
        pass
    f.close()
    
def append(): 
    f = open(fname,'ab')
    if not f: 
        print("The file does not exist")
    else: 
        while True:
            s=[]
            Bno=int(input("Enter Book Number: "))
            s.append(Bno)
            Bname=input("Enter the book Name: ")
            s.append(Bname)
            Author=input("Enter the author name: ")
            s.append(Author)
            price=int(input("Enter the price:"))
            s.append(price)
            p.dump(s,f)
            c = input("Do you want to add more record?: ")
            if c.upper()=="N": 
                break 
    f.close()
    
def search(): 
    found=0 
    f=open(fname,"rb")
    if not f: 
        print("This file does not exist")
    else: 
        try: 
            while True: 
                s=[]
                s=p.load(f)
                if s[3]>100 and s[3]<500: 
                    print(s)
                    found=1 
        except EOFError: 
            pass
        if found==0: 
            print("The record does no exist")
    f.close() 
        
print("Creation of the file")
create()
while True: 
    print("1.To add records to the file") 
    print("2.To display the contents inside the file")
    print("3.Search for books whose price is in the range of 100 to 500") 
    print("4.Quit")
    c=int(input("Enter your choice: "))
    if c ==1: 
        append()
    elif c ==2: 
        display()
    elif c==3: 
        search()
    else: 
            break 
    ch=input("Do you want to continue the program?: ")
    if ch.upper()=="N": 
         break
