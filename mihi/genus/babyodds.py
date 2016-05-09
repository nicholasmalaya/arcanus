#
# Play prior Odds for baby
# ugh some horrible hacking here, dont hold this against me
#

from Tkinter import *

#
# odds calculator
#
odds=0.5
odds_history = []
odds_history.append(odds)

global mbet
global fbet

mbet=2.0
fbet=1.0

#
# ya ya, global variables are the devil...
#
#
boy_betters  = []
girl_betters = []
#boy_betters.append(("Nick",1-0.5))

#
# implements the gui that appears
#
class gui:

    label = None
    wg = None
    wb = None
    f = None

    def __init__(self, root):
        """Implements the graphical surface."""

        #
        #
        #
        self.root = root
        self.dir = []
        # Frame to contain the fields
        self.f = Frame(root) ; self.f.pack(side=TOP, fill=X)

        # show current odds
        root.wm_title("Welcome to the MALAYA BABY BETTING STATION")
        #titlestr ="Welcome to the MALAYA BABY BETTING STATION"
        #wt = Label(self.f, text=titlestr)
        #wt.pack()

        # show current odds
        titlestr ="Enter your NAME"
        wt = Label(self.f, text=titlestr)
        wt.pack()

        #
        # Text field for entry:
        #
        self.t1 = Text(self.f, width=40, height=1)
        self.t1.pack(side=TOP,expand=YES,fill=X)

        # show current odds
        titlestr ="Enter your BET (boy or girl below) "
        wt = Label(self.f, text=titlestr)
        wt.pack()

        self.t2 = Text(self.f, width=40, height=1)
        self.t2.pack(side=TOP,expand=YES,fill=X)

        # show current odds
        girlstr ="The current odds of a girl are "+str(odds)
        boystr ="The current odds of a boy  are "+str(1-odds)
        self.wg = Label(self.f, text=girlstr)
        self.wb = Label(self.f, text=boystr)
        self.wg.pack()
        self.wb.pack()


        from PIL import Image, ImageTk
        image = Image.open("boy.jpg")
        photo = ImageTk.PhotoImage(image)
        self.label = Label(image=photo)
        self.label.image = photo # keep a reference!
        self.label.pack()
                                  
        # Button
        self.button = Button(root, text = 'Register my Bet!', command = self.show_it )
        self.button.pack(side=TOP)

        return


    def calc_odds(self,bet):
        global mbet
        global fbet
        global odds

        '''update and log the odds'''
        if('boy' in bet):
            mbet=mbet+1.0
        else:
            fbet=fbet+1.0
            
        odds=float(fbet)/float(fbet+mbet)
        odds_history.append(odds)    
        return 0

    def summarize(self,boo):
        print 'BETTING HAS ENDED'

        if(boo == 1.0):
            print 'It is a boy! The winners are:'
            print 'BETTER --  ODDS'
            print ''
            print ''
            for winners in boy_betters:                
                print winners[0],winners[1]

            print 'The incorrect bets were:'
            for winners in girl_betters:                
                print winners[0], winners[1]

        else:
            print 'It is a girl! The winners are:'
            print 'BETTER --  ODDS'
            print ''
            print ''
            for winners in girl_betters:                
                print winners[0], winners[1]

            print 'The incorrect bets were:'
            for winners in boy_betters:                
                print winners[0], winners[1]

        #
        # lets do some data science!
        #
        import matplotlib.pyplot as plt
        plt.plot(odds_history)
        plt.title("DATA SCIENCE")
        plt.ylabel('Odds of a Girl')
        plt.xlabel('# of bets')
        plt.show()

        # teardown and exit succcessfully
        sys.exit(0)

        
    def show_it(self):
        
        # get whatever was entered and put it onto the screen
        name = self.t1.get('0.0',END)
        bet  = self.t2.get('0.0',END)
        
        if('END' in name):
            self.summarize(1.0)

        # some sanity checking... 
        if('boy' in bet or 'girl' in bet):
            print 'Your bet has been logged successfully!'
            # print the bet
            #print 'Name:',name
            #print 'Bet :',bet        

            if('boy' in bet):
                boy_betters.append((name,1-odds))
                #
                # display image
                #
                self.label.destroy()
                from PIL import Image, ImageTk
                image = Image.open("boy.jpg")
                photo = ImageTk.PhotoImage(image)
                self.label = Label(image=photo)
                self.label.image = photo # keep a reference!
                self.label.pack()

            else:
                girl_betters.append((name,odds))
                #
                # display image
                #
                self.label.destroy()
                from PIL import Image, ImageTk
                image = Image.open("girl.jpg")
                photo = ImageTk.PhotoImage(image)
                self.label = Label(image=photo)
                self.label.image = photo # keep a reference!
                self.label.pack()

            self.calc_odds(bet)
            # update current odds
            self.wg.destroy()
            self.wb.destroy()
            girlstr ="The current odds of a girl are "+str(odds)
            boystr ="The current odds of a boy  are "+str(1-odds)
            self.wg = Label(self.f, text=girlstr)
            self.wb = Label(self.f, text=boystr)
            self.wg.pack()
            self.wb.pack()

        else:
            print "error: bet must be 'boy' or 'girl'"
            print 'you entered', bet     
            print 'Your bet was not logged!!!!! '
            print 'Please re-enter your bet'

        # clear! 
        self.t1.delete('1.0', END)
        self.t2.delete('1.0', END)

        #self.root.destroy()
        #self.root.quit()
        
        return


if __name__ == '__main__':
    #
    #If run as stand alone ...
    #
    root = Tk()
    gui( root )
    mainloop()


#
# nick 
# 5/7/16
#
# https://mail.python.org/pipermail/tutor/2004-December/034349.html
#
