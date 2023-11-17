from utils import date, envoie_sms

ACTIVE = True
INACTIVE = False


class Alarme2:
    def __init__(self, lieu, telephone, etat):
        self.lieu = lieu
        self.telephone = telephone
        self.active = etat
        self.journal = []

    def intrusion(self):
        evenement = date() + " Intrusion"
        if self.active:
            sms = self.lieu + ' : ' + evenement
            if envoie_sms(self.telephone, sms):
                evenement = evenement + " envoi sms au " + self.telephone
            else:
                evenement += " envoi au " + self.telephone + "échoué"
        self.journal.append(evenement)

    def activer(self):
        self.active = ACTIVE
        evenement = date() + " Activation "
        self.journal.append(evenement)

    def desactiver(self):
        self.active = INACTIVE
        evenement = date() + " Désactivation "
        self.journal.append(evenement)

    def efface_journal(self):
        self.journal = []
