from Plugins.Plugin import Plugin

import time


class BootPlugin(Plugin):
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

                self.matrix.submit_all()

        self.matrix.fill_all((0, 0, 0))
        self.matrix.submit_all()
        print("Fertig")
