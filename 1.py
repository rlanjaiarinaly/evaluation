from collections import defaultdict
def isValidHtml(html) :
    d = defaultdict(int)
    html =html.split('<')
    for a in html :
        if ">" in a and "/" not in a :
            d[a[:len(a)-1]] += 1
        elif ">" in a and "/" in a :
            d[a[1:len(a)-1]] -= 1
            if d[a[1:len(a)-1]] < 0 :
                return False
            
    for i,v in d.items():
        if v != 0 :
            return False
    return True 
