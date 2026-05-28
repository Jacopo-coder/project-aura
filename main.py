from creazione_personaggio import crea_personaggio
from prologo import avvia_prologo

while True:
    nome_giocatore, forza, agilita, resistenza, divinazione, ingegno, fortuna = crea_personaggio()

    conferma = input("\nSei soddisfatto dei tuoi ricordi? (y/n): ").strip().lower()
    

    if conferma == "y":

        break
    else:
        print("\nI tuoi ricordi vacillano... Ricominciamo da capo!\n")

avvia_prologo(nome_giocatore, ingegno)



