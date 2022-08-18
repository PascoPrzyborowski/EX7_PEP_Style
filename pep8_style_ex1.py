import time

#ohne pep8 style
print()
x = "Arbeitsbeschaffungsmakro für Word oder Excel. Ersetze A durch E und umgekehrt! viel Spaß im Büro mit langen Texten wieder rück zu verwandeln!"
print(x)
time.sleep(1)
x = x.replace("a", "e")
x = x.replace("e", "a")
x = x.replace("A", "E")
x = x.replace("E", "A")
y = x
print()
print("Text nach dem Austauschen :")
print()
print(y)
print()
time.sleep(1)



#mit pep8  style
print()
ausgabetext = "Arbeitsbeschaffungsmakro für Word oder Excel \
               Ersetze A durch E und umgekehrt! \
               viel Spaß im Büro mit langen Texten wieder rück zu verwandeln!"
               #Ausgabetext unverändert.

print(ausgabetext) # Ausgabe
time.sleep(1)

ausgabetext = ausgabetext.replace("a", "e")
ausgabetext = ausgabetext.replace("e", "a")
ausgabetext = ausgabetext.replace("A", "E")
ausgabetext = ausgabetext.replace("E", "A")
# Ersetze a durch e im text und umgekehrt für Groß und Kleinschreibung (Blockanweisung)

print()
print("Text nach dem Austauschen :")
print()
print(ausgabetext) #Ausgabe veränderter Text
print()
time.sleep(1)