import numpy as np
import matplotlib.pyplot as plt

def poly_print(c,name):
    #
    # prints coefficients for lift or drag functions
    #
    p=0
    print ''
    for item in c:
        # last step
        if(p == len(c)-1):
            print '        '+str(item)+'*x^'+str(p)+"'",
        # first step
        elif(p==0):
            print name +" = '"+str(item)+'*x^'+str(p)+" + "
            p=p+1
        # middle steps
        else:
            print '        '+str(item)+'*x^'+str(p)+" + "
            p=p+1
    print ''
    return 0

def reader(fl):
    #
    # reads a file and returns function values
    # 
    angle = []
    cd    = []
    
    # open
    fo = open(fl, "r")
    
    #
    # iterate
    #
    for line in fo:
        two_var = line.split()
        angle.append(float(two_var[0].split(',')[0]))
        cd.append(float(two_var[1]))
        
    # close
    fo.close()
    return angle, cd

# -----------------------
# plotting function
# -----------------------
    
def drag_polar(name):
    f1 = "cd_"+name+".dat"
    f2 = "cl_"+name+".dat"
    print f1,f2
    anglecd, cd = reader(f1)
    anglecl, cl = reader(f2)
    
    #
    # plot interpolated function
    #
    # theta := ((t+pi/2)%pi)-pi/2
    # lift = ' if ( abs ( theta )< pi / 24 , theta * 9 , sin ( 2 * theta ) ) '
    # drag = if(abs(theta)<pi/24,0.005+theta*theta*81/25, 1-0.8cos(2*theta))
    # 
    #rad = np.linspace(0.0, 360.0)
    #
    
    anglecd = -1 + 2*np.array(anglecd)/360.0
    anglecl = -1 + 2*np.array(anglecl)/360.0
    
    #
    # interpolate!
    # interp1d(x, y, kind='cubic')
    #
    #from scipy.interpolate import interp1d
    from numpy.polynomial import polynomial as P
    
    inter_cd,stat_cd = P.polyfit(anglecd, cd, 16,full=True)
    inter_cl,stat_cl = P.polyfit(anglecl, cl, 16,full=True)
    
    rad    = np.linspace(-0.99, 0.99)
    t      = (rad+np.pi)%np.pi - np.pi/2.0
    #anglei = (rad+1)*180.
    anglei = rad

    #cdi = np.cos(2 * np.pi * rad) * np.exp(-rad)
    #cli = np.cos(2 * np.pi * rad)
    
    #cli = np.where(abs(t) > np.pi/24., t, np.sin(2*t))
    #cdi = np.where(abs(t) > np.pi/24., t*t*81/25., 1-0.8*np.cos(2*t))
    
    poly_print(inter_cl,'lift')
    poly_print(inter_cd,'drag')
    
    #
    # plot!
    #
    sz=25
    plt.subplot(2, 1, 1)
    plt.plot(anglecd, cd, 'ko-',label='COMSOL Data')
    plt.plot(anglei, P.polyval(anglei,inter_cd), color='blue',label='Interpolant')
    #plt.title(r'Coefficients of Drag/Lift as functions of $\alpha$')
    #plt.subtitle(r'Coefficients of Drag/Lift as functions of $\alpha$')
    #plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$C_d$',size=sz)
    plt.legend()
    plt.xlim([-1,1])
    plt.ylim([-0.1,3.5])
    
    plt.subplot(2, 1, 2)
    plt.plot(anglecl, cl, 'ko-',label='COMSOL Data')
    plt.plot(anglei, P.polyval(anglei,inter_cl), color='blue',label='Interpolant')
    plt.ylabel(r'$C_l$',size=sz)
    plt.xlabel(r'$\alpha$',size=sz)
    plt.legend()
    plt.xlim([-1,1])
    plt.ylim([-3,3])
    plt.savefig(name+".png")
    plt.close()

# -----------------------
# main function
# -----------------------
#
def main():
    drag_polar('90')
    drag_polar('flat')
    drag_polar('semi')

# EXECUTE
# http://docs.scipy.org/doc/numpy/reference/routines.polynomials.poly1d.html
#
# grab original data
#
if __name__ == "__main__":
    main()

#
# nick
# 6/2/16
#
