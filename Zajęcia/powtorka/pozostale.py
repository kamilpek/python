## zadanie 3

re.compile(r'(\w+)(\w+)\2\1').search('abbabaaba').group(0,1,2)     
    
re.compile("(a(b)c)d").match("abcd").group(0,1,2)     
    
re.compile(r'(a(b)c)\1d\2').match("abcabcdb").group(0,1,2)     
    
re.compile("[ab]*[ba]{1,3}").match("bababb").group(0) 

## zadanie 5

(0 and (lambda x:x+1) or (lambda x:x-1)) (0)

