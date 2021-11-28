#membuat function random string 'aku':

import random

def shuffleString(x, n):
    i = 0
    a = []
    
    while i < n :
        b = ''.join(random.sample(x, len(x)))
        if (b not in a):
            a += [b]
            i += 1            
    print(a)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
