#assignment3
#q1

# exp=0
# add=0
# for i in range(3):
    
#     ovt=int(input("enter your value:"))
#     if(ovt>40):
#         exp=(ovt-40)*12
#         add=add+exp
# print("extpay=",add)      

# #q2  
# n=int(input("enter your number"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print(fact)    

# #q3
# n=int(input('enetr your number:'))
# pow=int(input('enter your pow number:'))
# result=1
# while(pow!=0):
#     result*=n
#     pow-=1
# print(result)

# #q5
# for i in range(1,500):
#     num=i
#     sum=0
#     while(i!=0):
#         rem=i%10
#         sum=sum+rem*rem*rem
#         i=i//10
#     if(num==sum):
#        print(num)  

#q6
# n=int(input("how many words words you find out:"))
# poss=0
# neg=0
# eql=0
# for i in range(n):
    
#     num=int(input("enter your numbers:"))
#     if(num>0):
#         poss+=1
#     elif(num==0):
#         eql+=1
#     else:
#         neg+=1  
# print("poss",poss)
# print("neg",neg)
# print("eql",eql)  

#9  
# print("gk")      
# for i in range(1,300+1):
#     j=2
#     falg=0
#     while(j<i):
#         if(i%j==0):
#             falg=1
#             break
#         j+=1
#     if(falg==0):
#         print(i)

#q10

x,y,z=map(int,input('enter ur value').split())
big=small=res=0
if(x>y and x>z):
    big=x
elif(y>x and y>z):
    big=y
else:
    big=z    

if(x<y and x<z):
    small=x          ###but i need modify this programing
elif(y<x and y<z):
    small=y
else:
    small=z        
res=big-small
print(res)
        
#q.12
# n=int(input('enter your no:'))
# fact=1
# res=0
# new_res=0
# for i in range(1,n+1):
#     fact=fact*i
#     res=i/fact
#     new_res+=res
# print(new_res)    


#q13
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if(i!=j and i!=k and j!=k):
#                 print(i,j,k,end='\n')

##############amstroong number###########################################
# for i in range(1,500):
#     j=i
#     sum=0
#     while(i!=0):
#         rem=i%10
#         sum=sum+rem*rem*rem
#         i=i//10
#     if(j==sum):
#         print(j)    


