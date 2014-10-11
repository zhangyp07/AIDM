# -*- coding: utf-8 -*-

import numpy.random as rd
import numpy as np

def jsim(s1, s2):
    sum = s1.union(s2)
    com = s1.intersection(s2)
    return float(len(com))/float(len(sum))
    
def minhash1(S, k, seed):
    word = []    
    for item in S:
        w = list(item)
        word.extend(w)
    wd = set(word)
    word = list(wd)
    
    rd.seed(seed)
    pm = []    
    for i in range(k):    
        tmp = rd.permutation(range(len(word)))
        pm.append(list(tmp))
    
    sig = []     #set the initial value len(S) for the signiture matrix.
    
    for var in range(k):
        sigtmp = [len(word)] * len(S)   #for each permutation(hash function) generate a row of Signitures matrix, then append to the sig
        for i in range(len(word)):   
            for j in range(len(S)):
                if word[i] in S[j]:
                    if pm[var][i] < sigtmp[j]:
                        sigtmp[j] = pm[var][i]
        sig.append(sigtmp)
            
    return {'Word': word, 'Signitures': sig}
    
def minhash2(S, k, seed):
    word = []    
    for item in S:
        w = list(item)
        word.extend(w)
    wd = set(word)
    word = list(wd)
    
    rd.seed(seed)
    a = rd.randint(1, k, k)     #hash(x) = a*x + b mod k
    a = list(a)
    b = rd.randint(1, k, k)
    b = list(b)    
    pm = []    
    for i in range(k):    
        tmp = [(a[i]*x+b[i])%k for x in range(k)]
        pm.append(list(tmp))
    
    sig = []     #set the initial value len(S) for the signiture matrix.
    
    for var in range(k):
        sigtmp = [len(word)] * len(S)   #for each permutation(hash function) generate a row of Signitures matrix, then append to the sig
        for i in range(len(word)):   
            for j in range(len(S)):
                if word[i] in S[j]:
                    if pm[var][i] < sigtmp[j]:
                        sigtmp[j] = pm[var][i]
        sig.append(sigtmp)
            
    return {'Word': word, 'Signitures': sig}
    
def sigsim(ss1, ss2):
    same = 0
    for i in range(len(ss1)):
        if ss1[i] == ss2[i]:
            same = same + 1
    return float(same)/float(len(ss1))
    
def simmat(Sig):
    M = np.zeros([len(Sig), len(Sig)])
    for i in range(len(Sig[0])):
        for j in range(len(Sig[0])):
            M[i,j] = sigsim(Sig[:,i], Sig[:,j])
    return M
      
def hashvector(vector):
    hs = 0
    for i in range(len(vector)):
        hs = hs + vector[i] * (10 ** i)
    return hs
    
