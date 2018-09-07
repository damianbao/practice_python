from random import randint, random
from time import time, localtime

times = ['0600', '0700', '0800', '0900', '1000', '1100', '1200', '1300', \
         '1400', '1500', '1600', '1700', '1800', '1900', '2000', '2100', \
         '2200', '2300', '0000', '0100', '0200', '0300', '0400', '0500']


temp = 23.45
humidity = 50


def stats_for_a_day (f, t, h):
    for hour in times[:13]:  #?
        t += random()/2
        h += randint (1,4)
        f.write("%4s\t%.2f\t%d\n" % (hour, t, h))
    for hour in times[13:]:
        t -= random()/2
        h -= randint (1,4)
        f.write("%4s\t%.2f\t%d\n" % (hour, t, h))

dir = 'datab/'


for day in range(14):
    f = open (dir + str(time()) + '.txt', 'w')
    stats_for_a_day (f, temp, humidity)
    f.close()
