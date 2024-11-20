# plot_results.py

import pickle
import matplotlib.pyplot as plt
import numpy as np

# Cargar la historia de aptitud
with open('fitness_history.pkl', 'rb') as f:
    fitness_history = pickle.load(f)

generations = np.arange(1, len(fitness_history) + 1)
max_fitness = [data['max'] for data in fitness_history]
average_fitness = [data['average'] for data in fitness_history]

# Gráfica de evolución de la aptitud
plt.figure(figsize=(10,6))
plt.plot(generations, max_fitness, label='Aptitud Máxima', color='blue', linewidth=2)
plt.plot(generations, average_fitness, label='Aptitud Promedio', color='orange', linewidth=2)
plt.title('Evolución de la Aptitud a lo largo de las Generaciones')
plt.xlabel('Generaciones')
plt.ylabel('Aptitud')
plt.legend()
plt.grid(True)
plt.savefig('grafica_aptitud.png')
# plt.show()  # Comentado para no abrir la ventana de la gráfica

# Cargar los resultados de evaluación
with open('evaluation_results.pkl', 'rb') as f:
    results = pickle.load(f)

estrategias = list(results.keys())
victorias = []
empates = []
derrotas = []

for strategy in estrategias:
    total_games = results[strategy]['wins'] + results[strategy]['draws'] + results[strategy]['losses']
    victorias.append((results[strategy]['wins'] / total_games) * 100)
    empates.append((results[strategy]['draws'] / total_games) * 100)
    derrotas.append((results[strategy]['losses'] / total_games) * 100)

# Gráfica comparativa
ind = np.arange(len(estrategias))
width = 0.25

plt.figure(figsize=(10,6))
plt.bar(ind - width, victorias, width, label='Victorias', color='green')
plt.bar(ind, empates, width, label='Empates', color='yellow')
plt.bar(ind + width, derrotas, width, label='Derrotas', color='red')

plt.ylabel('Porcentaje (%)')
plt.title('Tasas de Victoria por Estrategia contra Estrategia Aleatoria')
plt.xticks(ind, estrategias)
plt.legend()
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafica_comparativa.png')
# plt.show()  # Comentado para no abrir la ventana de la gráfica
