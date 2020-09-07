##########################################################################################
#
#           Command Line Arguments
#
#   * Python Command line arguments are input parameters passed to the script when
#     executing them. Almost all programming language provide support for command line
#     arguments. Then we also have command line options to set some specific options for the
#     program.
#   * There are many options to read python command line arguments. The three most
#      
#   * common ones are:
#       1.Python sys.argv
#       2.Python getopt module
#       3.Python argparse module
#   
#   Python sys module
#       * Python sys module stores the command line arguments into a list, we can access it
#         using sys.argv.
#       * This is very useful and simple way to read command line arguments as String.
#       * argv is considered as array of vectors which contains command line arguments.
#       * As it is an array its index starts from 0.
#       * argv[0] contains name of our python application and actual command line arguments
#         starts from index 1.
#
##############################################################################################

#Consider below application which demonstrates concept of Command Line Arguments

#(Run the above application as :- python commad_line_arguments.py 10 11)


import sys

print("---Learn Python with Mr.Ahirrao---")

print("Demonstration of Command Line Arguments")

print("Application Name :"+sys.argv[0])

x=int(sys.argv[1])
y=int(sys.argv[2])

z=x+y;

print(z)

