def tens(num):
    #Formats num into a four digit number e.g. num = 1 -> n = 0001
    n = '{:04}'.format(num)
    if int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1])+int(list(str(n))[::-1][2])+int(list(str(n))[::-1][3]) == 0:
                return("zero")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 1:
        if int(list(str(n))[::-1][0]) == 1:
                return("one")
        if int(list(str(n))[::-1][1]) == 1:
                return("ten")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 2:
        if int(list(str(n))[::-1][0]) == 2:
                return("two")
        if int(list(str(n))[::-1][1]) == 2:
                return("twenty")
        if int(list(str(n))[::-1][1]) == 1:
                return("eleven")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 3:
        if int(list(str(n))[::-1][0]) == 3:
                return("three")
        if int(list(str(n))[::-1][0]) == 2:
                return("twelve")
        if int(list(str(n))[::-1][0]) == 1:
                return("twenty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("thirty")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 4:
        if int(list(str(n))[::-1][0]) == 4:
                return("four")
        if int(list(str(n))[::-1][0]) == 3:
                return("thirteen")
        if int(list(str(n))[::-1][0]) == 2:
                return("twenty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("thirty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("fourty")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 5:
        if int(list(str(n))[::-1][0]) == 5:
                return("five")
        if int(list(str(n))[::-1][0]) == 4:
                return("fourteen")
        if int(list(str(n))[::-1][0]) == 3:
                return("twenty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("thirty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("fourty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("fifty")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 6:
        if int(list(str(n))[::-1][0]) == 6:
                return("six")
        if int(list(str(n))[::-1][0]) == 5:
                return("fifteen")
        if int(list(str(n))[::-1][0]) == 4:
                return("twenty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("thirty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("forty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("fifty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("sixty")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 7:
        if int(list(str(n))[::-1][0]) == 7:
                return("seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("sixteen")
        if int(list(str(n))[::-1][0]) == 5:
                return("twenty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("thirty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("forty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("fifty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("sixty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("seventy")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 8:
        if int(list(str(n))[::-1][0]) == 8:
                return("eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("seventeen")
        if int(list(str(n))[::-1][0]) == 6:
                return("twenty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("thirty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("forty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("fifty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("sixty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("seventy one")
        if int(list(str(n))[::-1][0]) == 0:
                return("eighty")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 9:
        if int(list(str(n))[::-1][0]) == 9:
                return("nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("eighteen")
        if int(list(str(n))[::-1][0]) == 7:
                return("twenty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("thirty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("forty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("fifty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("sixty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("seventy two")
        if int(list(str(n))[::-1][0]) == 1:
                return("eighty one")
        if int(list(str(n))[::-1][0]) == 0:
                return("ninety")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 10:
        if int(list(str(n))[::-1][0]) == 9:
                return("nineteen")
        if int(list(str(n))[::-1][0]) == 8:
                return("twenty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("thirty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("forty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("fifty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("sixty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("seventy three")
        if int(list(str(n))[::-1][0]) == 2:
                return("eighty two")
        if int(list(str(n))[::-1][0]) == 1:
                return("ninety one")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 11:
        if int(list(str(n))[::-1][0]) == 9:
                return("twenty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("thirty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("forty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("fifty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("sixty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("seventy four")
        if int(list(str(n))[::-1][0]) == 3:
                return("eighty three")
        if int(list(str(n))[::-1][0]) == 2:
                return("ninety two")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 12:
        if int(list(str(n))[::-1][0]) == 9:
                return("thirty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("forty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("fifty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("sixty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("seventy five")
        if int(list(str(n))[::-1][0]) == 4:
                return("eighty four")
        if int(list(str(n))[::-1][0]) == 3:
                return("ninety three")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 13:
        if int(list(str(n))[::-1][0]) == 9:
                return("forty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("fifty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("sixty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("seventy six")
        if int(list(str(n))[::-1][0]) == 5:
                return("eighty five")
        if int(list(str(n))[::-1][0]) == 4:
                return("ninety four")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 14:
        if int(list(str(n))[::-1][0]) == 9:
                return("fifty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("sixty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("seventy seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("eighty six")
        if int(list(str(n))[::-1][0]) == 5:
                return("ninety five")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 15:
        if int(list(str(n))[::-1][0]) == 9:
                return("sixty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("seventy eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("eighty seven")
        if int(list(str(n))[::-1][0]) == 6:
                return("ninety six")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 16:
        if int(list(str(n))[::-1][0]) == 9:
                return("seventy nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("eighty eight")
        if int(list(str(n))[::-1][0]) == 7:
                return("ninety seven")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 17:
        if int(list(str(n))[::-1][0]) == 9:
                return("eighty nine")
        if int(list(str(n))[::-1][0]) == 8:
                return("ninety eight")
    elif int(list(str(n))[::-1][0])+int(list(str(n))[::-1][1]) == 18:
        if int(list(str(n))[::-1][0]) == 9:
                return("ninety nine")
            
def hundreds(num):
    if num < 100:
        return tens(num)
    else:
        n = '{:04}'.format(num)
        if int(list(str(n))[::-1][0]) + int(list(str(n))[::-1][1]) + int(list(str(n))[::-1][2]) == 1:
            return ("one hundred")
        if int(list(str(n))[::-1][0]) + int(list(str(n))[::-1][1]) + int(list(str(n))[::-1][2]) > 1:
            if int(list(str(n))[::-1][0]) + int(list(str(n))[::-1][1]) != 0:
                return (str(tens(int(''.join(str(num)[0]))))+" hundred and "+str(tens(int(''.join(list((str(num))[1:3:]))))))
            else:
                return (str(tens(int(''.join(str(num)[0]))))+" hundred")


def thousands(num):
    n = '{:04}'.format(num)
    if num < 1000:
        return(hundreds(num))
    else:
        n = '{:04}'.format(num)
        if int(list(str(n))[::-1][2])+int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) != 0:                
            if int(list(str(n))[::-1][2]+list(str(n))[::-1][1]+list(str(n))[::-1][0]) < 100:
                if int(list(str(n))[::-1][0]) !=0:
                    return (str(tens(int(''.join(str(num)[0]))))+" thousand and "+str(hundreds(int(''.join(list((str(num))[1:4:]))))))
                else:
                    return (str(tens(int(''.join(str(num)[0]))))+" thousand")
            else:
                return (str(tens(int(''.join(str(num)[0]))))+" thousand "+str(hundreds(int(''.join(list((str(num))[1:4:]))))))
        else:
            return (str(tens(int(''.join(str(num)[0]))))+" thousand")

def tenthousands(num):
    if num < 10000:
        return(thousands(num))
    else:
        n = '{:05}'.format(num)
        if int(list(str(n))[::-1][3])+int(list(str(n))[::-1][2])+int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) != 0:
            if int(list(str(n))[::-1][2]+list(str(n))[::-1][1]+list(str(n))[::-1][0]) < 100:
                if int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) !=0:
                    return (str(tens(int(''.join(str(num)[0:2]) )))+" thousand and "+str(hundreds(int(''.join(list((str(num))[2:5:]))))))
                else:
                    return (str(tens(int(''.join(str(num)[0:2]) )))+" thousand")
            else:
                return (str(tens(int(''.join(str(num)[0:2]))))+" thousand "+str(hundreds(int(''.join(list((str(num))[2:5:]))))))
        else:
            return (str(tens(int(''.join(str(num)[0:2]))))+" thousand")

def hundredthousands(num):
    if num < 100000:
        return(tenthousands(num))
    else:
        n = '{:06}'.format(num)
        if int(list(str(n))[::-1][4])+int(list(str(n))[::-1][3])+int(list(str(n))[::-1][2])+int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) != 0:
            if int(list(str(n))[::-1][3]+list(str(n))[::-1][2]+list(str(n))[::-1][1]+list(str(n))[::-1][0]) < 1000:
                if int(list(str(n))[::-1][2]+list(str(n))[::-1][1]+list(str(n))[::-1][0]) < 100:
                    if int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) !=0:
                        return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand and "+str(hundreds(int(''.join(list((str(num))[3:6:]))))))
                    else:
                        return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand")
                else:
                    return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand "+str(hundreds(int(''.join(list((str(num))[3:6:]))))))
            elif int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) !=0:
                return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand and "+str(thousands(int(''.join(list((str(num))[3:6:]))))))
            else:
                if int(list(str(n))[::-1][0]) !=0:
                    return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand "+str(thousands(int(''.join(list((str(num))[3:6:]))))))
                else:
                    return (str(hundreds(int(''.join(str(num)[0:3]) )))+" thousand ")
        else:
            return (str(hundreds(int(''.join(str(num)[0:3]))))+" thousand")

def millions(num):
    if num < 1000000:
        print(hundredthousands(num))
    else:
        n = '{:09}'.format(num)
        if int(list(str(n))[::-1][5])+int(list(str(n))[::-1][4])+int(list(str(n))[::-1][3])+int(list(str(n))[::-1][2])+int(list(str(n))[::-1][1])+int(list(str(n))[::-1][0]) != 0:
            print (str(hundreds(int(''.join(list((str(num))[0:1:]))))) + " million " + str(hundredthousands(int(''.join(list((str(num))[1:7:]))))))
        else:
            print(tens(int(''.join(list((str(num))[0:1:])))) + " million")


for x in range(10000000):
    millions(x)
    

