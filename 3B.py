
print('Celcius\t\t Fahrenheit')

for temp in range(21):
    f = 9 / 5 * temp + 32
    print(temp,'\t\t','{:.0f}'.format(f))