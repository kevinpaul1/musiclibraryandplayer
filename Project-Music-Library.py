#--Import all modules to be used--

from Tkinter import *
import pyglet
import tabulate
import os
import pickle

                        #--Create a class for user's registration and login--

class registration:

                        #--Functions in the class to be called at runtime--
    
    def register(self):
        self.username=raw_input("Enter a username you would like to use. ")
        self.password=raw_input("Enter a password you would like to use. ")
        self.a=open("users.txt","a+")
        self.l=self.a.readlines()
        self.flag1=0
        if (self.username+"\n") in self.l:
            for i in range(0,len(self.l),2):
                if self.l[i]==self.username+"\n":
                    self.flag1=1
                    break
                else:
                    pass
        if self.flag1==0:
            self.a.write(self.username)
            self.a.write("\n")
            self.a.write(self.password)
            self.a.write("\n")
            self.a.close()
            print "Registration Successful"
            print
        
        else:
            print "Username Already present"
            print
    def login(self):
        self.b=open("users.txt","a")
        self.user1=raw_input("Enter the username-  ")
        self.pas1=raw_input("Enter the password-  ")
        self.b=open("users.txt","r")
        self.l=self.b.readlines()
        self.flag2=0
        if (self.user1+"\n") in self.l:
            for i in range(0,len(self.l),2):
                if self.l[i]==self.user1+"\n":
                    if self.l[i+1]==self.pas1+"\n":
                        self.flag2=1
                        break
                    else:
                        pass
                else:
                    pass
        if self.flag2==1:
            print
            print"Login Succesful!"
            print"----------------"
            self.f=open(self.user1+".dat","ab")
            self.f.close()
            print
        elif self.flag2==2:
            pass
        else:
            print
            print"Login Incorrect!"
            print"----------------\n"
            print"The username you provided either doesn't exist or the password doesn't match it."

            '''calls the login function again to allow user to
            type in accont information if entered wrong'''
            
            self.login()

                        #--Create a class for the music library itself--
class music:
    def __init__(self):
        self.name="null"
        self.artist="null"
        self.album="null"
    def getdata(self):
        self.name=raw_input("Enter the Song Name You wish to Add: ")
        self.artist=raw_input("Enter the Artist of the Song: ")
        self.album=raw_input("Enter the Album of the Song: ")
        print
    def getname(self):
        self.name=raw_input("Enter the New Song Name: ")
    def getartist(self):
        self.artist=raw_input("Enter the New Artist Name: ")
    def getalbum(self):
        self.album=raw_input("Enter the New Album Name: ")
    def outdata(self):
        return [self.name,self.artist,self.album]
m=music()              #Create an object for class music
def append():           #To Add details

    '''--Saves input in a file to be accessed at any time in the program to perform various operations--
    --Also allows to add more data as input at any time--'''

    print                                                                                                                                                                                                                                                                                                                                 
    print "Be sure to only enter songs that are saved in your system, and to enter the \ncorrect name of the song, exactly as it is saved, including capitalisation"  
    print
    f=open("p1.dat","ab")
    print "Go easy on yourself and enter names of songs that you can see,\nand that are right there on your desktop"
    print
    size=input("Enter the No. of Songs You wish to Add to the Music Library: ")
    print
    for i in range(0,size):
        m.getdata()
        pickle.dump(m,f)
    f.close()
    print
