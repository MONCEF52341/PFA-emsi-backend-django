import os
from graphviz import Digraph

def generate_directory_tree(directory, graph, parent_node=None, exclude=[]):
    if parent_node is None:
        parent_node = directory
    items = os.listdir(directory)
    for item in items:
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            if os.path.basename(full_path) not in exclude:
                graph.node(full_path, label=os.path.basename(item), shape='folder')
                generate_directory_tree(full_path, graph, parent_node=full_path, exclude=exclude)
                graph.edge(parent_node, full_path)
        else:
            if os.path.basename(full_path) not in exclude:
                graph.node(full_path, label=os.path.basename(item), shape='file')
                graph.edge(parent_node, full_path)

def create_directory_tree_graph(directory, exclude=[]):
    graph = Digraph(format='png')
    generate_directory_tree(directory, graph, exclude=exclude)
    return graph

directory_path = 'AbsenceManager'
output_file = 'architecture.png'

# Liste des fichiers et dossiers à exclure
files_to_exclude = ['Coordonées.txt', 'test.py','tree.py','__pycache__','my_models.png','ShemaFromDB.jar','migrations','templates']

graph = create_directory_tree_graph(directory_path, exclude=files_to_exclude)
graph.render(output_file, cleanup=True)