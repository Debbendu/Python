
import math

def isLeapYear(x):
    if x%4==0 and x%100!=0 or x%400==0:
        return True
    else:
        return False
def degToRad(x):
    return x*3.1415926/180


file1 = open('Tavg.txt', 'r')
Lines = file1.readlines()
file1.close()
file2 = open('SolarRadiation.txt', 'w')
longlitude=Lines[0].split('\t')
latitude=Lines[1].split('\t')


file2.write('N\tN\tN\t')

for i in range(3,len(longlitude)):
    file2.write(longlitude[i])
    if(i!=(len(longlitude)-1)):
        file2.write('\t')


file2.write('Y\tM\tD\t')
for i in range(3,len(latitude)):
    file2.write(latitude[i])
    if(i!=(len(latitude)-1)):
        file2.write('\t')



for i in range(2,len(Lines)):
    ro=Lines[i].split('\t')
    day=int(ro[2])
    if(int(ro[1])>=2):
        day+=31
    if(int(ro[1])>=3):
        if(isLeapYear(int(ro[0]))):
            day+=29
        else :
            day+=28
    if(int(ro[1])>=4):
        day+=31
    if(int(ro[1])>=5):
        day+=30
    if(int(ro[1])>=6):
        day+=31
    if(int(ro[1])>=7):
        day+=30
    if(int(ro[1])>=8):
        day+=31
    if(int(ro[1])>=9):
        day+=31
    if(int(ro[1])>=10):
        day+=30
    if(int(ro[1])>=11):
        day+=31
    if(int(ro[1])>=12):
        day+=30
    file2.write(ro[0]+'\t'+ro[1]+'\t'+ro[2]+'\t')
    for j in range(3,len(latitude)):
        lat=float(latitude[j])
        phai=degToRad(lat)
        delta=.409*math.sin((2*3.1415926*day/365)-1.405)
        omega=math.acos(-math.tan(phai)*math.tan(delta))
        Dr=1+.033*math.cos(2*3.1415926*day/365)
        Ra=15.392*Dr*((omega*math.sin(phai)*math.sin(delta))+(math.cos(phai)*math.cos(delta)*math.sin(omega)))
        file2.write(str(Ra)+'\t')
    file2.write('\n')


    
    
    