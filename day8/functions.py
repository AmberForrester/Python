def f_to_c(f):
    return 5*(f-32)/9
    
f = int(input('Enter temperature in F: '))
c = f_to_c(f)
print(f'{round(c, 2)}C')

def inch_to_cms(inch):
    return inch * 2.54


n = int(input('Enter value in inches: '))

print(f'The corresponding value in cms is {inch_to_cms(n)}')