from tkinter import * 
from tkinter import messagebox

score1 = 0
wickets = 0 
B1score = 0
B1balls = 0
B2score = 0 
B2balls = 0
totalballs = 0
totalovers = 0
over = 0
class Cricket:
   def __init__(self,root):
        self.root = root
        self.root.geometry('1270x880+0+0')
        self.root.config(bg="white")

#frame=1
        frame1 = Frame(self.root)
        frame1.place( x=210,y=20,width=770,height=50 )

#team label
        self.t_name=StringVar()
        self.t_name.set("India")
        self.teamlbl = Label(frame1,text="",textvariable=self.t_name,font=("",15,"bold"))
        self.teamlbl.pack(side="left",padx=(25,0))

#score label
        self.scr=StringVar()
        self.scr.set("0")
        self.scrlbl = Label(frame1,text="",textvariable=self.scr,font=("",15,"bold"))
        self.scrlbl.pack(side="left",padx=(20,0))

#Wicket label
        self.wkt=StringVar()
        self.wkt.set("- 0")
        self.wktlbl = Label(frame1,text="",textvariable=self.wkt,font=("",15,"bold"))
        self.wktlbl.pack(side="left")

#Over label
        self.over=StringVar()
        self.over.set("0")
        self.overlbl = Label(frame1,text="",textvariable=self.over,font=("",15,"bold"))
        self.overlbl.pack(side="left",padx=(25,0))


#balls label 
        self.balls=StringVar()
        self.balls.set(".0")
        self.ballslbl = Label(frame1,text="",textvariable=self.balls,font=("",15,"bold"))
        self.ballslbl.pack(side="left")
    
#Total overs label
        self.total_1over=StringVar()
        self.total_1over.set("/ 0")
        self.total_1overlbl = Label(frame1,text="",textvariable=self.total_1over,font=("",15,"bold"))
        self.total_1overlbl.pack(side="left")

#Batsman-1 label
        self.B1=StringVar()
        self.B1.set("Sujal")
        self.B1lbl = Label(frame1,text="",textvariable=self.B1,font=("",15,"bold"))
        self.B1lbl.pack(side="left",padx=(35,0))
        
        self.B1scr=StringVar()
        self.B1scr.set("0")
        self.B1scrlbl = Label(frame1,text="",textvariable=self.B1scr,font=("",15,"bold"))
        self.B1scrlbl.pack(side="left",padx=(5,0))
        
        self.B1balls=StringVar()
        self.B1balls.set("(0)")
        self.B1ballslbl = Label(frame1,text="",textvariable=self.B1balls,font=("",15,"bold"))
        self.B1ballslbl.pack(side="left")

#Batsman-1 label
        self.B2=StringVar()
        self.B2.set("Shrey")
        self.B2lbl = Label(frame1,text="",textvariable=self.B2,font=("",15,"bold"))
        self.B2lbl.pack(side="left",padx=(40,0))
        
        self.B2scr=StringVar()
        self.B2scr.set("0")
        self.B2scrlbl = Label(frame1,text="",textvariable=self.B2scr,font=("",15,"bold"))
        self.B2scrlbl.pack(side="left",padx=(5,0))
        
        self.B2balls=StringVar()
        self.B2balls.set("(0)")
        self.B2ballslbl = Label(frame1,text="",textvariable=self.B2balls,font=("",15,"bold"))
        self.B2ballslbl.pack(side="left")