def update():           # Updates and Shows in the Print

    '''--If user feels that he/she has entered the wrong details, he/she may opt to change the saved details--
    --He/she may change(update) song name, artist name or album name for any song--'''

    print
    print"\tEnter 1 to Update Song Name\tEnter 2 to Update Artist Name\n\tEnter 3 to Update Album Name"
    choice=input("Enter your Choice: ")
    if choice==1:
        f=open("p1.dat","rb")
        f1=open("temp.dat","ab")
        x=raw_input("Enter the Song to be Updated: ")
        try:
            while True:
                m=pickle.load(f)
                if m.name!=x:
                    pickle.dump(m,f1)
                else:
                    print"\tEnter new details "
                    m.getname()
                    pickle.dump(m,f1)
        except EOFError:
            pass
        f.close()
        f1.close()
        os.remove("p1.dat")
        os.rename("temp.dat","p1.dat")
        
    elif choice==2:
        f=open("p1.dat","rb")
        f1=open("temp.dat","ab")
        y=raw_input("Enter the Name of the Artist to Update: ")
        try:
            while True:
                m=pickle.load(f)
                if m.artist!=y:
                    pickle.dump(m,f1)
                else:
                    print"\tEnter new details "
                    m.getartist()
                    pickle.dump(m,f1)
        except EOFError:
            pass
        f.close()
        f1.close()
        os.remove("p1.dat")
        os.rename("temp.dat","p1.dat")
    elif choice==3:
        f=open("p1.dat","rb")
        f1=open("temp.dat","ab")
        z=raw_input("Enter the Name of the Album: ")
        try:
            while True:
                m=pickle.load(f)
                if m.album!=z:
                    pickle.dump(m,f1)
                else:
                    print"\tEnter new details "
                    m.getalbum()
                    pickle.dump(m,f1)
        except EOFError:
            pass
        f.close()
        f1.close()
        os.remove("p1.dat")
        os.rename("temp.dat","p1.dat")
    else:
        print "Wrong Choice"
    print
def delete():           #to delete songs

        #--Remove songs of user's choice--

    print
    f=open("p1.dat","rb")
    f1=open("temp.dat","ab")
    song=raw_input("Enter the Song to be Deleted: ")
    flag=0
    try:
        while True:
            m=pickle.load(f)
            if m.name!=song:
                pickle.dump(m,f1)
            else:
                flag=1
    except EOFError:
        pass
    f.close()
    f1.close()
    if flag==1:
        print
        print"Deletion successful."
        print"--------------------"
    os.remove("p1.dat")
    os.rename("temp.dat","p1.dat")
    print
def search():           #To Search for details 

        #--searches for song/artist name already saved in the file by user through append()--

    print
    global flag1
    f=open("p1.dat","rb")
    print"\t1.Enter 1 to search using Song Name\n\t2.Enter 2 to search using Artist Name"
    print
    choice=input("Enter your Choice: ")
    if choice==1:
        song=raw_input("Enter the Song Name to be Searched for: ")
        flag1=0
        l=[]
        try:
            while True:
                m=pickle.load(f)
                if m.name==song:
                    flag1=1
                    v=m.outdata()
                    l.append(v)
                    break
        except EOFError:
            pass
        if flag1==1:
            print"The song you Searched for is Present"
            headers=["SONG","ARTIST","ALBUM"]
            print tabulate.tabulate(l,headers)
            print
        else:
            print
            print"The song you Searched for isn't Present"

                        #--user-friendly statements indicate whether search was found-- 

    elif choice==2:
        artist=raw_input("Enter the Artist Name to be Searched for: ")
        flag1=0
        l=[]
        try:
            while True:
                m=pickle.load(f)
                if m.artist==artist:
                    flag1=1
                    v=m.outdata()
                    l.append(v)
                    break
        except EOFError:
            pass
        if flag1==1:
            print"The artist you Seached for is Present"
            print
            headers=["SONG","ARTIST","ALBUM"]
            print tabulate.tabulate(l,headers)
        else:
            print
            print"The artist you Searched for isn't Present"
    if flag1==1:

                        #--Allows user to use information when search is found--

        print
        
def display():          # to show data present in files

        #--Shows all songs already saved in the file in table format, with artist and album names--

    print
    f=open("p1.dat","rb")
    table=[]
    try:
        while True:
            m=pickle.load(f)
            l=m.outdata()
            table.append(l)
    except EOFError:
        pass
    headers=["SONG","ARTIST","ALBUM"]
    print tabulate.tabulate(table,headers)
    f.close()
    print

