

date_number = -1


def date():
    global date_number
    date_number += 1
    return str(date_number).zfill(4)


def envoie_sms(x, y):
    print(x , y)
    return True
