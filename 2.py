def nonConsecutiveDigits(n):
    def contains_consecutive(n):
        n = str(n)
        current = n[0]
        for i in range(1,len(n)):
            if current == n[i] :
                return True
            else :
                current = n[i]
        return False
    j = n+1
    while(contains_consecutive(j)) :
        j+=1
    return j