#Frame-2 
        frame2 = Frame(self.root)
        frame2.place( x=210,y=100,width=770,height=300 )

        totalscorelbl = Label(frame2,text="ADD SCORE",font=("",13,"bold")).place(x=25,y=5)
        
        score1button = Button(frame2,text="+1",font=("",15,"bold"),command=self.scr1)
        score1button.place(x=5,y=40)

        score2button = Button(frame2,text="+2",font=("",15,"bold"),command=self.scr2)
        score2button.place(x=55,y=40)

        score3button = Button(frame2,text="+3",font=("",15,"bold"),command=self.scr3)
        score3button.place(x=105,y=40)

        score4button = Button(frame2,text="+4",font=("",15,"bold"),command=self.scr4)
        score4button.place(x=5,y=90)
        
        score5button = Button(frame2,text="+5",font=("",15,"bold"),command=self.scr5)
        score5button.place(x=55,y=90)
        
        score6button = Button(frame2,text="+6",font=("",15,"bold"),command=self.scr6)
        score6button.place(x=105,y=90)

        score7button = Button(frame2,text="-1",font=("",16,"bold"),command=self.scr7)
        score7button.place(x=55,y=140)

        score8button = Button(frame2,text="+0",font=("",16,"bold"),command=self.scr8)
        score8button.place(x=5,y=140)

        totalwicketlbl = Label(frame2,text="ADD WICKET",font=("",13,"bold")).place(x=25,y=200)

        wicket1button = Button(frame2,text="+1",font=("",15,"bold"),command=self.wickets1)
        wicket1button.place(x=5,y=235)

        wicket2button = Button(frame2,text="-1",font=("",16,"bold"),command=self.wickets2)
        wicket2button.place(x=105,y=235)

        totalB1runslbl = Label(frame2,text="ADD B1 SCORE",font=("",13,"bold")).place(x=210,y=5)
 
        totalB1runs1button = Button(frame2,text="+1",font=("",15,"bold"),command=self.B1score1)
        totalB1runs1button.place(x=200,y=40)

        totalB1runs2button = Button(frame2,text="+2",font=("",15,"bold"),command=self.B1score2)
        totalB1runs2button.place(x=250,y=40)

        totalB1runs3button = Button(frame2,text="+3",font=("",15,"bold"),command=self.B1score3)
        totalB1runs3button.place(x=300,y=40)

        totalB1runs4button = Button(frame2,text="+4",font=("",15,"bold"),command=self.B1score4)
        totalB1runs4button.place(x=200,y=90)

        totalB1runs5button = Button(frame2,text="+5",font=("",15,"bold"),command=self.B1score5)
        totalB1runs5button.place(x=250,y=90)
        
        totalB1runs6button = Button(frame2,text="+6",font=("",15,"bold"),command=self.B1score6)
        totalB1runs6button.place(x=300,y=90)
        
        totalB1runs7button = Button(frame2,text="+0",font=("",15,"bold"),command=self.B1score7)
        totalB1runs7button.place(x=200,y=140)
        
        totalB1runs8button = Button(frame2,text="-1",font=("",16,"bold"),command=self.B1score8)
        totalB1runs8button.place(x=250,y=140)

        totalB1runs9button = Button(frame2,text="0",font=("",16,"bold"),command=self.B1score9)
        totalB1runs9button.place(x=300,y=140)

        totalB1ballslbl = Label(frame2,text="B1 BALLS PLAYED",font=("",13,"bold")).place(x=200,y=200)

        totalB1balls1button = Button(frame2,text="-1",font=("",16,"bold"),command=self.B1balls2)
        totalB1balls1button.place(x=200,y=235)
        
        totalB1balls2button = Button(frame2,text="+1",font=("",15,"bold"),command=self.B1balls1)
        totalB1balls2button.place(x=300,y=235)

        totalB1balls3button = Button(frame2,text="0",font=("",16,"bold"),command=self.B1balls3)
        totalB1balls3button.place(x=250,y=235)

        

        totalB2runslbl = Label(frame2,text="ADD B2 BALLS",font=("",13,"bold")).place(x=410,y=5)

        totalB2runs1button = Button(frame2,text="+1",font=("",15,"bold"),command=self.B2score1)
        totalB2runs1button.place(x=400,y=40)

        totalB2runs2button = Button(frame2,text="+2",font=("",15,"bold"),command=self.B2score2)
        totalB2runs2button.place(x=450,y=40)

        totalB2runs3button = Button(frame2,text="+3",font=("",15,"bold"),command=self.B2score3)
        totalB2runs3button.place(x=500,y=40)

        totalB2runs4button = Button(frame2,text="+4",font=("",15,"bold"),command=self.B2score4)
        totalB2runs4button.place(x=400,y=90)

        totalB2runs5button = Button(frame2,text="+5",font=("",15,"bold"),command=self.B2score5)
        totalB2runs5button.place(x=450,y=90)
        
        totalB2runs6button = Button(frame2,text="+6",font=("",15,"bold"),command=self.B2score6)
        totalB2runs6button.place(x=500,y=90)
        
        totalB2runs7button = Button(frame2,text="+0",font=("",15,"bold"),command=self.B2score7)
        totalB2runs7button.place(x=400,y=140)
        
        totalB2runs8button = Button(frame2,text="-1",font=("",16,"bold"),command=self.B2score8)
        totalB2runs8button.place(x=450,y=140)

        totalB2runs9button = Button(frame2,text="0",font=("",16,"bold"),command=self.B2score9)
        totalB2runs9button.place(x=500,y=140)

        totalB2ballslbl = Label(frame2,text="B2 BALLS PLAYED",font=("",13,"bold")).place(x=400,y=200)

        totalB2balls1button = Button(frame2,text="-1",font=("",16,"bold"),command=self.B2balls2)
        totalB2balls1button.place(x=400,y=235)
        
        totalB2balls2button = Button(frame2,text="+1",font=("",15,"bold"),command=self.B2balls1)
        totalB2balls2button.place(x=500,y=235)

        totalB2balls3button = Button(frame2,text="0",font=("",16,"bold"),command=self.B2balls3)
        totalB2balls3button.place(x=450,y=235)

        totalballslbl = Label(frame2,text="ADD TOTAL BALLS",font=("",13,"bold")).place(x=600,y=5)

        totalballs1button = Button(frame2,text="+1",font=("",15,"bold"),command=self.totalballs1)
        totalballs1button.place(x=610,y=40)

        totalballs2button = Button(frame2,text="+0",font=("",15,"bold"),command=self.totalballs2)
        totalballs2button.place(x=710,y=40) 


