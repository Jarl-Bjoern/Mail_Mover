from HF import *

# Variablen_Bereich
Pfad_Analyse = r'C:\ProgramData\Net at Work Mail Gateway\Temporary Files\MailQueues'

# Funktionen
def Initialien():
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ('               		      Mail-Mover')
    print ('                              Version 0.1')
    print ('                             Rainer Herold')
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def Meta_Analyse(Kollege = ""):
    try: mkdir('C:/Mails')
    except FileExistsError: pass

    try:
        for root, _, files in walk(Pfad_Analyse, topdown=False):
            for file in files:
                if (file.endswith('.metadata')):
                    try: Datei = open(join(root, file), 'r')
                    except UnicodeDecodeError: Datei = open(join(root, file), 'r', encoding='utf-8')
                    except UnicodeEncodeError: Datei = open(join(root, file), 'r', encoding='utf-8')
                    Text = Datei.readlines()
                    Datei.close()

                    for Name in finditer('"recipient":{"address":{"localPart":"', str(Text)):
                        Startposition = Name.span()[1]
                        for i in str(Text)[Startposition:]:
                            if (i != '"'): Kollege += i
                            else: break

                    try: makedirs(rf'C:/Mails/{Kollege}')
                    except FileExistsError: pass

                    try:
                        copy(join(root, file), f'C:/Mails/{Kollege}/{file}', follow_symlinks=True)
                        print (f'Die Datei {file} wurde erfolgreich kopiert.')
                        copy(f'{join(root, file[:-9])}.eml', f'C:/Mails/{Kollege}/{file[:-9]}.eml', follow_symlinks=True)
                        print (f'Die Datei {file[:-9]}.eml wurde erfolgreich kopiert.')
                        rename(join(root, file), f'{join(root, file)}.old')
                        print (f'Die Datei {file} wurde erfolgreich umbenannt.')
                        rename(join(root, f'{file[:-9]}.eml'), f'{join(root, file[:-9])}.eml.old')
                        print (f'Die Datei {file[:-9]}.eml wurde erfolgreich umbenannt.')
                    except SameFileError as e: print (e)
                    except FileExistsError as e: print (e)

                    Kollege = ""
                    sleep(0.5)
            print (f"Der Pfad {root} wurde ueberprueft.")
            sleep(2.5)
    except: print ("Ein Fehler ist aufgetreten"), sleep(5)
