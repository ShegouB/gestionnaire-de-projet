import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Connexion à la base de données SQLite
conn = sqlite3.connect('projects.db')
c = conn.cursor()

# Fonction pour créer les tables
def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 description TEXT,
                 status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 project_id INTEGER,
                 name TEXT,
                 description TEXT,
                 assigned_to TEXT,
                 status TEXT,
                 start_date TEXT,
                 end_date TEXT,
                 FOREIGN KEY (project_id) REFERENCES projects(id))''')

def alter_tables():
    try:
        c.execute('ALTER TABLE tasks ADD COLUMN start_date TEXT')
    except sqlite3.OperationalError:
        pass  # La colonne existe déjà
    try:
        c.execute('ALTER TABLE tasks ADD COLUMN end_date TEXT')
    except sqlite3.OperationalError:
        pass  # La colonne existe déjà

create_tables()
alter_tables()
conn.commit()    
 
def create_project():
    st.header('Créer un nouveau projet')
    name = st.text_input('Nom du projet')
    description = st.text_area('Description')
    status = st.selectbox('Statut', ['Not Started', 'In Progress', 'Completed'])
    
    if st.button('Créer projet'):
        c.execute('INSERT INTO projects (name, description, status) VALUES (?, ?, ?)', (name, description, status))
        conn.commit()
        st.success(f"Le projet '{name}' a été créé avec succès")

def view_projects():
    st.header('Voir les projets')
    projects = pd.read_sql_query('SELECT * FROM projects', conn)
    st.write(projects)

def create_task():
    st.header('Créer une nouvelle tâche')
    projects = pd.read_sql_query('SELECT * FROM projects', conn)
    project_id = st.selectbox('Projet', projects['id'])
    name = st.text_input('Nom de la tâche')
    description = st.text_area('Description')
    assigned_to = st.text_input('Assigné à')
    status = st.selectbox('Statut', ['Not Started', 'In Progress', 'Completed'])
    start_date = st.date_input('Date de début')
    end_date = st.date_input('Date de fin')
    
    if st.button('Créer tâche'):
        c.execute('INSERT INTO tasks (project_id, name, description, assigned_to, status, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?, ?)', (project_id, name, description, assigned_to, status, start_date, end_date))
        conn.commit()
        st.success(f"La tâche '{name}' a été créée avec succès")

def view_tasks():
    st.header('Voir les tâches')
    tasks = pd.read_sql_query('SELECT * FROM tasks', conn)
    st.write(tasks)

def projects_by_status():
    st.header("Projets par statut")
    projects = pd.read_sql_query('SELECT status, COUNT(*) as count FROM projects GROUP BY status', conn)
    fig = px.bar(projects, x='status', y='count', labels={'status': 'Statut', 'count': 'Nombre de Projets'})
    st.plotly_chart(fig)


def tasks_by_project():
    st.header("Tâches par projet")
    tasks = pd.read_sql_query('SELECT projects.name as project, COUNT(tasks.id) as count FROM tasks INNER JOIN projects ON tasks.project_id = projects.id GROUP BY project', conn)
    fig = px.bar(tasks, x='project', y='count', labels={'project': 'Projet', 'count': 'Nombre de Tâches'})
    st.plotly_chart(fig)

def gantt_chart():
    st.header("Diagramme de Gantt des Tâches")
    tasks = pd.read_sql_query('''
        SELECT 
            tasks.name, 
            tasks.start_date, 
            tasks.end_date, 
            tasks.status, 
            projects.name as project
        FROM tasks 
        JOIN projects ON tasks.project_id = projects.id
    ''', conn)
    
    if tasks.empty:
        st.warning("Aucune tâche disponible pour générer le diagramme de Gantt.")
    else:
        fig = px.timeline(tasks, x_start="start_date", x_end="end_date", y="project", color="status", title="Diagramme de Gantt des Tâches")
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig)

def main():
    
    st.sidebar.title(f"Bienvenue")
    option = st.sidebar.selectbox("Choisissez une option", ["Créer un projet", "Voir les projets", "Créer une tâche", "Voir les tâches", "Projets par statut", "Tâches par projet", "Diagramme de Gantt"])
        
    if option == "Créer un projet":
            create_project()
    elif option == "Voir les projets":
            view_projects()
    elif option == "Créer une tâche":
            create_task()
    elif option == "Voir les tâches":
            view_tasks()
    elif option == "Projets par statut":
            projects_by_status()
    elif option == "Tâches par projet":
            tasks_by_project()
    elif option == "Diagramme de Gantt":
            gantt_chart()

if __name__ == '__main__':
    main()


