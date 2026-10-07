import csv

class Strumento:
    def __init__(self, Codice, Tipo, Marca, Anno, Valore):
        self.__codice = Codice
        self.__tipo = Tipo
        self.__marca = Marca
        self.__anno = Anno
        self.__valore = Valore

    def __str__(self):
        return f"Codice = {self.__codice}, Tipo = {self.__tipo}, Marca = {self.__marca}, Anno = {self.__anno}, Valore = {self.__valore}"

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

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO -------------DONE--------------

        usedCodes = set(el[1:] for el in self.__strumenti.keys())
        codice = 1
        while codice in usedCodes:
            codice += 1
        #Crea un codice che non sia già stato usato

        self.__strumenti[codice] = [tipo, marca, anno_acquisto, valore]

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO

    @property
    def responsabile(self):
        return self.__responsabile
    def strumenti(self):
        return self.__strumenti

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        """Crea un nuovo responsabile"""
        self.__responsabile = nuovo_responsabile