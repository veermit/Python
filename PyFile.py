# W3School

""" 
Imported Libraries
to use modules of library
need to import from modules
"""
import os

""" 
Definition of main
function
"""
def main():
	print ("Inside main")
	FileOperation("Test.txt")

""" 
This function opens
file with the parameter name
"""
def FileOperation(FileName):
	from os import path

	# Cheking whether given parameter(file) is exists
	if path.exists(FileName) == True:
		FileDesc = open(FileName, "rt")
		print (FileDesc)
	else:
		FileDesc = open(FileName, "wt")
		print (FileDesc)

	# Cheking whether given parameter is file/Dir
	if path.isfile(FileName) == True:
		print ("Present parameter is File")
	else:
		print ("Present parameter is Directory")

	# Cheking whether given parameter(file) is exists and delete
	if path.exists(FileName) == True:
		os.remove(FileName)
		print ("File deleted")
	else:
		print ("File does not exists")


""" 
 This condition ensures 
 that the main fucntion 
 is exists
"""
if __name__ == "__main__":
	main()


"""
Note: 	
	Ensure that the main() (executable code), 
	shold be last line of the file

	All functions must be defiend before any executable code
""" 
