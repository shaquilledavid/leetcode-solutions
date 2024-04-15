def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(s) == 1:
        return d[s]

    total = 0
    i = 0
    j = 1
    while i < len(s):
        if (j < len(s)) and (((s[j] == 'V' or s[j] == 'X') and s[i] == 'I') or ((s[j] == 'L' or s[j] == 'C') and s[i] == 'X') or ((s[j] == 'D' or s[j] == 'M') and s[i] == 'C')):
            sub = d[s[j]] - d[s[i]]
            total += sub
            print(total)
            i += 2
            j += 2

        else:
            total += d[s[i]]
            print(total)
            i += 1
            j += 1
            
    return total
