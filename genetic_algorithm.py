# genetic_algorithm.py

import random
import numpy as np
from tic_tac_toe import TicTacToe
from strategies import random_strategy, heuristic_strategy, minimax_strategy

class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.num_states = 3**9  # Número total de estados posibles del tablero
        self.population = [self.generate_individual() for _ in range(self.population_size)]
        self.fitness_history = []

    def generate_individual(self):
        # Cada individuo es un diccionario que mapea estados a movimientos
        individual = {}
        for state in range(self.num_states):
            individual[state] = random.randint(0, 8)
        return individual

    def state_to_int(self, state_str):
        mapping = {' ': '0', 'X': '1', 'O': '2'}
        state_int = int(''.join(mapping[ch] for ch in state_str), 3)
        return state_int

    def play_game(self, individual, opponent_strategy):
        game = TicTacToe()
        current_player = 'X'
        while not game.is_full():
            if current_player == 'X':
                state_int = self.state_to_int(game.get_state())
                move = individual.get(state_int, random.choice(game.available_moves()))
                if move not in game.available_moves():
                    move = random.choice(game.available_moves())
                game.make_move(move, 'X')
                if game.check_winner('X'):
                    return 1  # Victoria
            else:
                move = opponent_strategy(game, 'O')
                game.make_move(move, 'O')
                if game.check_winner('O'):
                    return -1  # Derrota
            current_player = 'O' if current_player == 'X' else 'X'
        return 0  # Empate

    def evaluate_fitness(self, individual):
        wins = 0
        draws = 0
        losses = 0
        opponents = [random_strategy, heuristic_strategy]
        for opponent in opponents:
            for _ in range(10):  # Jugar 10 partidas contra cada oponente
                result = self.play_game(individual, opponent)
                if result == 1:
                    wins += 1
                elif result == 0:
                    draws += 1
                else:
                    losses += 1
        fitness = wins + 0.5 * draws - losses
        return fitness

    def selection(self, fitnesses):
        # Encontrar la aptitud mínima
        min_fitness = min(fitnesses)
        # Ajustar las aptitudes si hay valores negativos
        if min_fitness < 0:
            adjusted_fitnesses = [f - min_fitness + 1 for f in fitnesses]  # +1 para evitar ceros
        else:
            adjusted_fitnesses = fitnesses[:]
        total_fitness = sum(adjusted_fitnesses)
        # Evitar división por cero
        if total_fitness == 0:
            probabilities = [1 / len(adjusted_fitnesses)] * len(adjusted_fitnesses)
        else:
            probabilities = [f / total_fitness for f in adjusted_fitnesses]
        selected_indices = np.random.choice(range(self.population_size), size=self.population_size, p=probabilities)
        selected = [self.population[i] for i in selected_indices]
        return selected

    def crossover(self, parent1, parent2):
        child1 = {}
        child2 = {}
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.num_states - 1)
            keys = list(parent1.keys())
            for i, key in enumerate(keys):
                if i < crossover_point:
                    child1[key] = parent1[key]
                    child2[key] = parent2[key]
                else:
                    child1[key] = parent2[key]
                    child2[key] = parent1[key]
        else:
            child1 = parent1.copy()
            child2 = parent2.copy()
        return child1, child2

    def mutate(self, individual):
        for key in individual.keys():
            if random.random() < self.mutation_rate:
                individual[key] = random.randint(0, 8)

    def run(self):
        for generation in range(self.generations):
            fitnesses = [self.evaluate_fitness(individual) for individual in self.population]
            self.fitness_history.append({
                'max': max(fitnesses),
                'average': sum(fitnesses) / len(fitnesses)
            })
            print(f'Generación {generation +1} - Máx: {max(fitnesses)}, Promedio: {sum(fitnesses)/len(fitnesses)}')
            selected_population = self.selection(fitnesses)
            next_generation = []
            for i in range(0, self.population_size, 2):
                parent1 = selected_population[i]
                if i+1 < self.population_size:
                    parent2 = selected_population[i+1]
                else:
                    parent2 = selected_population[0]
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                next_generation.extend([child1, child2])
            self.population = next_generation[:self.population_size]
        # Guardar el mejor individuo
        fitnesses = [self.evaluate_fitness(individual) for individual in self.population]
        best_individual = self.population[np.argmax(fitnesses)]
        return best_individual, self.fitness_history
