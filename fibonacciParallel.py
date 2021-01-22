""" Calculation of the first fibonacci number factored using Python. 
   :author: Ricardo Ortiz  <ricardo.ortiz@alumnos.ucn.cl>
   :version: 1.0"""  

# Dependencies
import pandas as pd
import numpy as np
import multiprocessing

# Method that calculates the fibonacci
def fibonacci(num):
    if num==1 or num == 2:

        return (1)

    else:

        return fibonacci(num-1)+fibonacci(num-2) 
 
# Function to calculate factorial
def factorize(num):
   if num==0 or num==1:

            result=1

   elif num>1:
            result=num*factorize(num-1)

   return result

#stores fibonacci numbers
array=[]

# List of elements on which you want to apply the function
result=[]
def app():
  for num in range(300):
    print("n:",num+1," finonacci =>",fibonacci(num+1)," finonacci factorize =>",factorize(fibonacci(num+1)))
    array.append(fibonacci(num+1))

  # Apply the function on each element in parallel
  pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
  result = pool.map(factorize, array)
  print (result)

# Run app    
app()

