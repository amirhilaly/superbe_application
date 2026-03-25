import emailSender
import URSSAF, FISC
CV = open("CV.pdf") # oui oui, .pdf, python c'est trop fort ca peut faire ca
entreprises = open("entreprises.txt")

for entreprise in entreprises:
    emailSender.CV(entreprise)
    if emailSender.response == "non":
        emailSender.reply(URSSAF.threat, FISC.threat)

    
