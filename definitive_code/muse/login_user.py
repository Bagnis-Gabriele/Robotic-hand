import csv
def login():
    print("--------------------------------------")
    print("LOGIN")
    print("--------------------------------------")
    with open("user.csv", "a") as data_file:
        pass    #controllo se esiste
    with open("user.csv", "r") as data_file:
        reader = csv.reader(data_file)
        count = 1
        utenti = []
        for header in reader:
            if(header[0]!=None):
                print (str(count) + ". " + header[0])
                utenti.append(header[0])
                count+=1
    ok=False
    while (ok==False):        
        scelta = input("selezionare un utente, per crearne uno inserire 0: ")
        ok = True
        if(int(scelta) < 0 or int(scelta) > count-1):
            ok=False
            print("l'utente selezionato non esiste")

    #aggiunta nuovo utente
    if(int(scelta) == 0):
        with open("user.csv", newline='', mode='a') as data_file:
            fileCSV = csv.writer(data_file)
            ok = False
            while (ok == False):
                nome = input("inserire il nuovo utente: ")
                ok = True
                if (nome in utenti):
                    ok = False
                    print("utente già registrato")

            fileCSV.writerow([nome])
        f = "utenti\\" + nome + ".csv"
        with open(f, newline='', mode='a') as data_file:
            fileCSV = csv.writer(data_file)
            fileCSV.writerow(['delta','theta','alpha','beta','mano'])

    #selezione utente
    if(int(scelta) != 0):
        nome = utenti[int(scelta)-1]

    return str(nome)
