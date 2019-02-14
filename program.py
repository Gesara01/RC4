#!/usr/bin/env python

def KSA(key):
    length = len(key)
    S = []
    j = 0

    for i in range(256):
        S.append(i)
        S[i] = i

    for i in range(256):
        j = (j + S[i] + key[i % length]) % 256
        S[i], S[j] = S[j], S[i]   
    return S

def PRGA(S, M):
    i = 0
    j = 0
    K = []
    l = 0
    length = len(M)
    
    for x in range(length+1):
        K.append(x)
    
    while l < len(M):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        temp = (S[i] + S[j]) % 256
        K[l] = S[temp]
        l += 1
    print(K)
    return K
        
def main():
    K = input()
    M = input()
    
    def convert_key(key):
        return [ord(c) for c in key]
    K = convert_key(K)
 
    M = convert_key(M)
    print(M)
    S = KSA(K)
    K = PRGA(S,M)
    
    E = []
    
    for i in range(len(M)):
        E.append(i)
    
    for i in range(len(M)):
        E[i] = K[i] ^ M[i]
    
    print(str.join("",("%02X" % i for i in E)))

    return 

if __name__ == "__main__":
    main()


    