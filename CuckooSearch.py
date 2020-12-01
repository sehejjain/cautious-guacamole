import random
import numpy as np
from numpy.random.mtrand import randint
from scipy.stats import multivariate_normal
import scipy.stats


class cuckoo:
    
    
    def __init__(self, populationSize, probability, iterations):
        self.nestNumb = populationSize
        self.Pa = probability
        self.iterNumb = iterations
        self.nests = []
        
    def f(self, x): #x = (x,y)
        mean = np.array([0,0])
        cov = np.array([[0.1,0 ], [0,0.1]])
        ans = multivariate_normal.pdf(x, mean, cov)
        return pow((pow((x[0] - 3), 2) +pow((x[1] - 4), 2)), 2)
                
        
    def generate(self):
        x =random.uniform(-10,10)
        y =random.uniform(-10,10)
        return [x,y]
    
    def LevyFlight(self, x):
        beta = 1.5 # Lambda (between 1 and 3)
        alpha = (random.uniform(-1,1)) #between -1 and 1
        x += scipy.stats.levy_stable.pdf(x, alpha, beta)

        return x
        
    def abandonWorst(self, nest):
        for i in range(len(nest)-int(self.Pa*len(nest)),len(nest)): # Pa of worst solutions
            buf = self.generate() #generate new nests
            val = self.f(buf)   #evaluate new nests
            nest[i] = [buf,val] #swap
        return nest
    
    def run(self):

        # generate random nests
        for i in range(self.nestNumb):
            buf = self.generate()
            self.nests.append((buf, self.f(buf)))
         #start iteration
        for step in range(self.iterNumb):
            if (step%50 == 0):
                print("iteration\t",step)
                
            i = randint(0,self.nestNumb) #chose random nest
            cuckoo = self.LevyFlight(self.nests[i][0]) #get random cuckoo and make him levy's flight
            Fcuckoo = self.f(cuckoo) #evaluate cuckoo
            
            jnest = randint(0,len(self.nests)) #nest chosen by cuckoo
            
            if(Fcuckoo > self.nests[jnest][1]):
                self.nests[jnest] = [cuckoo, Fcuckoo] #replace new solution
                

            self.nests.sort(key=lambda val: val[1], reverse=True) #best solutions at start of list
            self.nests = self.abandonWorst(self.nests)
            self.nests.sort(key=lambda val: val[1], reverse=True)
            
        return self.nests   