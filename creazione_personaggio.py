import random

def calcola_statistica():
    lanci = []
    for lancio in range(4):
        numero_estratto = random.randint(1, 8)
        lanci.append(numero_estratto)
    lanci.sort()
    lanci.pop(0)
    return sum(lanci)

def chiedi_statistica(nome_statistica, dadi_disponibili):
    print(f"\n{nome_statistica}: ")
    scelta = input()
    
    if scelta.lower() == "ricomincia":
        return "RESET"
        
    while not scelta.isdigit() or int(scelta) not in dadi_disponibili:
        if scelta.lower() == "ricomincia":
            return "RESET"
        print("Numero non valido o inserimento sbagliato!")
        scelta = input(f"Riprova {nome_statistica} o scrivi 'ricomincia' per ripartire da capo: ")
        
    return int(scelta)

def crea_personaggio():
    
    print("==================================================")
    print("                  PROJECT-AURA                    ")
    print("       Un gioco di ruolo testuale ideato da       ")
    print("             JACOPO 'TAKESHI' BITOSSI             ")
    print("                Versione 1.0 [2026]               ")
    print("==================================================\n")
    
    print("Svegliati... Come ti chiami, viandante?")
    nome_giocatore = input()

    stat_1 = calcola_statistica()
    stat_2 = calcola_statistica()
    stat_3 = calcola_statistica()
    stat_4 = calcola_statistica()
    stat_5 = calcola_statistica()
    stat_6 = calcola_statistica()

    print(f"\n{nome_giocatore}, ecco i ricordi delle tue caratteristiche: ")
    print(stat_1, stat_2, stat_3, stat_4, stat_5, stat_6)
    print("Assegna un valore ad ognuna...")

    dadi_disponibili = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]
    
    forza = chiedi_statistica("Forza", dadi_disponibili)
    if forza == "RESET":
        print("\nI tuoi ricordi sono confusi... Ricominciamo...\n")
        return crea_personaggio()
    dadi_disponibili.remove(forza)

    print("Ti sono rimasti questi ricordi da assegnare: ", dadi_disponibili)

    agilita = chiedi_statistica("Agilità", dadi_disponibili)
    if agilita == "RESET":
        print("\nI tuoi ricordi sono confusi... Ricominciamo...\n")
        return crea_personaggio()
    dadi_disponibili.remove(agilita)

    print("Ti sono rimasti questi ricordi da assegnare: ", dadi_disponibili)

    resistenza = chiedi_statistica("Resistenza", dadi_disponibili)
    if resistenza == "RESET":
        print("\nI tuoi ricordi sono confusi... Ricominciamo...\n")
        return crea_personaggio()
    dadi_disponibili.remove(resistenza)

    print("Ti sono rimasti questi ricordi da assegnare: ", dadi_disponibili)

    divinazione = chiedi_statistica("Divinazione", dadi_disponibili)
    if divinazione == "RESET":
        print("\nI tuoi ricordi sono confusi... Ricominciamo...\n")
        return crea_personaggio()
    dadi_disponibili.remove(divinazione)

    print("Ti sono rimasti questi ricordi da assegnare: ", dadi_disponibili)

    ingegno = chiedi_statistica("Ingegno", dadi_disponibili)
    if ingegno == "RESET":
        print("\nI tuoi ricordi sono confusi... Ricominciamo...\n")
        return crea_personaggio()
    dadi_disponibili.remove(ingegno)

    print("L'ultimo frammento dei tuoi ricordi si assesta... Ecco la tua fortuna...")
    fortuna = dadi_disponibili[0]
    dadi_disponibili.remove(fortuna)

    personaggio = {
        "nome": nome_giocatore,
        "forza": forza,
        "agilita": agilita,
        "resistenza": resistenza,
        "divinazione": divinazione,
        "ingegno": ingegno,
        "fortuna": fortuna
    }

    return personaggio

mio_personaggio = crea_personaggio()

print("\nPERSONAGGIO SALVATO")
print(mio_personaggio)