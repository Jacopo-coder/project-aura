import random

def crea_personaggio():
    print("Benvenuto avventuriero!")
    nome_giocatore = input("Quale è il tuo nome?")
    print("Capisco, quindi il tuo nome è", nome_giocatore,", ho capito bene?")
    print("Ti sei appena svegliato da un lungo sonno, ricordi le tue caratteristiche?")

    stat_1 = random.randint(1, 25)
    stat_2 = random.randint(1, 25)
    stat_3 = random.randint(1, 25)
    stat_4 = random.randint(1, 25)
    stat_5 = random.randint(1, 25)
    stat_6 = random.randint(1, 25)

    print("Ecco i ricordi delle tue caratteristiche: ",stat_1, stat_2, stat_3, stat_4, stat_5, stat_6, "assegna un valore ad ognuna...")

    dadi_disponibili = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]

    print("Forza: ")
    forza = int(input())
    while forza not in dadi_disponibili:
        print("Numero non valido o già usato!")
        forza = int(input("Riprova: "))
    dadi_disponibili.remove(forza)

    print("Ti sono rimasti questi ricordi da assegnare: ",dadi_disponibili)

    print("Agilita: ")
    agilita = int(input())
    while agilita not in dadi_disponibili:
        print("Numero non valido o già usato!")
        agilita = int(input("Riprova: "))
    dadi_disponibili.remove(agilita)

    print("Ti sono rimasti questi ricordi da assegnare: ",dadi_disponibili)

    print("Resistenza: ")
    resistenza = int(input())
    while resistenza not in dadi_disponibili:
        print("Numero non valido o già usato!")
        resistenza = int(input("Riprova: "))
    dadi_disponibili.remove(resistenza)

    print("Ti sono rimasti questi ricordi da assegnare: ",dadi_disponibili)

    print("Divinazione: ")
    divinazione = int(input())
    while divinazione not in dadi_disponibili:
        print("Numero non valido o già usato!")
        divinazione = int(input("Riprova: "))
    dadi_disponibili.remove(divinazione)

    print("Ti sono rimasti questi ricordi da assegnare: ",dadi_disponibili)

    print("Ingegno: ")
    ingegno = int(input())
    while ingegno not in dadi_disponibili:
        print("Numero non valido o già usato!")
        ingegno = int(input("Riprova: "))
    dadi_disponibili.remove(ingegno)

    print("Ti è rimasto un solo ricordo...")

    print("L'ultimo frammento dei tuoi ricordi si assesta...")
    fortuna = dadi_disponibili[0]
    dadi_disponibili.remove(fortuna)

    return nome_giocatore, forza, agilita, resistenza, divinazione, ingegno, fortuna