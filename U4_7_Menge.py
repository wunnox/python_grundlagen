###################################################################
#
# Uebung:
# Erstellen Sie folgendes Tupel:
# a=('Petra','Hans','Fred','Hans','Ursula','Robert','Petra','Ursula','Hans')
# Geben Sie die obigen Namen auf dem Bildschirm so aus, dass jeder
# Name nur einmal erscheint.
#
###################################################################

#### Lösung: ####

# KI-Prompt
# Setze in einem Python Script ein Tupel mit folgendem Inhalt 
# 'Petra','Hans','Fred','Hans','Ursula','Robert','Petra','Ursula','Hans'
# Das Tupel soll in ein Set geladen werden
# Anschliessend soll jeder Name einmal ausgegeben werden

a = ('Petra', 'Hans', 'Fred', 'Hans', 'Ursula', 'Robert', 'Petra', 'Ursula', 'Hans')
s = set(a)
for n in s:
    print(n)
