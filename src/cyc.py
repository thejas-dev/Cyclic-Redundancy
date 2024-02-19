def longXDv(dividend,divisor,length,appender='000'):
    tempDividend = dividend.split('0b')[1]
    tempDivisor = divisor.split('0b')[1]
    if(len(tempDividend) > len(tempDivisor)):
        appender = tempDividend[-int(len(tempDividend)-len(tempDivisor)):] + appender
        tempDividend = tempDividend[:-int(len(tempDividend)-len(tempDivisor))]
        dividend = '0b' + tempDividend

    for i in range((len(appender) + 1)):
        if i == 0:
            if(dividend.split('0b')[1][0] == '1'):
                dividend = format(int(dividend,2) ^ int(divisor,2),'0'+length+'b')
            else:
                dividend = format((int(dividend,2) ^ 0b0),'0'+length+'b')
        else:
            dividend = list(dividend + appender[i-1])
            dividend.pop(0)
            dividend = ''.join(dividend)
            if(dividend[0] == '1'):
                dividend = format(int(dividend,2) ^ int(divisor,2),'0'+length+'b')
            else:
                dividend = format((int(dividend,2) ^ 0b0),'0'+length+'b')
        # print(dividend)
        if(i+1 == len(appender)+1):
            if(len(dividend) > (int(length)-1)):
                return dividend[len(dividend) - (int(length)-1):]
            else:
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
    length = str(len(divisor))
    appender = ''
    rangel = len(dividend) + len(divisor) - 1 
    for k in range(rangel - len(dividend)):
        appender += '0'
    rem = longXDv('0b'+dividend,'0b'+divisor,length,appender)
    print(f"The Remainder is:- {rem}\nThe Codeword is:- {dividend}{rem}")
    changedCodeword = input("Enter codeword:- ")
    dividend2 = changedCodeword[:len(dividend)]
    rem2 = changedCodeword[len(dividend):]
    print(dividend2,rem2)
    syndrome = longXDv('0b'+dividend2,'0b'+divisor,length,str(rem2))
    print("The Syndrome is :- ",syndrome)
    if(int(syndrome) == 0):
        print(f"\033[1;93mThe Syndrome is zero, hence the transmitted bits are error freeee...\033[0m") 
    else:
        print(f"\033[1;93mThe Syndrome is not zero, hence there is error in the transmitted bits!\033[0m")

if __name__=="__main__":    
    main()
