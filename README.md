# Web Scraping Project

Ce projet de web scraping est conçu pour extraire et organiser des données à partir d'un site web donné. Les données extraites sont organisées dans une structure hiérarchique claire basée sur les années et les mois. Chaque dossier contient des fichiers Python (`code.py`) utilisés pour le scraping et les fichiers JSON (`data.json`) contenant les données scrappées.

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [Structure du projet](#structure-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Outils utilisés](#outils-utilisés)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

---

## Aperçu du projet

Le projet utilise des outils de scraping, notamment [Firecrawl](http://www.firecrawl.dev/), pour explorer et collecter des informations depuis un site web. Les données sont ensuite stockées dans des fichiers JSON et organisées en dossiers selon l'année et le mois correspondant à leur extraction.

## Structure du projet

Voici un aperçu de la structure du projet :

```sh
src/
├── 2022
│   ├── Aout
│   │   ├── code.py
│   │   └── data.json
│   ├── Decembre
│   │   ├── code.py
│   │   └── data.json
│   ├── Novembre
│   │   ├── code.py
│   │   └── data.json
│   ├── Octobre
│   │   ├── code.py
│   │   └── data.json
│   └── Septembre
│       ├── code.py
│       └── data.json
├── 2023
│   ├── Aout
│   │   ├── code.py
│   │   └── data.json
│   ├── Avril
│   │   ├── code.py
│   │   └── data.json
│   ├── Decembre
│   │   ├── code.py
│   │   └── data.json
│   ├── Fevrier
│   │   ├── code.py
│   │   └── data.json
│   ├── Janvier
│   │   ├── code.py
│   │   └── data.json
│   ├── Juille
│   │   ├── code.py
│   │   └── data.json
│   ├── Juin
│   │   ├── code.py
│   │   └── data.json
│   ├── Mai
│   │   ├── code.py
│   │   └── data.json
│   ├── Mars
│   │   ├── code.py
│   │   └── data.json
│   ├── Novembre
│   │   ├── code.py
│   │   └── data.json
│   ├── Octobre
│   │   ├── code.py
│   │   └── data.json
│   └── Septembre
│       ├── code.py
│       └── data.json
└── 2024
    ├── Aout
    │   ├── code.py
    │   └── data.json
    ├── Avril
    │   ├── code.py
    │   └── data.json
    ├── Fevrier
    │   ├── code.py
    │   └── data.json
    ├── Janvier
    │   ├── code.py
    │   └── data.json
    ├── Juillet
    │   ├── code.py
    │   └── data.json
    ├── Juin
    │   ├── code.py
    │   └── data.json
    ├── Mai
    │   ├── code.py
    │   └── data.json
    ├── Mars
    │   ├── code.py
    │   └── data.json
    ├── Novembre
    │   ├── code.py
    │   └── data.json
    ├── Octobre
    │   ├── code.py
    │   └── data.json
    └── Septembre
        ├── code.py
        └── data.json

```


### Contenu des fichiers

- **`code.py`** : Contient le script Python utilisé pour scrapper les données pour un mois donné.
- **`data.json`** : Contient les données extraites, structurées en format JSON.

## Prérequis

Assurez-vous d'avoir installé les outils et dépendances suivants :

- Python 3.12 ou supérieur
- Environnement virtuel Python (`venv`)
- Bibliothèques Python : 
  - `requests`
  - `BeautifulSoup4`
  - Toute autre dépendance utilisée pour le projet
- [Firecrawl](http://www.firecrawl.dev/) pour le crawling.

## Installation

1. Clonez le dépôt du projet :
   ```bash
   git clone https://github.com/Roslyns/web-scrapping-project.git
   cd web-scrapping-project/src
