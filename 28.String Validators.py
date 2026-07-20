if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = False
    for i in range (len(s)):
        if s[i].isalnum():
            alnum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            digit = True
        if s[i].islower():
            lower = True
        if s[i].isupper():
            upper = True
            
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
