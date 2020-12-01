# cuckoo algorithm
import Algorithm
import matplotlib.pyplot as plt

def meanPoint(x,val):
    mean=0
    for i in range(len(x)):
        mean= x[i]*val[i]
    
    mean = mean/sum(val)
    return mean

if __name__ == '__main__':
    n = 100
    Pa = 0.25
    iterNumb = 100
    

    CS  = Algorithm.cuckoo(n, Pa, iterNumb)
    #print(CS.LevyFlight([4, -2]))
    nests = CS.run()
     
     
    nestsPoints, nestsVal = zip(*nests)
    #print("vector of nests: ",nests)
    x,y = zip(*nestsPoints)
     
    print("Best point: ", nestsPoints[0], "  which value is: ", nestsVal[0])
    plt.plot(x,y, 'bo')
    plt.show()
 
    #print 1-Pa of all nests, without abandoned ones
    plt.plot(x[0:-25],y[0:-25], 'bo')
    plt.show()

    pass