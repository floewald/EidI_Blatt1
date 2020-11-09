def inputInteger(varName):
    var = int( input("Please Enter {}:\n".format(varName) ) )
    return var

def getDepature(x, y, minutes):
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
z = inputInteger("your flight time in minutes")

# task 3a.1
# hours depature
h_dep = 0
# minutes depature
m_dep = 0

# task 3a.2
# boadring time (in minutes)
t_board = 30
# hours boarding
h_board = 0
# minutes boarding
m_board = 0


# task 3a.1
h_dep, m_dep = getDepature(x, y, z)
# task 3a.2
h_board, m_board = getDepature(x, y, z + t_board)



print()
print("Time:                {:02d}:{:02d}".format(x,y) )
print("Flight duration:     {}".format(z) )
print("Depature:            {:02d}:{:02d}".format( h_dep, m_dep) )
print("Boarding:            {:02d}:{:02d}".format( h_board, m_board) )