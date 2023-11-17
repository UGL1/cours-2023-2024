from Alarm import Alarme

alarme1 = Alarme("Loritz", "971971971", False) # aucun événement
alarme2 = Alarme("Poincaré", "971971971", True) # idem
alarme1.intrusion() # date est interrogé et renvoie 0000 mais rien n'est consigné
alarme1.activer() # '0001 Activation ' est enregistré dans le journal de alarme1
alarme1.intrusion() # '0002 Intrusion envoi sms au 971971971' aussi
# '971971971 Loritz : 0002 Intrusion' est envoyé par SMS par alarme1
alarme1.desactiver() # '0003 Désactivation ' est enregistré dans le journal de alarme1
alarme2.intrusion() # '0004 Intrusion envoi sms au 971971971' est enregistré dans le journal de alarme2
# '971971971 Poincaré : 0004 Intrusion'  est envoyé par SMS par alarme1

