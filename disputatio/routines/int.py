#!/bin/py
#
# Integrate exodus II file in space
#
import sys
import numpy as np
import glob 
import vtk 

# -----------------------------------------------#
#              Perform Radial Integration        #
# -----------------------------------------------#
def integrate(name, var):
    """ given filename and var, generate profile """
    d = vtk.vtkExodusIIReader() 
    d.SetFileName(name) 
    d.UpdateInformation() 
    
    d.SetPointResultArrayStatus(var,1) 
    d.Update() 
    
    blocks = d.GetOutput().GetNumberOfBlocks()
    data   = d.GetOutput()
    
    # range to integrate at
    height = 0.804380714893
    thresh = 0.004
    
    rmin = 0.0
    rmax = 1.0
    nr   = 10
    dr = (rmax-rmin)/nr
    rint = np.zeros(nr)
    rn   = np.ones(nr)

    for j in xrange(blocks):
        blk = data.GetBlock(0).GetBlock(j)
        pts    = blk.GetNumberOfPoints()
        pt_data = blk.GetPointData().GetArray(var)

        for i in xrange(pts):
            # gather x,y,z location
            z,y,x = blk.GetPoint(i)

            # gather point scalar value
            u = pt_data.GetValue(i)

            # now, find all values near the target height
            # (convert to cylindrical)
            if(abs(z - height) < thresh):
                r  = np.sqrt((x)**2 + (y)**2)
                fr = np.floor(r/dr)
                rint[fr] += u
                rn  [fr] += 1
    return rint/rn


# -----------------------------------------------#
#  Inform user precisely what we are capable of. #
# -----------------------------------------------#
def help_msg():
            print 'usage: python int.py command list'
            print 'commands:'
            print '         -l: list of files'
            print '         -f: single file'
            print '         -a: all exodus files in pwd'
            print '         --var={T,u,v,w,P}: set variable'
            print '         --plot: plots results' 
            sys.exit(0)


# -----------------------------------------------#
#              Main Function                     #
# -----------------------------------------------#
if __name__ == "__main__":
    """ When invoked from command line """

    # -----------------------------------------------#
    #              Input Parsing                     #
    # -----------------------------------------------#
    #
    # see if user needs help
    # 
    if(len(sys.argv) <= 1): 
        help_msg()        
    else:        

        #
        # find if --var is present in list
        # then, save data and delete
        #
        if ('--var' in str(sys.argv)):
            vart = [x for x in sys.argv if '--var=' in x]
            var  = str(vart[0])[6:]
            print 'Setting parameter to: ', var
            
            # now, find and delete all --var elements
            for i in sys.argv:
                if '--var' in str(i):
                    sys.argv.remove(i)                   
        else:
            print 'No parameter given, defaulting to W'
            var   = "w"
                   

        #
        # set plot?
        #
        plot=0
        for i in sys.argv:
            if '--plot' in str(i):
                plot=1
                sys.argv.remove(i)                   


        #
        # provide help
        #
        if ('-h' in str(sys.argv[1]) or '--help' in str(sys.argv[1]) ):
            help_msg()
        

        #
        # iterate over list of files
        #
        if ('-l' in str(sys.argv[1])):
            names=[]
            for i in xrange(2,len(sys.argv)):
                names.append(sys.argv[i])

            if not names:
                print 'No files given!'
                print 'Exiting...'
                sys.exit(0)

        #
        # single file
        #
        if ('-f' in str(sys.argv[1])):
            names=[str(sys.argv[2])]


        #
        # all files in pwd
        #
        if ('-a' in str(sys.argv[1])):
            names = sorted(glob.glob("*.exo"))
            if not names:
                print 'No exodusII files detected!'
                print 'Exiting...'
                sys.exit(0)

        # -----------------------------------------------#
        #     Finished Input Parsing                     #
        # -----------------------------------------------#
        #
        # iterate + integrate over files
        #    
        for n in names:
            print 'integrating fields...'
            #integrate(n,var)
            
        #
        # plot?
        #
        if plot == 1:
            print 'plotting results...'
