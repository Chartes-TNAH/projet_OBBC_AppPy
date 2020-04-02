"""
TEST AREA

Author : Lucas Terriel
Date: 31/03/2020

"""



# Tentative pour faire un moteur de recherche plein texte full-lxml


from lxml import etree

# mettre son document xml

source_doc = etree.parse(
    "/Users/lucasterriel/Desktop/projet_barzaz-breiz"
    "/OBBC/app/data_xml-xslt/Barzaz-Breiz.xml")


titres = source_doc.findall("//div[@type='chanson']/head")
transcriptions = source_doc.findall("//div[@type='chanson']"
                                    "/div[@type = 'transcription']/lg/*")
originaux = source_doc.findall("//div[@type='chanson']"
                               "/div[@type = 'original']/lg/*")

# tentative de xpath pour recupérer l'id
# après la transcription mais parent:: ne marche pas

transcriptions_n = source_doc.findall("//div[@type='chanson']/"
                                      "div[@type = 'transcription']/parent::div/@n")

resultats = []


keyword = input("Entrer votre recherche : ")

# pas obligatoire c'est parceque mes titres sont entierement en majuscules
if keyword == keyword.lower():
    keyword = keyword.upper()

for transcription in transcriptions:
    if keyword in transcription.text:
        TRANSCRIPTION = transcription.text
        resultats.append(TRANSCRIPTION)

print(resultats)

"""

def start():
    keyword = input("Entrer votre recherche : ")

    if keyword == keyword.lower():
    	keyword = keyword.upper()

    for titre in titres:
        if keyword in titre.text:
            TITRE = titre.text
            resultats.append(TITRE)
    print(resultats)
    resultats[:] = [] 

continuer = True
while continuer:
    start()
    continuer = input("On continue? (o/n) ").lower() in ("o", "oui")

"""