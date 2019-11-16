#!/usr/local/bin/python3
####################################################
#
# Uebung UT1_GutesPasswort:
# Schreiben Sie ein Programm, welches die Qualität eines
# Passwortes prüft. Dieses muss folgnede Bedingungen erfüllen:
# - Mindestens 1 Grossbuchstabe (prüfen Sie ob die Ordinalzahl >64 und <91 ist)
# - Mindestens 1 Kleinbuchstabe (prüfen Sie ob die Ordinalzahl >96 und <123 ist)
# - Mindestens 1 Zahl (prüfen Sie ob die Ordinalzahl >47 und <58 ist)
# - Mindestens 1 Sonderzeichen
# - Mindestens 6 Zeichen lang
#
####################################################

res = False


def isGoodPassword(password):
    z = [0, 0, 0, 0]  # Anzahl der verschiedenen Zeichentypen
    for c in password:
        a = ord(c)  # Zeichen in ASCII-Nummer umwandeln
        if a > 64 and a < 91:  # Grossbuchstaben zählen
            z[0] = z[0] + 1
        else:
            if a > 96 and a < 123:  # Kleinbuchstaben zählen
                z[1] += 1
            else:
                if a > 47 and a < 58:  # Ziffern zählen
                    z[2] += 1
                else:
                    z[3] += 1  # Sonderzeichen zählen

    return ((z[0] > 0) and (z[1] > 0) and (
        z[2] > 0) and (z[3] > 0) and (sum(z) > 5))


pw = input("Geben Sie ein Passwort ein: ")

while res == False:
    res = isGoodPassword(pw)
    if res == True:
        break
    pw = input(
        "Dieses Passwort entspricht nicht den Kriterien, geben Sie ein neues ein: ")

print("Das Passwort", pw, "ist gut")
