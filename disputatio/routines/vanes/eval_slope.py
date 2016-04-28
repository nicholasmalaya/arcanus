import numpy as np


def slope_func(x,y):
    tmp = 0.0

#
# code block
#
    tmp += 25.726409509885706 * x**0 * y**0
    print tmp
    tmp += -7.959002774480191 * x**0 * y**1
    print tmp
    tmp += -15.508167202030295 * x**0 * y**2
    print tmp
    tmp += 2.965402639113657 * x**0 * y**3
    print tmp
    tmp += 2.908979127634638 * x**0 * y**4
    print tmp
    tmp += -0.472590823195663 * x**0 * y**5
    print tmp
    tmp += 34.433271501999322 * x**1 * y**0
    print tmp
    tmp += -5.272449164192513 * x**1 * y**1
    print tmp
    tmp += -22.326487602085692 * x**1 * y**2
    print tmp
    tmp += 2.102507411190583 * x**1 * y**3
    print tmp
    tmp += 3.914198314742165 * x**1 * y**4
    print tmp
    tmp += -0.414792906597238 * x**1 * y**5
    print tmp
    tmp += 18.642522726102548 * x**2 * y**0
    print tmp
    tmp += -0.472154879795198 * x**2 * y**1
    print tmp
    tmp += -12.254352889020941 * x**2 * y**2
    print tmp
    tmp += 0.184571173718402 * x**2 * y**3
    print tmp
    tmp += 1.987885398263920 * x**2 * y**4
    print tmp
    tmp += -0.133536246179303 * x**2 * y**5
    print tmp
    tmp += 4.998330147251158 * x**3 * y**0
    print tmp
    tmp += 0.405313228278152 * x**3 * y**1
    print tmp
    tmp += -3.237761593593429 * x**3 * y**2
    print tmp
    tmp += -0.173496672310084 * x**3 * y**3
    print tmp
    tmp += 0.478992888127426 * x**3 * y**4
    print tmp
    tmp += -0.019284794711885 * x**3 * y**5
    print tmp
    tmp += 0.658962676868528 * x**4 * y**0
    print tmp
    tmp += 0.112796968137289 * x**4 * y**1
    print tmp
    tmp += -0.414470445248186 * x**4 * y**2
    print tmp
    tmp += -0.047912734297560 * x**4 * y**3
    print tmp
    tmp += 0.054948414261503 * x**4 * y**4
    print tmp
    tmp += -0.001201763731608 * x**4 * y**5
    print tmp
    tmp += 0.034118218498095 * x**5 * y**0
    print tmp
    tmp += 0.008461273235451 * x**5 * y**1
    print tmp
    tmp += -0.020661658530202 * x**5 * y**2
    print tmp
    tmp += -0.003578246014591 * x**5 * y**3
    print tmp
    tmp += 0.002403161687857 * x**5 * y**4
    print tmp
    tmp += -0.000024490557266 * x**5 * y**5
    print tmp


#
# end code block
#
    return tmp

def main():
    x = -5.5
    y = -3.5

    m = slope_func(x,y)
    print 'x,y: ',x,y,m

    theta = np.tan(m)
    print 'theta =', theta*180/np.pi
    dx = np.cos(theta)
    dy = np.sin(theta)
    print 'dx: ',dx
    print 'dy: ',dy
    print 'dy/dx: ',y/x
    
#
# execute
#
main()
