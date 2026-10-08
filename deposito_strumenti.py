import csv
from operator import itemgetter

class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.__id_prestito = id_prestito
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.__id_prestito:^4} {self.__data:^6} {self.__id_strumento:^4} {self.__cognome_allievo:<20}"

    def lista_prestito(self):
        return [self.__id_prestito, self.__data, self.__id_strumento, self.__cognome_allievo]

    @property
    def id_prestito(self):
        return self.__id_prestito
    @property
    def id_strumento(self):
        return self.__id_strumento

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore

    def __str__(self):
        return f"{self.__codice:^4} {self.__tipo:<25} {self.__marca:<15} {self.__anno_acquisto:^6} {float(self.__valore)}"

    def lista_prestito(self):
        return [self.__codice, self.__tipo, self.__marca, self.__anno_acquisto, self.__valore]

    @property
    def codice(self):
        return self.__codice

    @property
    def marca(self):
        return self.__marca

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO --------------DONE----------------
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO -------------DONE--------------
        try:
            with open(file_path) as csvfile:
                file = csv.reader(csvfile, delimiter=',')
                for riga in file:
                    self.__strumenti.append(Strumento(riga[0], riga[1], riga[2], riga[3], riga[4]))
        except FileNotFoundError:
            print(f"Impossibile trovare il file (FileNotFoundError)")
            exit()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO -------------DONE--------------
        codice = 1
        while codice in set(int(el.codice[1:]) for el in self.__strumenti): codice += 1
        scodice = "S" + str(codice)
        s = Strumento(scodice, tipo, marca, anno_acquisto, valore)
        self.__strumenti.append(s)
        return s.__str__()

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO -------------DONE----------------
        Lista = sorted([el.lista_prestito() for el in self.__strumenti], key = itemgetter(2))
        return Lista

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO ------------DONE----------------
        if id_strumento not in set(el.codice for el in self.__strumenti):
            raise NameError("Il codice strumento non è presente nel deposito")
        elif id_strumento in set(el.id_strumento for el in self.__prestiti):
            raise NameError("Lo strumento risulta in prestito ad un altro allievo")
        n_prestito = 1
        while n_prestito in set(int(el.id_prestito[1:]) for el in self.__prestiti): n_prestito += 1
        id_prestito = "P" + str(n_prestito)
        # Crea un id_prestito che non sia già stato usato
        self.__prestiti.append(Prestito(id_prestito, data, id_strumento, cognome_allievo))
        return True

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO -------------DONE----------------
        try:
            complex = [self.__prestiti.index(el) for el in self.__prestiti if el.id_prestito == id_prestito]
            indice = complex[0]
            # for el in self.__prestiti:
            # if el.id_prestito == id_prestito: indice = self.__strumenti.index(el)
            self.__prestiti.pop(indice)
        except IndexError:
            print(f"Il codice prestito inserito non è associato a nessun prestito")
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