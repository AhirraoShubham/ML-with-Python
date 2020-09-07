##########################################################################
#    Variabels in Python
#
# * Variables are used to store information to be referenced and 
#   manipulated in computer program. They also provide a way of labeling
#   data with a decriptive name, so our progams can be understood more 
#   clearly by the reader and ourselves.
# * It is helpful to think of variables as containers that hold information
# * Their sole purpose is to label and store data in memory. This data can
#   can then be used throughout our program
# * As Python is Dynamically typed language there is no need to use 
#   data types explicitly while creating the variable.
# * Depends on the value that we initialise interpreter decides its data
#   type and allocates memory accordingly. 
#
############################################################################

# Consider below application which demonstrate different ways in which we 
#      can create variabels.

print("--- (-: Learn Python with Mr.Ahirrao :-) ---")

print("Demonstration of variable in Python")

no = 11                 # Considered as Integer

name = "Mr.Ahirrao"       # Considered as String 

fValue = 3.14           # Considered as Float   

cValue = 10+5j          # Considered as Complex number

eValue = 7E4            # Considered as Scintific number where E indicates power of 10

bigValue = 123456789    

print(no)

print("String is "+name)

print(fValue)

print(cValue)

print(eValue)

print(bigValue)

#We can use type function to get data type of variable

print("--- Get DataType of any variable using type funcation ---")

print(type(no))

print(type(name))

print(type(fValue))

print(type(cValue))

print(type(eValue))

print(type(bigValue))


#Save and run file for output