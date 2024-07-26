fname = "Sadeed"
substring = fname[0:3]
print(substring)

print(fname[0])

print(fname[-4:-1])
print(fname[1:4])
print(fname[:4])
print(fname[1:])

# Apply String Functions - 
print(len(fname))

print(fname.endswith("eed"))

print(fname.startswith("s"))

fname = "amber"
print(fname.capitalize())

print(fname.upper())

# Escape Character - allows you to use double quotes when you normally would not be allowed. 

txt = "Hello\nWorld!"
print(txt) 

mymsg = "Welcome to CBC!\nI hope you are having a nice day!"
print(mymsg)

#String Interpolation

myName = input('Enter your name: ')
mymsg2 = f'Welcome {myName}!'
print(mymsg2)

print(mymsg2.find('Welcome'))