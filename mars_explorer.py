# Completed Hackerrank Mars Exploration


def marsExploration(s): 
    count = 0
    n = 3
    out = [(s[i:i+n]) for i in range(0, len(s), n)] 
    for sos in out:
        if sos != "SOS":
            if sos[0] != "S":
                count +=1
            if sos[1] != "O":
                count +=1
            if sos[2] != "S":
                count +=1
    return count
