def longXDv(dividend,divisor,appender='000'):
    for i in range((len(appender) + 1)):
        if i == 0:
            dividend = format(int(dividend,2) ^ int(divisor,2),'04b')
        else:
            dividend = list(dividend + appender[i-1])
            dividend.pop(0)
            dividend = ''.join(dividend)
            if(dividend[0] == '1'):
                dividend = format(int(dividend,2) ^ int(divisor,2),'04b')
            else:
                dividend = format((int(dividend,2) ^ 0b0000),'04b')
        if(i+1 == len(appender)+1):
            return dividend

def changeDividendLBit(dividend,val):
    temp = list(dividend)
    temp.pop()
    ldividend = ''.join(temp)
    ldividend = ldividend + val
    return ldividend
    
def main():
    dividend = input("Enter Dividend:- ")
    divisor = input("Enter Divisor:- ")
    rem = longXDv('0b'+dividend,'0b'+divisor)
    print(f"The remainder is:- {rem}\nThe Codeword is:- {dividend}{int(rem)}")
    syndrome = longXDv('0b'+dividend,'0b'+divisor,str(int(rem)))
    if(int(syndrome) == 0):
        print(f"\033[1;93mThe Syndrome is zero, hence the transmitted bits are error freeee...\033[0m")
        if(dividend[-1] == 0):
            updatedDividend = changeDividendLBit(dividend,'1')
        else:
            updatedDividend = changeDividendLBit(dividend,'0')
        print(f"For testing changing the last bit of dividend from {dividend} to {updatedDividend}, testing started :-")
        print('Test has errors' if int(longXDv('0b'+updatedDividend,'0b'+divisor,str(int(rem)))) != 0 else 'Test also dont have errors')
    else:
        print("The Syndrome is not zero, hence there is error in the transmitted bits!")

if __name__=="__main__":    
    main()
