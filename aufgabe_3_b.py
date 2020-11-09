def inputInteger(varName):
    var = int( input("Please Enter {}:\n".format(varName) ) )
    return var

def getGermanTime(x, y, minutes):
    """
    Input:  x - hours of atual time
            y - minutes of atual time
            minutes - minutes to count back
    Output: hh - hours of back counted depature
            mm - minutes of back counted depature
    """
    # hours depature or boarding
    hh = 0
    # minutes depature or boarding
    mm = 0
    # # hours to count back
    # hcb = 0
    # # minutes to count back
    # mcb = 0
    
    # hcb = minutes // 60
    # mcb = minutes % 60

    # if y > mcb:
    #     mm = y - mcb
    # else:
    #     mm = 60 - (mcb - y)
    #     hh = hh - 1

    # if x > hcb:
    #     hh = hh + x - hcb
    # else:
    #     hh = 24 + hh - (hcb - x)

    # return hh, mm
    mm = ( (60*x + y - minutes) %60 )
    hh = ( (60*x + y - minutes) //60 ) %24
    return hh, mm

# read actual time (x for the hours, y for the minutes)
# and the flight duration (z in minutes)
addString = " of the actual Time"
x = inputInteger("the Hours"+addString)
y = inputInteger("the Minutes"+addString)
z = 420

# task 3b
# hours depature
h_ger = 0
# minutes depature
m_ger = 0

# task 3b
h_ger, m_ger = getGermanTime(x, y, z)



print()
print("Approximatley arriving in Korea:  {:02d}:{:02d}".format(x,y) )
print("Time in Germany:                  {:02d}:{:02d}".format( h_ger, m_ger) )