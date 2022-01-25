print("\n-----------------------------------------------------")

print("LAMBDA OPERATION")

#to store a value without a variable call
print((lambda x:x*x)(5))

print("\n-----------------------------------------------------")


print((lambda u,v:u*u+v*v)(5,6))

print("\n-----------------------------------------------------")

#store in a variable
res=(lambda u,v:u*u+v*v)(5,6)
print(res)

print("\n-----------------------------------------------------")

#function in function
Temp=(lambda r,s:r*s(r))(5,(lambda x:x+x))
print(Temp)

print("\n-----------------------------------------------------")

#equation in lambda Function
#a2+bx+c

def q(t):
    return (lambda a,b,c:a*t*t+b*t+c)
re=q(2)
print(re(1,2,3))


print("\n-----------------------------------------------------")
