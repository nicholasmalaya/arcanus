#!/bin/py
#
# Integrate exodus II file in space
#
import sys
import glob 

#
# need vtk environment to read EXOII
#
try:
    import vtk 
except ImportError:
    sys.stderr.write("Error: Can't find the file 'vtk.py'...\n")
    sys.stderr.write("Did you invoke with pvpython?\n")
    sys.stderr.write("Is the paraview module loaded?\n")
    sys.exit(1)

# -----------------------------------------------#
#              Average Fields                    #
# -----------------------------------------------#
def average_fields(names, var):
    """ given list of filenames and var, generate average field """

    # open each file, and add the field data 
    # to our averaged array
    for name in names:
        d = vtk.vtkExodusIIReader() 
        d.SetFileName(name) 
        d.UpdateInformation() 
        
        d.SetPointResultArrayStatus(var,1) 
        d.Update() 
        
        blocks = d.GetOutput().GetNumberOfBlocks()
        data   = d.GetOutput()
        

        #
        # range to integrate over
        #
        height = 0.842820346355
        thresh = 0.004

        # open text file
        f = open('slices/'+var+'/'+name+'.txt', 'w')
        
        for j in xrange(blocks):
            blk = data.GetBlock(0).GetBlock(j)
            try:
                pts = blk.GetNumberOfPoints()
            except:
                ss='no data in this block'
            else:
                pt_data = blk.GetPointData().GetArray(var)
                if pt_data is None:
                    print 'Nada!'
                    print 'I cannot find the variable field: ', var
                    print 'Exiting...'
                    sys.exit(1)
                    
                for i in xrange(pts):
                    # gather x,y,z location
                    #z,y,x = blk.GetPoint(i)
                    x,y,z = blk.GetPoint(i)
                    
                    if(abs(z-height)<thresh):
                        # gather point scalar value
                        u = pt_data.GetValue(i)                     
                        f.write(str(x)+' , '+str(y)+' , '+str(u)+'\n')
                        
        # close file
        f.close()

    #
    # steady as she goes
    #
    return 0

# -----------------------------------------------#
#              Perform Radial Integration        #
# -----------------------------------------------#
def integrate(name, var):
    """ given filename and var, generate profile """
    d = vtk.vtkExodusIIReader() 
    d.SetFileName(name) 
    d.UpdateInformation() 

    print var
    d.SetPointResultArrayStatus(var,1) 
    d.Update() 
    
    blocks = d.GetOutput().GetNumberOfBlocks()
    data   = d.GetOutput()
    
    #
    # range to integrate over
    #
    height = 0.804380714893
    thresh = 0.004
    
    rmin = 0.0
    rmax = 1.0
    nr   = 10
    dr = (rmax-rmin)/nr

    #
    # print data.GetBlock(0).GetBlock(0).GetPointData().GetArray(var).GetValue(0)
    #
    
    for j in xrange(blocks):
        blk = data.GetBlock(0).GetBlock(j)
        try:
            pts = blk.GetNumberOfPoints()
        except:
            ss='no data in this block'
        else:
            # grabbing vtkDataArray
            pt_data  = blk.GetPointData().GetArray(var)
            pt_data2 = blk.GetPointData().GetArray(var)

            
            
            if pt_data is None:
                print 'Nada!'
                print 'I cannot find the variable field: ', var
                print 'Exiting...'
                sys.exit(1)

            for i in xrange(pts):
                # gather x,y,z location
                z,y,x = blk.GetPoint(i)

                # gather point scalar value
                #print dir(pt_data)
                u = pt_data.GetValue(i)
                print u

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
        #for n in names:
        #    print 'integrating fields...'
        #    integrate(n,var)
            
        #
        # average fields
        #
        print 'slicing fields...'
        average_fields(names,var)
            
        #
        # plot?
        #
        if plot == 1:
            print 'plotting results...'


#
#
# nick 
# 9/9/14
#
#
