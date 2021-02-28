import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter.messagebox import askokcancel




root = Tk()

root.minsize(450,450)

root.maxsize(1500,1500)

menubar = Menu(root)

root.title('DJ MIX')

root.config(menu = menubar)

app = Toplevel()


filename2 = PhotoImage(file = r"C:\Users\jackwin joseph\Pictures\lambo png.PNG")#add the desired image over here

background_label = Label(root, image = filename2,border=0, height = 1000, width  = 1000, padx  =  10, pady  = 10)

background_label.place(x=0, y=0, relwidth=1,bordermode = INSIDE, relheight = 1, anchor = NW)


songslist = []


realnames = []


artist = []

album = []

genre = []






v = StringVar()

songlabel = Label(root, textvariable = v, width = 20, bd = 20,font='bold',bg='grey',fg='black')



b = StringVar()


artistlabel = Label(root, textvariable =  b, width = 50 ,bd = 10)#string variable for the artist name

#C = Canvas(root, bg = "red", height = 20, width = 20)




index = 0





def choosedirectory():#shashank from here

    directory = askdirectory()
    
    os.chdir(directory)

    

    for files in os.listdir(directory):

        
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)

            audio = ID3(realdir)

            realnames.append(audio.get('TIT2','unknown song'))

            genre.append(audio.get('TCON','unkown genre'))

            artist.append(audio.get('TPE1','unknown artist'))

            album.append(audio.get('TALB','single track'))

            songslist.append(files)
    
            

            pygame.mixer.init()
            
            pygame.mixer.music.load(songslist[0])

            pygame.mixer.music.play()#here
            
            #while pygame.mixer.music.get_busy():
             #   pygame.time.Clock().tick(1)


#queuesong=[]



#for i in songslist:
 #   queuesong.append(i)


#queuesong.reverse()



#def queuesongs():

 #   pygame.mixer.music.load(queuesong.pop())
#
 #   pygame.mixer.music.queue(queuesong.pop())

  #  pygame.mixer.music.play()

   # while len(queuesongs)>0:

    #    pygame.mixer.music.queue(queuesong.pop())



def rewind():
    pygame.mixer.music.rewind()
    pass



def pause(event):
    pygame.mixer.music.pause()
    pass



def unpause(event):
    pygame.mixer.music.unpause()
    pass



def shutdown():
    if askokcancel(title='quit dj mix?',message='do you really want to quit?'):
        pygame.mixer.music.stop()
        root.destroy()



pause_unpause = Button(root,text='pause/unpause',border=0,width=14,height=5,font='bold',bg='grey')
pause_unpause.grid(row=3,column=0,padx=2,pady=2,ipadx=2,sticky=N)


pause_unpause.bind('<Button-1>',pause)
pause_unpause.bind('<Double-1>',unpause)

choosedirectory()



def updatename():
    
    global index
    
    global songname
    
    global artistname
    
    v.set(realnames[index])
    
    b.set(artist[index])
    #return songname



def nextsong(event):
    
    global index
    
    index += 1
    
    pygame.mixer.music.load(songslist[index])
    
    pygame.mixer.music.play()
    
    updatename()



def prevsong(event):
    
    global index

    index -= 1
    
    pygame.mixer.music.load(songslist[index])
    
    pygame.mixer.music.play()
    
    updatename()




def stopsong(event):
    
    pygame.mixer.music.stop()
    
    v.set("")
    b.set("")
    
    #return songname




def change_volume(event):
    
    pygame.mixer.music.set_volume(volume.get())
    



volume=DoubleVar()

volume.set(pygame.mixer.music.get_volume())

volume_scale = Scale(variable= volume,
                     from_ = 0.0,
                     to = 1.0,
                     resolution= 0.1,bg='light green',width=10,fg='purple',
                     command = change_volume,border=0,font='bold',
                     label='volume',
                     orient = HORIZONTAL)

volume_scale.grid(row=2,column=2,padx=2,pady=2,ipadx=2,sticky=S)
#volume_scale.grid()




#rewindButton.grid()

#queue1 = Button(root,bg='grey',width=10,height=5,text='queue',command=queuesongs)
#queue1.grid(row=3,column=2,padx=2,pady=2,ipadx=2,sticky=W)


