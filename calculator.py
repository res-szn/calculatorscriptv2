#THIS IS A BASE SMALL CALCULATOR SCRIPT

first=float(input('Enter First Number>'))
sec=float(input('Enter Second Number'))
opr=str(input("Enter Operation(+,-,x,/)>"))

if opr == "+":
    total =first + sec 
elif opr == "x":
    total=first*sec
elif opr=='-':
    total=first-sec
elif opr== "/":
    total=first/sec
else:
    total=('Error,Please enter a valid statement.')
print (total)