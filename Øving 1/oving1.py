from sys import stdin


class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 

def spor(kubbe):
    # SKRIV DIN KODE HER
    maksimal = None
    if kubbe is not None:
        maksimal = kubbe.vekt
        while kubbe.neste is not None:
            kubbe = kubbe.neste
            if kubbe.vekt> maksimal:
                maksimal = kubbe.vekt            
    return maksimal
    
# Oppretter lenket liste
    forste = None
    siste = None
    for linje in stdin:
        forrige_siste = siste
        siste = Kubbe(int(linje))
        if forste == None:
            forste = siste
        else:
            forrige_siste.neste = siste
    print spor(forste)

# Kaller loesningsfunksjonen og skriver ut resultatet

