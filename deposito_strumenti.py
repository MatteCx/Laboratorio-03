import csv
from operator import itemgetter
from datetime import datetime

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO --------------DONE----------------
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = {}
        self.__prestiti = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO -------------DONE--------------
        try:
            with open(file_path) as csvfile:
                file = csv.reader(csvfile, delimiter=',')
                for riga in file:
                    self.__strumenti[riga[0]] = [riga[1], riga[2], riga[3], riga[4]]
        except FileNotFoundError:
            print(f"Impossibile trovare il file (FileNotFoundError)")
            exit()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO -------------DONE--------------
        codice = 1
        while codice in set(el[1:] for el in self.__strumenti.keys()): codice += 1
        scodice = "S" + str(codice)
        #Crea un codice che non sia già stato usato
        self.__strumenti[scodice] = [tipo, marca, anno_acquisto, valore]

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO -------------DONE----------------
        return sorted([el for el in self.__strumenti.items()], key = itemgetter(2))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO ------------DONE----------------
        if id_strumento not in set(el for el in self.__strumenti.keys()):
            raise NameError("Il codice strumento non è presente nel deposito")
        elif id_strumento not in set(el[1] for el in self.__prestiti.items()):
            raise NameError("Lo strumento risulta in prestito ad un altro allievo")
        n_prestito = 1
        while n_prestito in set(int(el[1:]) for el in self.__prestiti.keys()): n_prestito += 1
        id_prestito = "P"+str(n_prestito)
        # Crea un id_prestito che non sia già stato usato
        self.__prestiti[id_prestito] = [data, id_strumento, cognome_allievo]

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO -------------DONE----------------
        try:
            self.__prestiti.pop(id_prestito)
        except KeyError:
            raise Exception("Il codice ID inserito non risulta collegato a nessun prestito")

    @property
    def responsabile(self):
        return self.__responsabile
    def strumenti(self):
        return self.__strumenti

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        """Crea un nuovo responsabile"""
        self.__responsabile = nuovo_responsabile