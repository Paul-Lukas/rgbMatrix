from Plugins.Plugin import Plugin

import time
import os

class BootPlugin(Plugin):
    ry = 0
    rx = 9
    richtungVorher = 3
    richtung = 3    
    def __init__(self, app, matrix):
        super().__init__(app, matrix)
    
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
        
    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):
        def cls():
            os.system('cls' if os.name=='nt' else 'clear')
        cls()    
        

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
            #self.matrix.submit_all()
            Arr[self.ry][self.rx]=Arr[self.ry][self.rx]+(1)
            self.matrix[self.rx, self.ry]=(0, 0, 255)
            self.matrix.submit_all()
            #print (Arr)
        def paintStart():
            #self.matrix.submit_all()
            Arr[0][9]=Arr[0][9]+(1)
            self.matrix[9, 0]=(0, 0, 255)
            self.matrix.submit_all()
            #print (Arr)    
            

        
        paintStart()
        def start():
            
            x=1
            while x<225:
                bewegenRot()
                #bewegenRotUnten()
                #tkFenster.update()
                time.sleep(0.2)
                #print(richtung)
                x= x+1
                
        def mulm(zeit):
            time.sleep(zeit)
            
        def startA():
            z= 0.1
            for a in range (3):
                self.richtungVorher = 3
                self.richtung = 3
                bewegenRot()
                mulm(z)
                
            for aa in range (13):
                self.richtungVorher = 3
                self.richtung = 4
                bewegenRot()
                mulm(z)
                
            for aaa in range (7):
                self.richtungVorher = 4
                self.richtung = 1
                bewegenRot()
                mulm(z)

            for aaaa in range (14):
                self.richtungVorher = 1
                self.richtung = 2
                bewegenRot()
                mulm(z)
                
            for aaaaa in range (29):
                self.richtungVorher = 2
                self.richtung = 3
                bewegenRot()
                mulm(z)
            
        def startAnim():
            self.richtungVorher = 3
            self.richtung = 3
            timew = 0.1
            x=0
            
            while x < 100:
                x=x+1
                bewegenRot()
                time.sleep(timew)
            
            
                
        def bewegenRot():
            
            #richtung = richtungr
            #richtungZVorher=richtungVorherr
            richtungsZdif = self.richtungVorher-self.richtung
            #i = rx
            #j = ry
            #arr[i][0]=1
            #print (arr)
            #print ( richtungsZdif )
            #print ( "-----------------------------------------")
            if not( richtungsZdif == 2 or richtungsZdif == -2 ):
            #x=1
            #if ( x==1):
                if (self.richtung == 1):
                    self.ry = self.ry-1
                    if ( self.ry >= 0 ):
                        paint()
                    elif ( self.ry < 0 ):
                        self.ry = 29
                        paint()
                    
                
                if (self.richtung == 2):
                    self.rx = self.rx+1
                    if ( self.rx <= 14 ):
                        paint()
                    elif ( self.rx > 14 ):
                        self.rx = 0
                        paint()
                        
                if (self.richtung == 3):
                    self.ry = self.ry+1
                    if ( self.ry <= 29 ):
                        paint()
                    elif ( self.ry > 29 ):
                        self.ry = 0
                        paint()
                        
                        
                if (self.richtung == 4):
                    self.rx = self.rx-1
                    if ( self.rx >= 0 ):
                        paint()
                    elif ( self.rx < 0 ):
                        self.rx = 14
                        paint()
            else:
                self.richtung = self.richtungVorher;
           


        def richtungAendernO():
            
            if not (self.richtung == 1):
                self.richtungVorher = self.richtung
                self.richtung = 1
            elif (self.richtungVorher == 3):
                self.richtung = 3
            else:
                pass;
            #print(self.richtung)

        def richtungAendernR():
            
            if not (self.richtung == 2):
                self.richtungVorher = self.richtung
                self.richtung = 2
            elif (self.richtungVorher == 4):
                self.richtung = 4
            else:
                pass;
            #print(self.richtung)

        def richtungAendernU():
            
            if not (self.richtung == 3):
                self.richtungVorher = self.richtung
                self.richtung = 3
            elif (self.richtungVorher == 1):
                self.richtung = 1
            else:
                pass;
            #print(self.richtung)

        def richtungAendernL():
           
            if not (self.richtung == 4):
                self.richtungVorher = self.richtung
                self.richtung = 4
            elif (self.richtungVorher == 2):
                self.richtung = 2
            else:
                pass;
            #print(self.richtung)



        

            
        wand=[]
        reihe=[]
        for i in range(30):
            reihe=[]
            for i in range (15):
                reihe = reihe+[(100,100,100)]
            wand = wand+[reihe]
        startA()
        #fuellen()
        #paint()
        self.matrix.submit_all()
