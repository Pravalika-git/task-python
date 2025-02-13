#   Arguments two types
# def sum(a,b):
#     print(2+3)
#     print(2-3)
#     print(2*3)
#     print(2/3) 
# sum(2,3)
# Method overload loading


# def sum(a,b,c):
#     return a+b+c

# def sum(a,b,c,d):
#     return a+b+c+d
# sum(2,4,5)
# sum(2,3,4,5)

#     print(2+3)
# sum(2,3)
    
# def sum(a,b,c,d):
# def sum(a,b,c,d):
#Abbitary argument ---  Random for a takes same remaning in all b in tuple data set because they are immuttable dont know how may agrument to give

def sum (a,*b):
   res=a
   for k in b :
         res =+ k
         return res
res=print(sum(2,3,4,5,6,7,8))

# def sum (**kargs) :
#     print(type(kargs))
#     res=0
#     for i,j in kargs .items():
#           res +=j
#           return res
# sum()
     