def sort():             # Sorts in ascending or descending order depending on user's choice

    '''--Gives user the option to view all saved songs in ascending
    in order of song name, artist name or  album name--'''

    print
    display()
    f=open("p1.dat","rb")
    L=[]
    print "\tEnter 1 to sort by Song name\tEnter 2 to sort by Artist name\n\tEnter 3 to sort by Album name"
    choice1=input("\tEnter your choice ")
    print
    if choice1==1:
        print
        try:
            while True:
                m=pickle.load(f)
                l=m.outdata()
                L.append(l)
        except EOFError:
            pass
        if choice==1:
            for i in range(len(L)):
                if i+1<=len(L)-1:
                    j=L[i]
                    j1=L[i+1]
                    k=j[0]
                    k1=j1[0]
                    if k[0]>k1[0]:
                        L[i],L[i+1]=L[i+1],L[i]
                    else:
                        if k[1]>k1[1]:
                            L[i],L[i+1]=L[i+1],L[i]
                        elif k[2]>k1[2]:
                            L[i],L[i+1]=L[i+1],L[i]
            print
            print "\tSorted in Ascending Order"
            print
    elif choice1==2:
        print
        try:
            while True:
                m=pickle.load(f)
                l=m.outdata()
                L.append(l)
        except EOFError:
            pass
        for i in range(len(L)):
            if i+1<=len(L)-1:
                j=L[i]
                j1=L[i+1]
                k=j[1]
                k1=j1[1]
                if k[0]>k1[0]:
                    L[i],L[i+1]=L[i+1],L[i]
                else:
                    if k[1]>k1[1]:
                        L[i],L[i+1]=L[i+1],L[i]
                    elif k[2]>k1[2]:
                        L[i],L[i+1]=L[i+1],L[i]
        print
        print "\tSorted in Ascending Order"
        print
    elif choice1==3:
        print
        try:
            while True:
                m=pickle.load(f)
                l=m.outdata()
                L.append(l)
        except EOFError:
            pass
        for i in range(len(L)):
            if i+1<=len(L)-1:
                j=L[i]
                j1=L[i+1]
                k=j[2]
                k1=j1[2]
                if k[0]>k1[0]:
                    L[i],L[i+1]=L[i+1],L[i]
                else:
                    if k[1]>k1[1]:
                        L[i],L[i+1]=L[i+1],L[i]
                    elif k[2]>k1[2]:
                        L[i],L[i+1]=L[i+1],L[i]
        print
        print "\tSorted in Ascending Order"
        print
    else:
        print "\tWrong choice"
    headers=["SONG","ARTIST","ALBUM"]
    print tabulate.tabulate(L,headers)    
    f.close()
    print
def play():             #Plays/Pauses music of user's choice

    '''--Plays music saved in the system(on desktop) as per user's input,
    hence the statement urging user to enter the correct name of the song in append()--''' 

    print
    f=open("p1.dat","rb")
    l=[]
    print "\tYou may add these songs to your playlist:"
    display()
    print "\tIn the order of songs given above, enter the format the song is saved in.\n\ti.e; if the song is 'song.mp3', enter '.mp3' "
    print
    try:
    
        while True:
            m=pickle.load(f)
            playlist=m.name
            form=raw_input("\tEnter format ")
            l.append(playlist+form)
            print
            
    except Exception:
        pass
    
    f.close()
    player=pyglet.media.Player()
    print "Songs in Playlist:\n"
    for i in range(len(l)):    
        print l[i]
    c=raw_input("\tAre you sure you entered the right format(s) for the song(s) or would you like to change them?\n\tTo change your input, enter 'change'\nTo continue,just press enter/return key ")
    try:
        while True:
            if c!='change':
                for i in range(len(l)):
                    player.queue(pyglet.resource.media(l[i]))
                def play_song():
                    player.play()
                def pause_song():
                    player.pause()
                def next_up():
                    player.next()
                _play=Button(text="PLAY",fg="GREEN",command=play_song)
                _play.pack(side="left")

                _pause=Button(text="PAUSE",fg="red",command=pause_song)
                _pause.pack(side="left")

                _next=Button(text="NEXT SONG",fg="blue",command=next_up)
                _next.pack(side="left")
                
                box=Tk()
                box.attributes("-topmost",True)
                box.mainloop()
                box.destroy()
                pyglet.app.run()
            else:
                box=Tk()
                box.destroy()
                play()
    except:
        pass
    finally:
        print
print"*****WELCOME TO YOUR PERSONALIZED MUSIC LIBRARY*****"
print"----------------------------------------------------------"

'''--lets the user choose between registering, logging in,
and/or leaving the application--
--creates an object for registration to
allow user to access all its functions--'''