#Frame 3
        frame3 = Frame(self.root)
        frame3.place( x=210,y=450,width=770,height=200 )  

        total_overlbl = Label(frame3,text="Enter Total overs",font=("",13,"bold")).place(x=10,y=20)
        self.total_overentry = Entry(frame3,font=("",10,"bold"))
        self.total_overentry.place(x=10,y=50)

        updateoverbutton = Button(frame3,text="Update",font=("",12,"bold"),command=self.update_total_over)
        updateoverbutton.place(x=40,y=100)

        Batsman1Namelbl = Label(frame3,text="Enter Batsman-1",font=("",13,"bold")).place(x=220,y=20)
        self.Batsman1entry = Entry(frame3,font=("",10,"bold"))
        self.Batsman1entry.place(x=220,y=50)

        updateBatsman1button = Button(frame3,text="Update",font=("",12,"bold"),command=self.update_B1_name)
        updateBatsman1button.place(x=260,y=100)

        Batsman2Namelbl = Label(frame3,text="Enter Batsman-2",font=("",13,"bold")).place(x=410,y=20)
        self.Batsman2entry = Entry(frame3,font=("",10,"bold"))
        self.Batsman2entry.place(x=410,y=50)

        updateBatsman2button = Button(frame3,text="Update",font=("",12,"bold"),command=self.update_B2_name)
        updateBatsman2button.place(x=440,y=100)

        TeamNamelbl = Label(frame3,text="Enter Captain name",font=("",13,"bold")).place(x=600,y=20)
        self.Teamnameentry = Entry(frame3,font=("",10,"bold"))
        self.Teamnameentry.place(x=610,y=50)

        updateTeamnamebutton = Button(frame3,text="Update",font=("",12,"bold"),command=self.update_captain)
        updateTeamnamebutton.place(x=640,y=100)

   def scr1(self):
       global score1
       score1 += 1
       self.scr.set(score1)

   def scr2(self):
       global score1
       score1 += 2
       self.scr.set(score1)

   def scr3(self):
       global score1
       score1 += 3
       self.scr.set(score1)

   def scr4(self):
       global score1
       score1 += 4
       self.scr.set(score1)

   def scr5(self):
       global score1
       score1 += 5
       self.scr.set(score1)

   def scr6(self):
       global score1
       score1 += 6
       self.scr.set(score1)

   def scr7(self):
       global score1
       score1 -= 1
       self.scr.set(score1)

   def scr8(self):
       global score1
       score1 += 0
       self.scr.set(score1)

   def wickets1(self):
       global wickets
       wickets += 1
       self.wkt.set(f"- {wickets}")
       if (wickets==10):
           self.wkt.set("- 0")

   def wickets2(self):
       global wickets
       wickets -= 1
       self.wkt.set(f"- {wickets}")

   def B1score1(self):
       global B1score
       B1score += 1
       self.B1scr.set(B1score)

   def B1score2(self):
       global B1score
       B1score += 2
       self.B1scr.set(B1score)

   def B1score3(self):
       global B1score
       B1score += 3
       self.B1scr.set(B1score)

   def B1score4(self):
       global B1score
       B1score += 4
       self.B1scr.set(B1score)

   def B1score5(self):
       global B1score
       B1score += 5
       self.B1scr.set(B1score)

   def B1score6(self):
       global B1score
       B1score += 6
       self.B1scr.set(B1score)

   def B1score7(self):
       global B1score
       B1score += 0
       self.B1scr.set(B1score)

   def B1score8(self):
       global B1score
       B1score -= 1
       self.B1scr.set(B1score)

   def B1score9(self):
       global B1score
       self.B1scr.set("0")

   def B1balls1(self):
       global B1balls
       B1balls += 1
       self.B1balls.set(f"({B1balls})")

   def B1balls2(self):
       global B1balls
       B1balls -= 1
       self.B1balls.set(f"({B1balls})")

   def B1balls3(self):
       global B1balls
       self.B1balls.set("(0)")

   def B2score1(self):
       global B2score
       B2score += 1
       self.B2scr.set(B2score)

   def B2score2(self):
       global B2score
       B2score += 2
       self.B2scr.set(B2score)

   def B2score3(self):
       global B2score
       B2score += 3
       self.B2scr.set(B2score)

   def B2score4(self):
       global B2score
       B2score += 4
       self.B2scr.set(B2score)

   def B2score5(self):
       global B2score
       B2score += 5
       self.B2scr.set(B2score)

   def B2score6(self):
       global B2score
       B2score += 6
       self.B2scr.set(B2score)

   def B2score7(self):
       global B2score
       B2score += 0
       self.B2scr.set(B2score)

   def B2score8(self):
       global B2score
       B2score -= 1
       self.B2scr.set(B2score)

   def B2score9(self):
       global B2score
       self.B2scr.set("0")

   def B2balls1(self):
       global B2balls
       B2balls += 1
       self.B2balls.set(f"({B2balls})")

                
   def B2balls2(self):
       global B2balls
       B2balls -= 1
       self.B2balls.set(f"({B2balls})")

   def B2balls3(self):
       global B2balls
       self.B2balls.set("(0)")

   def totalballs1(self):
       global totalballs, over
       totalballs += 1
       self.balls.set(f". {totalballs}")
       if totalballs>5:
                self.balls.set(".0")
                totalballs =0
                over += 1
                self.over.set(over)
           

   def totalballs2(self):
       global totalballs
       totalballs += 0
       self.balls.set(f". {totalballs}")


   def update_total_over(self): 
       a = self.total_overentry.get()
       self.total_1over.set(f"/ {a}")
       self.total_overentry.delete(0,'end')


   def update_B1_name(self):
       b= self.Batsman1entry.get()
       self.B1.set(f"{b}")

   def update_B2_name(self):
       b= self.Batsman2entry.get()
       self.B2.set(f"{b}")

   def update_captain(self):
       c = self.Teamnameentry.get()
       d = c.upper()
       self.t_name.set(d)

if __name__ == "__main__":
    root = Tk()
    app = Cricket(root)
    root.mainloop()
