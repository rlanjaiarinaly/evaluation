def pairProgramming(experiences,isMostExperienced) :
    m1,m2 = 0,1
    if isMostExperienced :
        for i in range(1,len(experiences)):
            if experiences[i] >= experiences[m1] :
                m2 = m1
                m1 = i
            elif experiences[i] > experiences[m2] :
                m2 = i
    else :
        for i in range(1,len(experiences)):
            if experiences[i] <= experiences[m1] :
                m2 = m1
                m1 = i
            elif experiences[i] < experiences[m2] :
                m2 = i
    return [m1,m2] if m1 < m2 else [m2,m1]
