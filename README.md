# Gestionnaire de Projets

Une plateforme où les équipes peuvent gérer des projets de manière collaborative. Les utilisateurs peuvent créer des projets, assigner des tâches, suivre l'avancement, et discuter des progrès.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## Fonctionnalités

- **Gestion de Projet** : Créez, modifiez et supprimez des projets.
- **Gestion des Tâches** : Assignez des tâches aux membres de l'équipe, définissez des dates de début et de fin, et suivez leur progression.
- **Visualisation des Projets** : Affichez les projets par statut.
- **Visualisation des Tâches** : Affichez les tâches par projet.
- **Diagramme de Gantt** : Visualisez les tâches avec un diagramme de Gantt pour une meilleure gestion du temps.

## Prérequis

- [Python](https://www.python.org/downloads/) (version 3.10 ou plus)
- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/download.html)

## Installation

1. Clonez le dépôt GitHub :
    ```bash
    git clone https://github.com/ShegouB/gestionnaire-de-projets.git
    cd gestionnaire-de-projets
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez l'application Streamlit :
    ```bash
    streamlit run app.py
    ```

2. Ouvrez votre navigateur et allez à l'adresse :
    ```
    http://localhost:8501
    ```

## Contribution

Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer :

1. Fork le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos modifications (`git commit -m 'Add some AmazingFeature'`)
4. Poussez votre branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## Contact

- **Nom** : Boris Shegou
- **GitHub** : (https://github.com/ShegouB)

