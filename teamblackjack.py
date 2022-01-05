import random
from tkinter import *
from tkinter import messagebox 

class Login(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.photo = PhotoImage(file="bg2.gif")
        self.loginphoto = PhotoImage(file="login.gif")
        self.gamephoto = PhotoImage(file="gamestart2.gif")
        self.gamephoto2 = PhotoImage(file="gamecant.gif")
        self.master=master
        self.memebers=self.load_members()
        self.create_widget()

    def create_widget(self):
        """creates widgets for Login"""
        self.label = Label(self, image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=0,column=0,columnspan=20,rowspan=20)
        # Label(self,text='Enter your name ').grid(row=0,column=0,columnspan=20,rowspan=20)
        self.entry=Entry(self,width=15,font=20)
        self.entry.grid(row=1,column=0,columnspan=20,rowspan=30)
        self.loginbutton = Button(self,text="Login",width=100,height=30,image=self.loginphoto, command=self.login).grid(row=6,column=0,columnspan=20,rowspan=30)
    def load_members(self):
        """loads members for blackjack"""
        file=open('members.txt','r')
        self.members={}
        for line in file:
            self.name, self.tries, self.wins, self.chips=line.strip('\n').split(',')
            self.members[self.name]=(int(self.tries),float(self.wins),int(self.chips))
        file.close()
        return self.members

    def yourname(self):
        """gets player's name"""
        return self.entry.get()

    def login(self):
        """checks existing/new player and returns summary of player"""
        self.name=self.yourname()
        if self.name in self.memebers.keys():
            (self.tries,self.wins,self.chips)=self.members[self.name]
            summary="Welcome, "+self.name+'!'+'\n'
            summary="-Your Status-"+'\n'
            summary+="Tries : "+str(self.tries)+" games"+'\n'
            summary+="Wins : "+str(int(self.wins))+" games"+'\n'
            summary+="Loses : "+str(int(self.tries - self.wins))+" games"+'\n'
            self.winrate=100*self.wins/self.tries if self.tries>0 else 0
            summary+="Winrate : "+str(round(self.winrate,1))+' %'+'\n'
            summary+="Chips : "+str(self.chips)+ ' chip(s)'
            Label(self, text=summary,font=15).grid(row=1,column=14,columnspan=20,rowspan=30)
            # summary="Welcome, "+self.name+'!'+'\n'
            # summary+="You played "+str(self.tries)+" games and won "+str(self.wins)+' of them'+'\n'
            # self.winrate=100*self.wins/self.tries if self.tries>0 else 0
            # summary+="Your all-time winning rate is "+str(round(self.winrate,1))+' %'+'\n'
            # summary+='You have ' +str(self.chips)+ ' chips.'
            # Label(self, text=summary).grid(row=1,column=14,columnspan=20,rowspan=30)
            if self.chips == 0:
                Button(self,text="Start The Game",image=self.gamephoto2,command=self.cantstart,width=160,height=30).grid(row=9,column=14,columnspan=20,rowspan=30)
            else:
                Button(self,text="Start The Game",image=self.gamephoto,command=self.loading,width=160,height=30).grid(row=9,column=14,columnspan=20,rowspan=30)

        else:
            var = messagebox.showinfo("Welcome!" , "Welcome New User!!\nYou get 50 Chips.")
            self.members[self.name]=(0,0,50)
            file=open('members.txt','w')
            for key in self.members:
                self.tries,self.wins,self.chips=self.members[key]
                line=key+','+str(self.tries)+','+str(self.wins)+','+str(self.chips)+'\n'
                file.write(line)
            file.close()
            summary1="Welcome, "+self.name+'!'+'\n'
            summary1="-Your Status-"+'\n'
            summary1+="Tries : "+str(self.tries)+" games"+'\n'
            summary1+="Wins : "+str(int(self.wins))+" games"+'\n'
            summary1+="Loses : "+str(int(self.tries - self.wins))+" games"+'\n'
            self.winrate=100*self.wins/self.tries if self.tries>0 else 0
            summary1+="Winrate : "+str(round(self.winrate,1))+' %'+'\n'
            summary1+="Chips : "+str(self.chips)+ ' chip(s)'
            Label(self, text=summary1,font=15).grid(row=1,column=14,columnspan=20,rowspan=30)
            Button(self,text="Start The Game",image=self.gamephoto,command=self.loading,width=160,height=30).grid(row=9,column=14,columnspan=20,rowspan=30)

    def cantstart(self):
        var = messagebox.showinfo("Error!" , "You have no chip!\nPlease make a new account.")

    def loading(self):
        """shows loading image"""
        self.photo = PhotoImage(file="loading.gif")
        self.label = Label(self, image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=0,column=0,columnspan=20,rowspan=20)
        window.after(1000, lambda:self.next_page())

    def next_page(self):
        """switches page to App"""
        self.pack_forget()
        App(window,self.name).pack()


class Card:
    """defines Card class"""
    __suits = ("Diamond", "Heart", "Spade", "Clover")
    __ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    
    def __init__(self, suit, rank, face_up=True):
        """creates a playing card object 
        arguments:
        suit -- must be in Card.__suits
        rank -- must be in Card.__ranks
        face_up -- True or False (defaut True)
        """
        if suit in Card.__suits and rank in Card.__ranks:
            self.__suit = suit
            self.__rank = rank
            self.__face_up = face_up
        else:
            print("Error: Not a valid card")
        self.__value = Card.__ranks.index(self.__rank) + 1
        if self.__value > 10:
            self.__value = 10
 
    def __str__(self):
        """returns its string representation"""
        if self.__face_up:
            return self.__suit +  self.__rank
        else:
            return "xxxxx" + "." + "xx"
 
    @property
    def suit(self):
        """its suit value in Card.__suits"""
        return self.__suit
 
    @property
    def rank(self):
        """its rank value in Card.__ranks"""
        return self.__rank
 
    @property
    def face_up(self):
        """its face_up value : True or False"""
        return self.__face_up
 
    @property
    def value(self):
        """its face value according to blackjack rule"""
        return self.__value
 
    def flip(self):
        """flips itself"""
        self.__face_up = not self.__face_up
 
    @staticmethod
    def fresh_deck():
        """returns a brand-new deck of shuffled cards with all face down"""
        cards = []
        for s in Card.__suits:
            for r in Card.__ranks:
                cards.append(Card(s,r,False))
        random.shuffle(cards)
        return cards
 
class Deck:
    """defines Deck class"""
    def __init__(self):
        """creates a deck object consisting of 52 shuffled cards 
        with all face down"""
        self.__deck = Card.fresh_deck()
 
 
    def next(self, open=True):
        """removes a card from deck and returns the card
        with its face up if open == True, or 
        with its face down if open == False
        """
        if self.__deck == []:
            self.__deck = Card.fresh_deck()
        card = self.__deck[0]
        self.__deck = self.__deck[1:]
        if open :
            card.flip()
        return card

class Hand:
    """defines Hand class"""
    def __init__(self, name="Dealer"):
        """creates player/dealer's empty hand
        argument: name -- player's name in string (default: 'Dealer')
        """
        self.__name = name
        self.__hand = []
        
    def __str__(self):
        """returns its string representation"""
        if len(self.__hand) == 0:
            show = "empty"
        else:
            show = ""
            for card in self.__hand:
                show += str(card) + " "
        return show

    @property
    def name(self):
        """its name : either player's name or 'Dealer'"""
        return self.__name

    @property
    def total(self):
        """the total value of its hand"""
        point = 0
        number_of_ace = 0
        for card in self.__hand:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += card.value
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point  

    def get(self, card):
        """gets a card from deck and puts the card into its hand"""
        self.__hand.append(card)

    def clear(self):
        """empties its hand"""
        self.__hand = []

    def open(self):
        """turns all of its hand's cards' faces up"""
        for card in self.__hand:
            if not card.face_up:
                card.flip()

class App(Frame):
    def __init__(self, master,name):
        super().__init__(master)
        self.pack(padx=10,pady=10)
        self.master=master
        self.a = Deck()
        self.n=2
        self.betamount = 1
        self.m=0
        self.d1=0
        self.d2=0
        self.we = Login(self)
        self.name=name
        self.chips = self.we.members[self.name][2]
        self.tries = self.we.members[self.name][0]
        self.wins = int(self.we.members[self.name][1])
        self.loses = int(self.tries-self.wins)
        self.photo = PhotoImage(file="back2.gif")
        self.back = PhotoImage(file='back-blue.gif')
        self.imagehit = PhotoImage(file='hitimage.gif')
        self.imagestart = PhotoImage(file='startimage.gif')
        self.stayimage = PhotoImage(file='stayimage.gif')
        self.betplus = PhotoImage(file='betplus.gif')
        self.betminus = PhotoImage(file='betminus.gif')
        self.create_widgets()

    def bet1(self):
        self.betamount = 1
        Label(self,text=self.betamount,font=20).grid(row=6, column=0)

    def gameover(self):
        if self.chips == 0:
            var = messagebox.showinfo("Game Over!" , "You Game Over!\nI'm sure you have to make a new account")
            self.store_members()
            self.quit()


    def create_widgets(self):
        """creates widgets for App"""
        self.b = Hand('Player')
        self.c=  Hand()
        self.we = Login(self)
        self.label = Label(self, image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=0,column=0,columnspan=20,rowspan=20)
        p1 = "      "
        d1 = "      "
        p2 = "      "
        d2 = "      "
        p3 = "      "
        d3 = "      "
        p4 = "      "
        d4 = "      "
        p5 = "      "
        d5 = "      "
        p6 = "      "
        d6 = "      "
        p7 = "      "
        d7 = "      "
        self.pscore = 0
        self.dscore = 0
        Label(self, text=self.pscore,font=30).grid(row=0, column=11)
        Label(self, text=self.dscore,font=30).grid(row=3, column=11)

        self.save()
    
        Label(self, text=self.chips,font=30, relief=RAISED).grid(row=6, column=7)

        self.labelp1=Label(self,relief=RAISED)
        self.labelp1['image']=self.back
        self.labelp1.grid(row=0,column=2)
        self.labelp2=Label(self, relief=RAISED)
        self.labelp2['image']=self.back
        self.labelp2.grid(row=0,column=3)
        self.labelp3=Label(self, relief=RAISED)
        self.labelp3['image']=self.back
        self.labelp3.grid(row=0,column=4)
        self.labelp4=Label(self, relief=RAISED)
        self.labelp4['image']=self.back
        self.labelp4.grid(row=0,column=5)
        self.labelp5=Label(self, relief=RAISED)
        self.labelp5['image']=self.back
        self.labelp5.grid(row=0,column=6)
        self.labelp6=Label(self, relief=RAISED)
        self.labelp6['image']=self.back
        self.labelp6.grid(row=0,column=7)
        self.labelp7=Label(self, relief=RAISED)
        self.labelp7['image']=self.back
        self.labelp7.grid(row=0,column=8)

        self.labeld1=Label(self, relief=RAISED)    
        self.labeld1['image']=self.back
        self.labeld1.grid(row=3,column=2)
        self.labeld2=Label(self, relief=RAISED)
        self.labeld2['image']=self.back
        self.labeld2.grid(row=3,column=3)
        self.labeld3=Label(self, relief=RAISED)
        self.labeld3['image']=self.back
        self.labeld3.grid(row=3,column=4)
        self.labeld4=Label(self, relief=RAISED)
        self.labeld4['image']=self.back
        self.labeld4.grid(row=3,column=5)
        self.labeld5=Label(self, relief=RAISED)
        self.labeld5['image']=self.back
        self.labeld5.grid(row=3,column=6)
        self.labeld6=Label(self, relief=RAISED)
        self.labeld6['image']=self.back
        self.labeld6.grid(row=3,column=7)
        self.labeld7=Label(self, relief=RAISED)
        self.labeld7['image']=self.back
        self.labeld7.grid(row=3,column=8)


        self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
        self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
        self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
        Button(self, text='quit',command=self.end,width=10,height=2).grid(row=7,column=8)
        self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
        self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
        Label(self, text=self.betamount,font=20).grid(row=6, column=0)

    def bet(self):
        if self.betamount+1 <= self.chips:
            self.betamount += 1
            Label(self, text=self.betamount,font=20).grid(row=6, column=0)
    def nobet(self):
        if self.betamount > 1:
            self.betamount -=1
            Label(self, text=self.betamount,font=20).grid(row=6, column=0)

    def start(self):
        """starts the game. 
        Player and Dealer get 2 cards each, one of the Dealer's card is unveiled"""
        self.create_widgets()
        self.START = Button(self, text='start',width=50,height=50,command=self.start,state=DISABLED,image=self.imagestart).grid(row=6,column=2)
        self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,image=self.imagehit).grid(row=6, column=3)
        self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,image=self.stayimage).grid(row=6, column=4)
        self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,state=DISABLED,image=self.betplus).grid(row=5, column=0)
        self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,state=DISABLED,image=self.betminus).grid(row=7, column=0)
        self.n=2
        self.n2=2
        self.chips = self.chips - self.betamount
        Label(self, text=self.chips,font=30, relief=RAISED).grid(row=6, column=7)
        x=self.a.next(self)
        p1=x
        y=str(x)+'.gif'
        self.photop1=PhotoImage(file=y)
        self.labelp1['image']=self.photop1
        self.b.get(x) # 플레이어 첫장 받음

        self.hidden=self.a.next(self)
        self.d1=self.hidden
        y=str(self.hidden)+'.gif'
        self.photod1=PhotoImage(file=y)
        # self.labeld1['image']=self.photod1 #첫째장을 사진가리기위해 주석
        # self.c.get(x)
        # self.dscore=self.c.total #딜러 첫장 받음,점수가리기

        x=self.a.next(self) 
        p2=x
        y=str(x)+'.gif'
        self.photop2=PhotoImage(file=y)
        self.labelp2['image']=self.photop2
        self.b.get(x)
        self.pscore = self.b.total
        Label(self, text=self.pscore,font=30).grid(row=0, column=11) # 플레이어 둘째장

        x=self.a.next(self)
        self.d2=x
        y=str(x)+'.gif'
        self.photod2=PhotoImage(file=y)
        self.labeld2['image']=self.photod2
        self.c.get(x)
        Label(self,text=self.c.total,font=30).grid(row=3,column=11) # 딜러 둘째장

        self.blackjackcheck()

    def save(self):
        """shows updated number of chips, tries, wins and loses of player"""
        Label(self, text=self.chips,font=30, relief=RAISED).grid(row=6, column=7)

    def hit(self):
        """hit : 
        ask for another card in an attempt to get closer to a count of 21"""
        self.n+=1
        x=self.a.next(self)
        self.bustcheck()
        self.blackjackcheck()
        if self.bustcheck() == True:
            if self.n==3:
                p3=x
                y=str(x)+'.gif'
                self.photop3=PhotoImage(file=y)
                self.labelp3['image']=self.photop3
                self.b.get(x)
            elif self.n==4:
                p4=x
                y=str(x)+'.gif'
                self.photop4=PhotoImage(file=y)
                self.labelp4['image']=self.photop4
                self.b.get(x)
            elif self.n==5:
                p5=x
                y=str(x)+'.gif'
                self.photop5=PhotoImage(file=y)
                self.labelp5['image']=self.photop5
                self.b.get(x)
            elif self.n==6:
                p6=x
                y=str(x)+'.gif'
                self.photop6=PhotoImage(file=y)
                self.labelp6['image']=self.photop6
                self.b.get(x)
            elif self.n==7:
                p7=x
                y=str(x)+'.gif'
                self.photop7=PhotoImage(file=y)
                self.labelp7['image']=self.photop7
                self.b.get(x)
        self.pscore = self.b.total 
        Label(self, text=self.pscore,font=30).grid(row=0, column=11)
        self.bustcheck()
        self.blackjackcheck()

    def blackjackcheck(self):
        """checks player's blackjack"""
        if self.pscore == 21:
            self.wins+=1
            self.tries+=1
            self.chips += self.betamount*2+self.betamount//2
            var = messagebox.showinfo("Result" , "BLACKJACK! YOU WIN!"+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.store_members()
    def bustcheck(self):
        """checks player's bust"""
        if self.pscore > 21:
            self.loses+=1
            self.tries+=1
            var = messagebox.showinfo("Result" , "You Bust! Dealer Win"+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.gameover()
            self.store_members()
            # Label(self, text="You Bust!").grid(row=8, column=1)
            return False
        else:
            return True

    def dbustcheck(self):
        """checks dealer's bust"""
        if self.dscore > 21:
            self.wins+=1
            self.tries+=1
            self.chips+=self.betamount*2
            var = messagebox.showinfo("Result" , "Dealer Bust! You Win"+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.store_members()
            return False
        else:
            return True

    def winnercheck(self):
        '''checks the winner'''
        
        if self.pscore > self.dscore and self.bustcheck() == True:
            self.wins+=1
            self.tries+=1
            self.chips+=self.betamount*2
            var = messagebox.showinfo("Result" , "Player Win!\nPlayer:"+str(self.pscore)+" Dealer:"+str(self.dscore)+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagehit).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagestart).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.store_members()

        elif self.pscore < self.dscore and self.dbustcheck() == True:
            self.loses+=1
            self.tries+=1
            var = messagebox.showinfo("Result" , "Dealer Win!\nPlayer:"+str(self.pscore)+" Dealer:"+str(self.dscore)+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",justify=CENTER,command=self.hit,state=DISABLED,width=50,height=50,image=self.imagehit).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",command=self.stay,state=DISABLED,width=50,height=50,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.gameover()
            self.store_members()
        elif self.pscore == self.dscore:
            self.tries+=1
            self.chips += self.betamount
            var = messagebox.showinfo("Result" , "Draw!\nPlayer:"+str(self.pscore)+" Dealer:"+str(self.dscore)+'\n\n'+"Win - "+str(self.wins)+" Lose - "+str(self.tries-self.wins)+" ("+str(round(100*self.wins/self.tries if self.tries>0 else 0,1))+' %)')
            self.save()
            self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
            self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
            self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
            self.BET = Button(self, text="bet+",width=50,height=50,command=self.bet,image=self.betplus).grid(row=5, column=0)
            self.NOBET = Button(self, text="bet-",width=50,height=50,command=self.nobet,image=self.betminus).grid(row=7, column=0)
            self.bet1()
            self.store_members()
    def stay(self):
        """stay:
        not ask for another card"""
        self.labeld1['image']=self.photod1
        self.c.get(self.hidden)
        self.dscore = self.c.total
        self.START = Button(self, text='start',width=50,height=50,command=self.start,image=self.imagestart).grid(row=6,column=2)
        self.HIT = Button(self, text="hit",width=50,height=50,justify=CENTER,command=self.hit,state=DISABLED,image=self.imagehit).grid(row=6, column=3)
        self.STAY = Button(self, text="stay",width=50,height=50,command=self.stay,state=DISABLED,image=self.stayimage).grid(row=6, column=4)
        Label(self, text=self.dscore,font=30).grid(row=3, column=11)
        self.dbustcheck()
        while 0 <= self.dscore <= 16 and self.dbustcheck() == True:
            x = self.a.next()
            if self.n2 == 2:
                d3=x
                y=str(x)+'.gif'
                self.photod3=PhotoImage(file=y)
                self.labeld3['image']=self.photod3
                self.c.get(x)
                self.dscore = self.c.total
                self.n2+=1
            elif self.n2 == 3:
                d4=x
                y=str(x)+'.gif'
                self.photod4=PhotoImage(file=y)
                self.labeld4['image']=self.photod4
                self.c.get(x)
                self.dscore = self.c.total
                self.n2+=1
            elif self.n2 == 4:
                d5=x
                y=str(x)+'.gif'
                self.photod5=PhotoImage(file=y)
                self.labeld5['image']=self.photod5
                self.c.get(x)
                self.dscore = self.c.total
                self.n2+=1
            elif self.n2 == 5:
                d6=x
                y=str(x)+'.gif'
                self.photod6=PhotoImage(file=y)
                self.labeld6['image']=self.photod6
                self.c.get(x)
                self.dscore = self.c.total
                self.n2+=1
            elif self.n2 == 6:
                d7=x
                y=str(x)+'.gif'
                self.photod7=PhotoImage(file=y)
                self.labeld7['image']=self.photod7
                self.c.get(x)
                self.dscore = self.c.total
                self.n2+=1
            Label(self, text=self.dscore,font=30).grid(row=3, column=11)
        self.winnercheck()

    def end(self):
        """ends the game"""
        self.store_members()
        summary=self.show_top5()
        var=messagebox.showinfo("Ranking",summary)
        self.quit()

    def store_members(self):
        """updates number of tries, wins, chips of player"""
        self.we.members[self.name]=(self.tries,self.wins,self.chips)
        file=open("members.txt",'w')
        for key in self.we.members:
            tries,wins,chips=self.we.members[key]
            line=key+','+str(tries)+','+str(wins)+','+str(chips)+'\n'
            file.write(line)
        file.close()

    def show_top5(self):
        """shows top 5 players by chips"""
        self.sorted_members=sorted(self.we.memebers.items(),key=lambda x:x[1][2],reverse=True)
        rank=1
        summary=''
        for self.we.members in self.sorted_members:
            chips=self.sorted_members[:5]
            chips=self.we.members[1][2]
            if chips<=0:
                break
            summary+=str(rank)+'.'+self.we.members[0]+':'+str(chips)+'\n'
            rank+=1
            if rank>5:
                break
        return summary


window=Tk()
window.geometry('860x430')
window.title("Black")
Login(window).pack()
window.mainloop()
