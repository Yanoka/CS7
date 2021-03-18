again ='yes'

while again.lower() =='yes':
    num1= int(input('Plese, enter first number: '))
    num2 = int(input('Plese, enter second number: '))
    sum = num1+num2
    print ('sum of', num1,'and', num2,'=', sum)
    again =input("Do you want to repeat(yes/no): ")

