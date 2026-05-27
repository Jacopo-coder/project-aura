import random

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

print("Ho capito bene? Le tue statistiche sono: ", forza, agilita, resistenza, divinazione, ingegno, fortuna, "corretto?")

print("Confermi? Digita 'y' se vuoi proseguire, altrimenti 'n' se vuoi ripartire con l'assegnazione dei ricordi")
conferma = input()

if conferma == "y":
    print("I tuoi ricordi sono stabili, l'avventura ha inizio...\n")
    
    prologo = """
    Apri gli occhi lentamente. Senti il crepitio di un fuoco vicino, e una aria calda che ti carezza la pelle.
    Sopra di te vedi le grandi assi di legno e paglia intrecciata che compongono il tetto della capanna in cui ti trovi.
    Alla tua destra, seduto su un basso sgabello noti un vecchio... 
    E' vestito con una lunga tonaca nera, dal cappuccio che porta fuoriescono dei lunghi capelli rossicci, ed una folta
    barba dello stesso colore nasconde gran parte dei suoi lineamenti.

    Appena provi ad alzarti l'anziano uomo sobbalza ed esclama: "Finalmente ti sei svegliato straniero, come ti senti?"
    
    Non ricordi come sei arrivato qui, ma senti che l'energia che scorre in questo 
    luogo risuona con la tua stessa anima. Ti metti a sedere su letto, e guardando questa strana figura rispondi: "Bene... credo."
    "Ma tu chi sei? E come sono finito qui?"
    
    Davanti a te si staglia l'unica stanza di una piccola capanna ricolma di oggetti di tipo, da cesti intrecciati pieni di erbe
    a piccole scaffalature ricoperte di ampolle contenenti liquidi a te sconosciuti.
    Sul fuoco del camino un grande pentolone d'ottone ribolle, vapori profumati permeano l'aria.

    Ti alzi in piedi, ma ti rendi subito contro che forse è troppo presto per fare sforzi, così barcolli fino al tavolo in mezzo alla stanza e ti siedi anche tu su uno sgabello.
    L'uomo ti osserva, e appena ti siedi esclama: "Io sono Aldas, e questa è casa mia. Ti ho portato io qui, con l'auto di un mio giovane amico, Tomash, il figlio del fabbro.
    Ti abbiamo trovato svenuto in mezzo al bosco durante una passeggiata, e non potevamo lasciarti a morire di freddo, così ho deciso di provare a farti rinsavire.
    Siamo ai confini del villaggio di Northermorn, lungo il fiume Ska..."

    Poi si avvicina al pentolone e continua: "E i tuoi indumenti mi fanno intuire che tu non sei di queste parti...
    Quindi dimmi, chi sei tu?"
    """
    print(prologo)

    print(f"Ti schiarisci la voce e rispondi: 'Il mio nome è {nome_giocatore}.'")
    print(f"Aldas ti fissa negli occhi, cercando di scorgere qualcosa nel tuo sguardo...")

    if ingegno > 15:
        print(f"Nota l'attenzione con cui ti guardi intorno: 'Vedo nei tuoi occhi la scintilla della curiosità, {nome_giocatore}...")
    else:
        print("Riempie una tazza con il misterioso infuso del pentolone e te la porge: 'Bevi su, ti farà bene")
    
    print(f"Ma dimmi, {nome_giocatore}, cosa vuoi fare adesso?")
    print("""
        -Bevi l'infuso
        -Fai una domanda
        -Ti guardi intorno
        """)


else:
    print("I tuoi ricordi vacillano, ricominciamo...")