choice="yes"
while True:
    r=registration()
    print"Enter 1 to register or 2 to login or 3 to exit."
    choice2=raw_input("Enter your choice. ")
    if choice2=="1":
        r.register()
        continue        #--lets user contine with logging in after registration--
    elif choice2=="2":
        r.login()
        print
        print"\t***Welcome",r.user1,"***"
        break           #--moves straight to working on the user's personal music library-- 
    elif choice2=="3":
        print "Thank You User"
        print "--------------"
        break 
    else:
        print "Invalid Choice\n"
        continue

        '''--moves to start of loop to make room for error
        from user's side and allows for re-entering of info--'''
    
print"-----------------------------------"
print

'''--gives User a choice on what operation he/she would like to perform.
the loop ensures that the user can continue running operations
for as long as he/she wishes--''' 

if choice2!="3":
    ch="yes"
    while ch=="yes":
        print"Enter 1 To Add song(s)\nEnter 2 To Search\nEnter 3 To Delete songs\nEnter 4 To Display all songs\nEnter 5 To Update song(s)\nEnter 6 To Sort in alphabetic order\nEnter 7 To Play all song(s)"
        choice3=input("Enter Your Choice: ") # To take input of User's Choice
        if os.path.isfile("p1.dat"):

                        #--makes sure that file exists so user can run operations--

            if choice3 ==1:
                append()
            elif choice3 ==2:
                search()
                if flag!=1:
                    break
                else:
                    print"Enter 1 to Update\tEnter 2 to Delete\tEnter 3 to Play"
                    choice1=input("Enter your choice.")
                    print
                    try:
                        while True:
                            if choice1==1:
                                update()
                                break
                            elif choice1==2:
                                delete()
                                break
                            elif choice1==3:
                                if len(l)==1:
                                    form=raw_input("Enter format the song is saved in ('.mp3', '.wav', '.ogg') ")
                                    z=l[0]
                            
                                else:
                                    print
                                    print tabulate.tabulate(l,headers=["SONG","ARTIST","ALBUM"])
                                    op=input("Enter the number of the song in this list(1,2,3....) ")
                                    print
                                    form=raw_input("Enter the format the song is saved in('.mp3','.wav','.ogg') ")
                                    z=l[op-1]
                                    name=z[0]+form    
                                    player1=pyglet.media.Player()
                                def play_it():
                                    player1.play()
                                def pause_it():
                                    player1.pause()
                            
                                player1.queue(pyglet.resource.media(name))
                            
                                play_1=Button(text="PLAY",fg="green",command=play_it)
                                play_1.pack(side="left")

                                pause_1=Button(text="PAUSE",fg="red",command=pause_it)
                                pause_1.pack(side="left")

                                c=raw_input("\tAre you sure you entered the right format(s) for the song(s) or would you like to change them?\n\tTo change your input, enter 'change'\tTo continue,just press enter/return key ")
                                try:
                                    while True:
                                        if c=='change':
                                            print
                                            print tabulate.tabulate(l,headers=["SONG","ARTIST","ALBUM"])
                                            op=input("Enter the number of the song in this list(1,2,3....) ")
                                            print
                                            form=raw_input("Enter the format the song is saved in('.mp3','.wav','.ogg') ")
                                            z=l[op-1]
                                     
                                        print "To stop playback, just close the objects"
                                        window=Tk()
                                        window.lift()
                                        window.mainloop()
                                        window.destroy()
                                        pyglet.app.run()
                                except Exception:
                                    pass
                                finally:
                                    print    
                                break
                    except Exception:
                        pass #--Accesses the class of all exceptions (exceptions.Exception()) and passes them all-- 
            elif choice3==3:
                delete()
            elif choice3==4:
                display()
            elif choice3==5:
                update()
            elif choice3==6:
                sort()
            elif choice3==7:
                play()
            else:
                print"Invalid choice"
        else:

                        #--if file doesn't exist, program creates the file at user' command-- 

            newchoice=raw_input("A file has to be created to carry out this operation.\nWould you like to create it? ")
            if newchoice=="yes":
                append()
        ch=raw_input("Do you wish to Continue? ")
