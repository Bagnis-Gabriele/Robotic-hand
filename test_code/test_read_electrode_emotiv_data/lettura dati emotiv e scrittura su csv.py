from pyemotiv import Epoc
import time
import numpy as np
import keyboard
import csv

esc = False

with open("avanti.csv", "wb") as csvavanti:
    avanti = csv.writer(csvavanti)
    with open("indietro.csv" , "wb") as csvindietro:
        indietro = csv.writer(csvindietro)

        time_passed = 0.0

        epoc = Epoc()
        while not esc:
            data = epoc.get_raw()

            if(keyboard.is_pressed('q')):
                esc = True

            if(keyboard.is_pressed('a')):
                print "INVIO AVANTI"

                avanti.writerow([str(time_passed) , 'af3, ' , str(np.average(data[0]))])
                avanti.writerow([str(time_passed) , 'f7, ' ,  str(np.average(data[1]))])
                avanti.writerow([str(time_passed) , 'f3, ' ,  str(np.average(data[2]))])
                avanti.writerow([str(time_passed) , 'fc5, ' ,  str(np.average(data[3]))])
                avanti.writerow([str(time_passed) , 't7, ' ,  str(np.average(data[4]))])
                avanti.writerow([str(time_passed) , 'p7, ' ,  str(np.average(data[5]))])
                avanti.writerow([str(time_passed) , 'o1, ' ,  str(np.average(data[6]))])
                avanti.writerow([str(time_passed) , 'o2, ' ,  str(np.average(data[7]))])
                avanti.writerow([str(time_passed) , 'p8, ' ,  str(np.average(data[8]))])
                avanti.writerow([str(time_passed) , 't8, ' ,  str(np.average(data[9]))])
                avanti.writerow([str(time_passed) , 'fc6, ' ,  str(np.average(data[10]))])
                avanti.writerow([str(time_passed) , 'f4, ' ,  str(np.average(data[11]))])
                avanti.writerow([str(time_passed) , 'f8, ' ,  str(np.average(data[12]))])
                avanti.writerow([str(time_passed) , 'af4, ' ,  str(np.average(data[13]))])

            if(keyboard.is_pressed('z')):
                print "INVIO INDIETRO"

                indietro.writerow([str(time_passed) , 'af3, ' , str(np.average(data[0]))])
                indietro.writerow([str(time_passed) , 'f7, ' ,  str(np.average(data[1]))])
                indietro.writerow([str(time_passed) , 'f3, ' ,  str(np.average(data[2]))])
                indietro.writerow([str(time_passed) , 'fc5, ' ,  str(np.average(data[3]))])
                indietro.writerow([str(time_passed) , 't7, ' ,  str(np.average(data[4]))])
                indietro.writerow([str(time_passed) , 'p7, ' ,  str(np.average(data[5]))])
                indietro.writerow([str(time_passed) , 'o1, ' ,  str(np.average(data[6]))])
                indietro.writerow([str(time_passed) , 'o2, ' ,  str(np.average(data[7]))])
                indietro.writerow([str(time_passed) , 'p8, ' ,  str(np.average(data[8]))])
                indietro.writerow([str(time_passed) , 't8, ' ,  str(np.average(data[9]))])
                indietro.writerow([str(time_passed) , 'fc6, ' ,  str(np.average(data[10]))])
                indietro.writerow([str(time_passed) , 'f4, ' ,  str(np.average(data[11]))])
                indietro.writerow([str(time_passed) , 'f8, ' ,  str(np.average(data[12]))])
                indietro.writerow([str(time_passed) , 'af4, ' ,  str(np.average(data[13]))])

            time.sleep(1./2048.)
            time_passed += 1./2048.



