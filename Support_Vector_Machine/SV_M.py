import sys
#warning append the directory where you have your data
#it is the machine where the author worked on specific 
sys.path.append("C:/Users/Ratul/Desktop/nadiabot") 

#from matplotlib import pyplot as plt

#import numpy as np

from CSV_Reader import *

#bunch of imports basically dependencies of this basic script 


def main(): 
	print("Hi machine learning from Python")
	file=input("CSV file from where the data needs to be read : ")
	Reader(file)
	



if __name__ == '__main__':
	main()
