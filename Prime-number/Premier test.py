import itertools


def divide_list(lst, n):
    return [list(i) for i in itertools.zip_longest(*[iter(lst)]*n, fillvalue=None)]

def algo_euclide(a, b):
    if b == 0:
        return a

    else:
        return algo_euclide(b, a % b)

def test_premier(n):
    for i in range(2,n):
        if n%i == 0 :
            return False
        


def est_premier(a,b):
    if(algo_euclide(a,b)==1):
        return True
    else:
        return False

def indicatrice_euler(n):
    indicatrice = 0
    i=1
    for i in range(n):
        if algo_euclide(i,n) == 1:
            indicatrice+=1

    print("indic :",indicatrice)


def inverse_mod(n,mod):
    for i in range(mod):        
        if((i*n)%mod ==1):
            return i

def ordre(a,n):
    for i in range(1,n):
        if((a**i)%n==1):
            return i


def test_shor(n):
    lfacteur = []
    for a in range(2,n):
        r=ordre(a,n)
        if(est_premier(a,n)):
            lfacteur.append(algo_euclide((a**(r/2))-1,n))
            lfacteur.append(algo_euclide((a**(r/2))+1,n))
            #print("d : ",algo_euclide((a**(r/2))-1,n),"  d' : ",algo_euclide((a**(r/2))+1,n))
    


    lfacteur = list(set(lfacteur))

    #del lfacteur[-1]
    
    lfacteur = [x for x in lfacteur if x > 1]
    
    lfacteur.remove(n)
    if not(lfacteur):
        print(n," est un nombre premier")
    else :            
        
        print("Les facteurs sont : ",lfacteur)            

      

def echant(n,e):
    l=[]
    echantillon=[]
    for i in range(0,n):
            if test_premier(i) != False:
                l.append(i)
    print("Il y a",len(l),"nombres premiers de 0 à",n)
    d_list = divide_list(l,5)
    print(d_list)

    




test_shor(72)

