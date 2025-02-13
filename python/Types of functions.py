# Tpes of function
#Function with return statement
# VOID --- no returnstatment
#Lambda functions ----single line, optimisation,anonmynms
#by assiging varible we call it
lam_example=lambda x , y,z : x+y+z 
print(lam_example(3,4,5  ))
lam =lambda :("Hellow world")
print(lam())
# mostly in higher argument
#map (fun,iterable)
def square(x):
    return x * x* x 

# def cube(x):
#     return  x * x * x * X

 
# def lambda2 (X):
#      return  x * x 
# res_map = map(lambda * , [1,2,3,4,5,6,])
# print(list(res_map))

res_map1 = map(square ,[1,2,3,4,5,6,7,8,9])
print(list(res_map1))

# res_map2 = map(cube ,[1,2,3,4,5,6,7,8,2,3,9,8])
# print(list(res_map2))


