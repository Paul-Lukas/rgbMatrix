from Plugins.Plugin import Plugin

import time


class ButtPlug(Plugin):
    def __init__(self, app, matrix):
        super().__init__(app, matrix)


    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):

        #self.matrix wird beim ausführen des super constructors gesetzt
        #self.matrix ist eine Instanz der matrix Klasse zu finden in Libraries/matrix.py
        #Eine beschreibung aller Methoden ist btw auch in Libraries/matrix.py zu findes, nur so btw
        #fill_all setzt alles auf eine Farbe, die Farbe muss als tupel mit 3 werten angegeben werden. RGB halt
        self.matrix.fill_all((0, 0, 0))
        time.sleep(1)
        # R
        self.matrix.fill_all((255, 0, 0))
        time.sleep(1)
        # G
        self.matrix.fill_all((0, 255, 0))
        time.sleep(1)
        # B
        self.matrix.fill_all((0, 0, 255))
        time.sleep(1)

        #Weiß
        self.matrix.fill_all((255, 255, 255))
        time.sleep(1)
        #Alles Löschen / Schwarz
        self.matrix.fill_all((0, 0, 0))
        time.sleep(1)

        #self.matrix[x, y] = (r, g, b) Setzt den Pixel mit der koordinate x, y auf den wert aus der Klammer
        #Die Änderung ist noch nicht zu sehen, aber vorgemerkt, sie wird mit submit_all an das Bord übertragen
        self.matrix[0, 0] = (0, 0, 255)
        self.matrix[14, 0] = (0, 255, 255)
        self.matrix[0, 29] = (0, 255, 255)
        self.matrix[14, 29] = (0, 255, 0)

        self.matrix.submit_all()

        time.sleep(2)

        #Wenn du eine Variable VOR self.matrix[x, y] stehen hast, dann nimmt diese Variable den tupel wert an
        #Achtung, es werden die gemerkten werte zurück gegeben, sprich das bord kann anders sein, falls noch nicht submit_all aufgerufen wurde
        farbwert = self.matrix[0, 0]


        #Die Letzte Möglickeit, für die ich aber gerade leider keine gescheite Anwendung hab ist es, dass ganze Array zu Tauschen
        testMatrix = [[(0, 0, 0) for j in range(15)] for i in range(30)]

        self.matrix.set_matrix(testMatrix)
        #Auch danach submitt_all machen
        self.matrix.submit_all()


        for i in range(30):
            for j in range(15):
                if (i + j) % 2 == 0:
                    self.matrix[j, i] = (255, 0, 0)
                else:
                    self.matrix[j, i] = (0, 0, 255)

                time.sleep(0.25)
                self.matrix.submit_all()

        self.matrix.fill_all((0, 0, 0))
        self.matrix.submit_all()
        print("Fertig")

def fuellen():
    wand=[]
    reihe=[]
    for i in range(30):
        reihe=[]
        for i in range (15):
            reihe = reihe+[(255,255,255)]
        wand = wand+[reihe]
    for zeile in range (30):    #wand[zeile][i][...]
        for i in range (15):
        #'#%02x%02x%02x' % (wand[zeile][i][0],1,2)
            #canvas.create_rectangle(11+20*i, 11+zeile*20, 29+20*i, 29+zeile*20, fill='#%02x%02x%02x' % (wand[zeile][i][0],wand[zeile][i][1],wand[zeile][i][2]))
            self.matrix[zeile, i]=(wand[zeile][i][0], wand[zeile][i][1], wand[zeile][i][2])
    y=29        
    x=9
    z=6
    #canvas.create_rectangle(11+20*x,11+0*20,29+20*x, 29, fill='#%02x%02x%02x' % (255,0,0))
    #canvas.create_rectangle(11+20*z,11+y*20,29+20*z,29+y*20, fill='#%02x%02x%02x' % (0,0,255))
    self.matrix[0, 9]=(255, 0, 0)
    self.matrix[29, 6]=(0, 0, 255)
    global ry
    ry = 0
    global rx
    rx = 9

    Arr=[]
    laenge=[]
    for i in range(30):
        laenge=[]
        for i in range (15):
            laenge = laenge+[(0)]
        Arr = Arr+[laenge]
    print (Arr)
    #Arr[1][1]=Arr[1][1]+(1)
    #print (Arr)
    self.matrix.submit_all()

Arr=[]
laenge=[]
for i in range(30):
    laenge=[]
    for i in range (15):
        laenge = laenge+[(0)]
    Arr = Arr+[laenge]
#print (Arr)
#Arr[1][1]=Arr[1][1]+(1)
#print (Arr)
    
def paint():
    global rx
    global ry
    global Arr
    Arr[ry][rx]=Arr[ry][rx]+(1)
    self.matrix[ry, rx]=(0, 0, 255)
    self.matrix.submit_all()
    print (Arr)
    
    

ry = 0
rx = 9

def start():
    global richtung
    global richtungZVorher
    x=1
    while x<225:
        bewegenRot()
        #bewegenRotUnten()
        #tkFenster.update()
        time.sleep(0.2)
        #print(richtung)
        x= x+1
    
        
        
def bewegenRot():
    global ry
    global rx
    global richtung
    global richtungVorher
    #richtung = richtungr
    #richtungZVorher=richtungVorherr
    richtungsZdif = richtungVorher-richtung
    #i = rx
    #j = ry
    #arr[i][0]=1
    #print (arr)
    print ( richtungsZdif )
    print ( "-----------------------------------------")
    if not( richtungsZdif == 2 or richtungsZdif == -2 ):
    #x=1
    #if ( x==1):
        if (richtung == 1):
            ry = ry-1
            if ( ry >= 0 ):
                paint()
            elif ( ry < 0 ):
                ry = 29
                paint()
            
        
        if (richtung == 2):
            rx = rx+1
            if ( rx <= 14 ):
                paint()
            elif ( rx > 14 ):
                rx = 0
                paint()
                
        if (richtung == 3):
            ry = ry+1
            if ( ry <= 29 ):
                paint()
            elif ( ry > 29 ):
                ry = 0
                paint()
                
                
        if (richtung == 4):
            rx = rx-1
            if ( rx >= 0 ):
                paint()
            elif ( rx < 0 ):
                rx = 14
                paint()
    else:
        richtung = richtungVorher;
   


def richtungAendernO():
    global richtung
    global richtungVorher
    if not (richtung == 1):
        richtungVorher = richtung
        richtung = 1
    elif (richtungVorher == 3):
        richtung = 3
    else:
        pass;
    print(richtung)

def richtungAendernR():
    global richtung
    global richtungVorher
    if not (richtung == 2):
        richtungVorher = richtung
        richtung = 2
    elif (richtungVorher == 4):
        richtung = 4
    else:
        pass;
    print(richtung)

def richtungAendernU():
    global richtung
    global richtungVorher
    if not (richtung == 3):
        richtungVorher = richtung
        richtung = 3
    elif (richtungVorher == 1):
        richtung = 1
    else:
        pass;
    print(richtung)

def richtungAendernL():
    global richtung
    global richtungVorher
    if not (richtung == 4):
        richtungVorher = richtung
        richtung = 4
    elif (richtungVorher == 2):
        richtung = 2
    else:
        pass;
    print(richtung)



richtungVorher = 3
richtung = 3

    
wand=[]
reihe=[]
for i in range(30):
    reihe=[]
    for i in range (15):
        reihe = reihe+[(0,0,0)]
    wand = wand+[reihe]