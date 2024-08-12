# try block: test a block of code for errors 
# except block: handle the error
# else block: execute code when there is no error
# finally block: execute code, regardless of the try and except blocks 



# Exception Handling - when an error occurs or (exception), Python will normally stop and generate an error message. 

# These exceptions can be handled using the 'try' statement:

""" try: # The try block will generate an exception R/T x is not defined - 
    print(x)
    
except:
    print('An exception occured') """
    
    # The try block raises an error with the x not being defined, the except block will be executed. *** Without the try block - the program will crash and raise an error. 
    


# Many Exceptions - define as many exception blocks as you want, wanting to exceutre a special block of code for a special kind of error. 

# Print one message if the try block raises a NameError and another for other errors: 

""" try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") """
  
  

# Else - define a block of code to be executed if no errors were raised. 

# The try block does not generate any error - 

""" try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") """
  
  

# Finally - if specified, will be executed regardless if the try block raises an error or not. 

""" try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") """
  
# Also useful to close objects and clean up resources - 

# Try to open and write to a file that is not writable:

""" try:
  f = open("./demofile.txt", "w") # Open the file in write mode. 
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") """

# The file is opened in write mode = allows you to write to it.
# If the file doesn't exist, it will be created. 
# If it already exists, it will be overwritten.