# variable
age = int(input('Please, enter the age: '))

# add 4 statements and print who is a person
if age <= 1:            # 1 year old or less
    print('infant')         
elif age < 13:          # older 1, but younger than 13
    print('child')
elif age < 20:          # at least 13, but less than 20
    print('teenager')
else:
    print('adult')      # at least 20