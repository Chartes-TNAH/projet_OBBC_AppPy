[![Build Status](https://travis-ci.com/Lucaterre/projet_OBBC_AppPy.svg?token=BV8Aycfaqc32oxNsVzFp&branch=master)](https://travis-ci.com/Lucaterre/projet_OBBC_AppPy)

# OPEN BARZAZ BREIZ COLLECTION


## Présentation



Open Barzaz Breiz Collection est une application web python-Flask de mise à disposition d'une collection de chants populaires bretons issus de l'ouvrage Barzaz Breiz (1846) de Théodore Hersart de La Villemarqué. 

L'application est conçue comme une édition numérique qui propose une navigation intéractive et une récupération au format XML-TEI des chansons du corpus. 

Le but technique de l'application est de proposer l'ajout de textes via le seul dataset XML sans avoir à modifier l'ensemble de la brique fonctionnelle de l'application (transformations XSLT, ORM, ou Python-Flask).

---

## Installation de l'application 


1. Installer OBBC à partir de la branche master du dépôt projet_OBBC_AppPy Github :

`$ git clone https://github.com/Lucaterre/projet_OBBC_AppPy.git `

2. Installer Python via le [site](https://www.python.org/downloads/). Pour rappel : la plupart des systèmes Linux, intègre déjà Python.

3. Créer un environnement virtuel à l'aide de VirtualEnv. Dans votre terminal, taper la commande : `$ pip install virtualenv` pour installer VirtualEnv puis `$ virtualenv -p python3 env` ou sous windows : `$ virtualenv -p` puis `$ env:python3 env`

4. Activer l'environnement virtuel via `$ source env/bin/activate`. Pour quitter l'environnement taper simplement `$ deactivate`.

5. Dans le terminal, se placer au niveau du fichier `requirements.txt`, puis installer les différents packages nécéssaires avec la commande suivante : `$ pip install -r requirements.txt`.

6. Dans le terminal, rentrer la commande `$ cd OBBC/`, Une fois dans le dossier lancer l'application avec la commande `$ python run.py` ou `$ python3 run.py` via le serveur local et selon votre version de python (`$ python --version ou -V`).

---

