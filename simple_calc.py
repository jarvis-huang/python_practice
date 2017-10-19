import sys

def main(s):
    stk = []
    temp = 1
    while s:
        i_plus = s.find('+')
        i_mult = s.find('*')
        
        # mode: 0 (last number), 1 (next is plus), 2 (next is mult)
        if i_plus<0 and i_mult<0: # last number
            mode = 0
        elif i_mult<0 and i_plus>=0:
            mode = 1
        elif i_plus<0 and i_mult>=0:
            mode = 2
        elif i_plus<i_mult:
            mode = 1
        else:
            mode = 2
            
        if mode==0:
            stk.append(temp*int(s))
            break
        elif mode==1:
            stk.append(temp*int(s[:i_plus]))
            s = s[i_plus+1:]
            temp = 1
        else:
            temp *= int(s[:i_mult])
            s = s[i_mult+1:]
    
    print(sum(stk))
    
# Simple calculator with only additions and multiplications.
# Usage:
#   python simple_calc.py "1+2*3+4*5"
#   (answer 27)

if __name__=="__main__":
    main(sys.argv[1])
