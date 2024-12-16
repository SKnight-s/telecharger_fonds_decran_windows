#Ce programme permet de télécharger les derniers fonds d'écran windows

import os
import shutil
import imageio.v2 as imageio


dossier1 = os.path.expanduser("~/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets")
dossier2 = os.path.expanduser("~/Pictures/A_afficher")
dossier3 = os.path.expanduser("~/Pictures/Fonds_decran")

if not os.path.exists(dossier2) :
    os.mkdir(dossier2)

if not os.path.exists(dossier3) :
    os.mkdir(dossier3)

files = os.listdir(dossier2)
os.chdir(dossier2)
for file in files :   # Déplace les images déjà dans le dossier
    shutil.copy(file,dossier3) # Copie  
    os.remove(os.path.join(dossier2,file)) # Enlève


l=os.listdir(dossier1)

for i in range (len(l)):
    a=l[i]
    os.chdir(dossier1)
    if os.path.getsize(l[i])>150000 :  # Si la taille de l'image est suffisante
        b=l[i] + ".jpg"
        shutil.copy(l[i],dossier2)
        os.chdir(dossier2)
        os.rename(a,b)
        img=imageio.imread(b)
        if img.shape[0] != 1080 :  # Si le format est le bon
            os.remove(b)
print("Termine")


    
