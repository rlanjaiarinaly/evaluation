from collections import defaultdict
import re
def isValidHtml(html) :
    d = defaultdict(int)
    htmlt =html.split('<')
    print(htmlt)
    for a in htmlt :
        if ">" in a and "/" not in a :
            d[a[:a.index(">")]] += 1
        elif ">" in a and "/" in a :
            d[a[1:len(a)-1]] -= 1
            if d[a[1:len(a)-1]] < 0 :
                return False

    for i,v in d.items():
        if v != 0 :
            return False
    r = re.search("<([a-z]+)>*<([a-z]+)>*</([a-z]+)>*</([a-z]+)>",html)
    if r is not None and (r.group(2) != r.group(3)) :
        return False
    return True
