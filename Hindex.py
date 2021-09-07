import os
os.system('cls')
import numpy as np
def solution(citations):
    citations = np.array(sorted(citations, reverse=True))
    for i in range(len(citations), -1 , -1) :
        if len(citations[citations>=i]) >= i and len(citations) - len(citations[citations>=i]) <= i :
            return i

#print(solution([0,0,0]))
#print(solution([0,1,2]))
#print(solution([12, 11, 10, 9, 8, 1]))
#print(solution([3, 0, 6, 1, 5]))