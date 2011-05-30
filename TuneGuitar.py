import appuifw
import e32
import audio
import os
import graphics
import key_codes 





def exit_key_handler():
    app_lock.signal()
    global running
    running = 0
    #app_lock = e32.Ao_lock()



BLACK = (0,0,0)
filepathe = u"C:\\Data\\Sounds\\Digital\\e.mid"
filepathb = u"C:\\Data\\Sounds\\Digital\\b.mid"
filepathg = u"C:\\Data\\Sounds\\Digital\\g.mid"
filepathd = u"C:\\Data\\Sounds\\Digital\\d.mid"
filepatha = u"C:\\Data\\Sounds\\Digital\\a.mid"
filepathae = u"C:\\Data\\Sounds\\Digital\\ae.mid"
filename = u"C:\\Data\\Sounds\\Digital\\record.wav"
filepathe2 = u"C:\\Data\\Sounds\\Digital\\e2.mid"
filepathb2 = u"C:\\Data\\Sounds\\Digital\\b2.mid"
filepathg2 = u"C:\\Data\\Sounds\\Digital\\g2.mid"
filepathd2 = u"C:\\Data\\Sounds\\Digital\\d2.mid"
filepatha2 = u"C:\\Data\\Sounds\\Digital\\a2.mid"
filepathae2 = u"C:\\Data\\Sounds\\Digital\\ae2.mid"
bgimage = graphics.Image.open(u"C:\\Data\\Images\\music1.jpg")


def handle_redraw(rect):canvas.blit(bgimage)
canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
appuifw.app.body=canvas

"""def handle_redraw(rect):    
   canvas.blit(img)
def draw_screen():
 
       #Set the screen to full
       appuifw.app.screen = 'full' 
 
       #Global variable for application UI
       global canvas
 
       #Create an instance of Canvas and set it as the application's body
 
       canvas = appuifw.Canvas(redraw_callback=handle_redraw)    
       appuifw.app.body = canvas
       
 
       #Global variable for application UI
       global img
       img = graphics.Image.new(canvas.size)
        
       #Clear the image
       img.clear(BLACK)
       handle_redraw(None)
       
draw_screen()

"""

def item1():
    global S
    S=audio.Sound.open(filename)
    S.record()
    appuifw.query(u"Press OK to stop recording", "query")
    print "Sounds Great!! Play from Menu"
    S.stop()
    

def item2 ():
    global S
    try:
        S=audio.Sound.open(filename)
        S.play()
        appuifw.query(u"Press OK to stop ", "query")
        S.stop()
        print u"Playing Stopped"
        print u"Delete from Menu"
    except:
        print"Record something first!"
    
        

def item3():
    os.remove(filename)
    appuifw.note(u"Deleted", "conf")
    
    
def subitem1():
    global sound
    #S.stop()
    #sb.stop()
    #sg.stop()
    sound = audio.Sound.open(filepathe)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem2():
    global sound
    #S.stop()
    #se.stop()
    #sg.stop()
    sound = audio.Sound.open(filepathb)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem3():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathg)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem4():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathd)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem5():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepatha)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem6():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathae)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem11():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathe2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem22():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathb2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem33():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathg2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem44():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathd2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem55():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepatha2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

def subitem66():
    global sound
    #S.stop()
    #se.stop()
    #sb.stop()
    sound = audio.Sound.open(filepathae2)
    sound.play(audio.KMdaRepeatForever)
    appuifw.query(u"Press OK to stop", "query")
    sound.stop()

# To add the functionality of Keypressed

canvas.bind(key_codes.EKey1, subitem1)
canvas.bind(key_codes.EKey2, subitem2)
canvas.bind(key_codes.EKey3, subitem3)
canvas.bind(key_codes.EKey4, subitem4)
canvas.bind(key_codes.EKey5, subitem5)
canvas.bind(key_codes.EKey6, subitem6)
canvas.bind(key_codes.EKey0, item1)


    


    
    
appuifw.app.screen='normal'
appuifw.app.title = u"iMUSIC"

#def quit():
    #script_lock.signal()
    #appuifw.app.set_exit()
    #----app_lock.signal()
app_lock = e32.Ao_lock()
    


appuifw.app.menu = [(u"Record", item1),(u"Play",item2),(u"Delete",item3),
                    (u"Tune Acoustic Guitar", ((u"Tune E(high)", subitem1),
                                    (u"Tune B", subitem2),
                                    (u"Tune G", subitem3),
                                    (u"Tune D", subitem4),
                                    (u"Tune A", subitem5),
                                    (u"Tune E(low)", subitem6))),
                    (u"Tune Electric Guitar",((u"Tune E(high)", subitem11),
                                    (u"Tune B", subitem22),
                                    (u"Tune G", subitem33),
                                    (u"Tune D", subitem44),
                                    (u"Tune A", subitem55),
                                    (u"Tune E(low)", subitem66)))]


appuifw.app.exit_key_handler = exit_key_handler
app_lock.wait()
#appuifw.app.exit_key_handler=quit
#script_lock = e32.Ao_lock()
#script_lock.wait()
#--appuifw.app.exit_key_handler = exit_key_handler
#--app_lock.wait()
#--e32.ao_yield()
