def junta(l1, l2):
    if (len(l1) == 0):
        return l2
    if(len(l2) == 0 ):
        return l1
    
    maior_1 = l1[-1]
    maior_2 = l2[-1]

    if maior_1 > maior_2:
        return junta(l1[:-1], l2) + [maior_1]
    else:
        return junta(l1, l2[:-1]) + [maior_2]
    