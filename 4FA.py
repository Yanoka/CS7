# MAXIMUM OF TWO VALUES
def main ():
    num1 = int(input ('Please, enter first number\n'))
    num2 = int(input ('Please, enter second number\n'))

    if num1 > num2:
        print(num1, 'is maximum value')
    elif num1 < num2:
        print(num2, 'is maximum value')
    else:
        print ('The numbers are equal')
   
main()