#queue1.grid()
#first_frame=Frame(root)
#label = Label(root, text = {}.format(updatename), bd  = 10, font = ('calibri',50) ,height = 1 , fg = 'dark green')

#label.grid(row=0,column=1,ipadx=10,padx=10,pady=10,sticky=N)

#but=Button(root,text='names',command=updatelabel)
#but.grid(sticky=S)
#but.bind('<Button-1>',updatelabel)





listbox = Listbox(root, selectbackground = 'black',selectmode = BROWSE, bd = 20, height = 20, width =20, font = 'helvetica,30')



listbox.grid(row=1,column=0,padx=1,pady=1,sticky=NW)
#listbox.grid()




listbox2 = Listbox(root, selectbackground = 'blue',selectmode = BROWSE, bd = 20, height = 20, width = 20, font = 'times,30')

listbox2.grid(row=1,column=1,padx=1,pady=1,sticky=N)
#listbox2.grid()


listbox3 = Listbox(root,selectbackground='black',selectmode=BROWSE,bd=20,height=20,width=20,font='calibri,30')
listbox3.grid(row=1,column=2,padx=1,columnspan=1,pady=1,ipadx=1,sticky=N)


#listbox3.grid()
listbox4 = Listbox(root,selectbackground='black',selectmode=BROWSE,bd=20,height=20,width=20,font='calibri,30')
listbox4.grid(row=1,column=3,padx=1,columnspan=1,pady=1,ipadx=1,sticky=N)
#listbox4.grid()

songslist.reverse()

realnames.reverse()

artist.reverse()


album.reverse()
genre.reverse()


for items in realnames:
    listbox.insert(0,items)




for item in artist:
    listbox2.insert(0,item)

for albums in album:
    listbox3.insert(0,albums)

for genres in genre:
    listbox4.insert(0,genres)

album.reverse()

artist.reverse()

realnames.reverse()

songslist.reverse()

def doStuff():
    selected = listbox.curselection()
    if selected: # only do stuff if user made a selection
        for index in selected:
            a=listbox2.index(index) # how you get the value of the selection from a listbox
            pygame.mixer.music.load(songslist[a])
            pygame.mixer.music.play()
    
    

photo1 = PhotoImage(file= r'C:\Users\jackwin joseph\Pictures\play sip.png')#"add the desired image path over here"

photoimage = photo1.subsample(10,10)





nextbutton = Button(root,bg='grey',border=0,height=100,width=100,image= photoimage,
                    text = 'Next Song',activeforeground='black',activebackground='green',font='bold')



nextbutton.grid(row=3,column=2,padx=2,pady=2,ipady=2)
#nextbutton.grid()
playa = Button(root,text='play select song',border=0,height=3,width=20,command=doStuff,bg='grey',font='bold')
playa.grid(row=3,column=5,padx=2,columnspan=10,pady=2,ipadx=2,sticky=W)


photo2 = PhotoImage(file= r'C:\Users\jackwin joseph\Pictures\previous button.png')#add the desired image over here

photoimage1 = photo2.subsample(10,10)



previousbutton = Button(root, image =photoimage1, border=0,height = 100,width = 100,fg = 'yellow', text = 'Previous Song', activeforeground = 'black',
                        activebackground = 'white', font = 'times,30',bg='grey')

previousbutton.grid(row = 3, column=1,padx=10,pady=10,ipadx=10,sticky=N)
#previousbutton.grid()



photo3 = PhotoImage(file = r'C:\Users\jackwin joseph\Pictures\stop button.png')#add the desired image over here

photoimage2 = photo3.subsample(10,10)


stopbutton = Button(root,image=photoimage2, height=100, border=0,width=100,
                    text='Stop music', activeforeground = 'black', activebackground = 'dark red',font='times,30',bg='grey')

stopbutton.grid(row=3, column=3,padx=2,pady=2,ipadx=10,sticky=N)
#stopbutton.grid()






#C.grid()

root.configure(background = 'AntiqueWhite1')



nextbutton.bind("<Button-1>",nextsong)


previousbutton.bind("<Button-1>",prevsong)


stopbutton.bind("<Button-1>",stopsong)


root.protocol('WM_DELETE_WINDOW',shutdown)

                                                                                                                                                            
songlabel.grid()

root.mainloop()
