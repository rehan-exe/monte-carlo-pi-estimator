#13th June 2026
import numpy as np
import math
import matplotlib.pyplot as plt
n=int(input("How many arbitrary points? ",)) #Part 1
t=np.linspace(0,2*math.pi,n)
x2=np.cos(t)
y2=np.sin(t)
x=np.random.uniform(-1,1,n) #Part 2 (a)
y=np.random.uniform(-1,1,n) #Part 2 (b)
ind=o=i=0
jhp=khp=0
while ind<len(x) and ind<len(y):
    if ((x[ind])**2 + (y[ind])**2)<=1: #Part 3
        i+=1 #Part 4
        if i==1:
            jhp+=1
            plt.scatter(x[ind],y[ind],color="blue",label="Points Inside the Circle") #Part 6
        else:
            jhp+=1
            plt.scatter(x[ind],y[ind],color="blue")
    else:
        o+=1
        if o==1:
            khp+=1
            plt.scatter(x[ind],y[ind],color="red",label="Points Outside the Circle")
        else:
            khp+=1
            plt.scatter(x[ind],y[ind],color="red") 
    ind+=1
print("Number of points inside the circle: ",jhp)
print("The number of points outside the circle: ",khp)
plt.plot([1,1],[1,-1], color="black",label="Square having side 2")
plt.plot([1,-1],[-1,-1],color="black")
plt.plot([-1,-1],[-1,1], color="black")
plt.plot([-1,1],[1,1],color="black")
plt.plot(x2,y2,color="green",label="Circle having radius 1")
plt.legend()
plt.grid()
plt.title("Monte Carlo Pi Estimator")
plt.axis("equal")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() #Part 6
print("Estimate of Pi is: ", 4*(i/n)) #Part 5
u=(input("Would you like to start an experiment of Monte Carlo estimation using numbers from 100->10^6 (Y/N)? ")).lower()
if u.lower()=="y":
    j=100
    kl=[]
    while j<=1000000:
        x=np.random.uniform(-1,1,j) 
        y=np.random.uniform(-1,1,j) 
        ind2=d=0
        while ind2<len(x) and ind2<len(y):
            if ((x[ind2])**2 + (y[ind2])**2)<=1:
                d+=1
            ind2+=1
        kl.append([j,4*(d/j)])
        j*=2 #Bonus 1
    j=1000000
    x=np.random.uniform(-1,1,j)
    y=np.random.uniform(-1,1,j)
    ind2=d=0
    while ind2<len(x) and ind2<len(y):
        if ((x[ind2])**2 + (y[ind2])**2)<=1:
            d+=1
        ind2+=1
    kl.append([j,4*(d/j)]) #Includes 1,000,000 as an arbitrary point random
    kpo=0
    p=0
    while p<len(kl):
        kpo+=1
        if p!=len(kl)-1:
            if kpo==1:
                plt.scatter(kl[p][0],kl[p][1],color="red",label="Pi Estimates")
                plt.plot([kl[p][0],kl[p+1][0]],[kl[p][1],kl[p+1][1]],color="black",linestyle="dotted")
            else:
                plt.scatter(kl[p][0],kl[p][1],color="red")
                plt.plot([kl[p][0],kl[p+1][0]],[kl[p][1],kl[p+1][1]],color="black",linestyle="dotted")
        elif p==len(kl)-1:
            plt.scatter(kl[p][0],kl[p][1],color="red")
            plt.plot([kl[p-1][0],kl[p][0]],[kl[p-1][1],kl[p][1]],color="black",linestyle="dotted")
        p+=1
    plt.axhline(y=math.pi,color="cyan",label="True Value of Pi (3.141592653585...)")
    plt.legend()
    plt.title("Monte Carlo Pi Estimate")
    plt.grid()
    plt.xscale("log")
    plt.ylabel("Pi Estimate")
    plt.xlabel("Number of arbitrary points")
    plt.title("Monte Carlo Increasing Arbitrary Random Point Pi Accuracy Scatter Plot")
    plt.show() #Bonus 2
else:
    print("Thank you for using this program :)")