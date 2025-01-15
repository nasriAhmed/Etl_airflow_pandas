# ETL Pipeline avec Airflow et Pandas

## Description du Projet

Ce projet implémente un pipeline ETL (Extract, Transform, Load) orchestré par **Apache Airflow** et utilise **Pandas** pour effectuer les transformations de données. Les performances et l'exécution du pipeline sont supervisées grâce à **Prometheus** et **Grafana**. Des tests unitaires assurent la fiabilité des différentes étapes.

---

## Fonctionnalités Clés

1. **Orchestration avec Airflow** :  
   - Planification et gestion des étapes ETL dans un DAG.  
   - Suivi des exécutions via l'interface Web d'Airflow.  

2. **Transformation des Données avec Pandas** :  
   - Nettoyage et enrichissement des données.  
   - Flexibilité pour des cas d'usage spécifiques.  

3. **Monitoring avec Prometheus et Grafana** :  
   - Collecte des métriques sur les performances du pipeline.  
   - Visualisation des métriques en temps réel.  

4. **Logs** :  
   - Enregistrement des étapes du pipeline dans un fichier log.  
   - Logs détaillés pour le debugging.  

5. **Tests avec Pytest** :  
   - Tests unitaires pour chaque étape ETL.  
   - Détection rapide des erreurs.  

---

## Arborescence du Projet

```plaintext
etl_airflow_pandas/
├── dags/
│   ├── etl_pipeline.py              # Fichier contenant le DAG Airflow
│   ├── __init__.py
├── scripts/
│   ├── etl.py                       # Scripts pour les étapes ETL
│   ├── logger_config.py             # Configuration du logger
│   ├── __init__.py
├── data/
│   ├── raw_data.csv                 # Données brutes
│   ├── temp/                        # Données temporaires
│       ├── extracted_data.csv       # Données extraites
│       ├── transformed_data.csv     # Données transformées
├── logs/
│   ├── etl_pipeline.log             # Logs générés par le pipeline
├── tests/
│   ├── test_etl.py                  # Tests unitaires pour les étapes ETL
│   ├── __init__.py
├── docker/
│   ├── docker-compose.yml           # Configuration Docker Compose
│   ├── prometheus.yml               # Configuration Prometheus
├── .env                             # Variables d'environnement
├── .gitignore                       # Fichiers à ignorer par Git
├── requirements.txt                 # Dépendances Python
├── README.md                        # Documentation du projet
```

---

## Prérequis

- **Python 3.9+**  
- **Docker et Docker Compose**  
- **Apache Airflow 2.6.1**  
- **Prometheus et Grafana**

---

## Installation

Installez les dépendances Python avec :  
```bash
pip install -r requirements.txt
```

---

## Étapes du Pipeline ETL

### **Extract** :  
- Chargement des données brutes depuis un fichier CSV.  
- **Fichier de sortie** : `data/temp/extracted_data.csv`.  

### **Transform** :  
- Nettoyage et enrichissement des données.  
- **Fichier de sortie** : `data/temp/transformed_data.csv`.  

### **Load** :  
- Chargement des données transformées dans une base de données ou un fichier final.  

---

## Configuration et Exécution

### **Configuration des Services** :  
1. Placez le fichier `docker/docker-compose.yml` à la racine du projet.  
2. Configurez les variables d'environnement dans `.env`.  

### **Lancer les Services** :  
```bash
docker-compose up -d
```

### **Accéder aux Interfaces** :  
- **Airflow** : [http://localhost:8080](http://localhost:8080)  
- **Prometheus** : [http://localhost:9090](http://localhost:9090)  
- **Grafana** : [http://localhost:3000](http://localhost:3000)  

### **Exécuter le Pipeline** :  
1. Accédez à l'interface Airflow.  
2. Activez le DAG `etl_pipeline`.  

---

## Tests

Lancez les tests unitaires avec :  
```bash
pytest tests/
```

---

## Monitoring

1. **Prometheus** collecte les métriques d'exécution.  
2. **Grafana** affiche les métriques sur des tableaux de bord.  

### Exemple de Métriques :  
- Temps d'exécution des étapes ETL.  
- Nombre d'exécutions réussies et échouées.  


## Auteur

Ahmed Nasri  
