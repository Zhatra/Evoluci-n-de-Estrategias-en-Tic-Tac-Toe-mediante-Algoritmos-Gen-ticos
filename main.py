# main.py

import pickle
from genetic_algorithm import GeneticAlgorithm
from strategies import random_strategy, heuristic_strategy, minimax_strategy
import random

def get_move_from_individual(individual):
    def strategy(game, player):
        state_int = GeneticAlgorithm.state_to_int(GeneticAlgorithm, game.get_state())
        move = individual.get(state_int, random.choice(game.available_moves()))
        if move not in game.available_moves():
            move = random.choice(game.available_moves())
        return move
    return strategy

def evaluate_strategies_against_random(strategies, num_games=100):
    from tic_tac_toe import TicTacToe
    results = {}
    for strategy_name, strategy_func in strategies.items():
        wins = 0
        draws = 0
        losses = 0
        for _ in range(num_games):
            game = TicTacToe()
            current_player = 'X'
            while not game.is_full():
                if current_player == 'X':
                    move = strategy_func(game, 'X')
                    game.make_move(move, 'X')
                    if game.check_winner('X'):
                        wins += 1
                        break
                else:
                    move = random_strategy(game, 'O')
                    game.make_move(move, 'O')
                    if game.check_winner('O'):
                        losses +=1
                        break
                if game.is_full():
                    draws +=1
                    break
                current_player = 'O' if current_player == 'X' else 'X'
        results[strategy_name] = {'wins': wins, 'draws': draws, 'losses': losses}
    return results

if __name__ == '__main__':
    ga = GeneticAlgorithm(
        population_size=50,
        generations=50,
        mutation_rate=0.01,
        crossover_rate=0.7
    )
    best_individual, fitness_history = ga.run()
    # Guardar el mejor individuo y la historia de aptitud
    with open('best_individual.pkl', 'wb') as f:
        pickle.dump(best_individual, f)
    with open('fitness_history.pkl', 'wb') as f:
        pickle.dump(fitness_history, f)
    
    # Definir las estrategias para evaluar
    strategies = {
        'AG Evolucionado': get_move_from_individual(best_individual),
        'Estrategia Aleatoria': random_strategy,
        'Estrategia Heurística': heuristic_strategy,
        'Algoritmo Minimax': minimax_strategy
    }
    
    # Evaluar todas las estrategias contra la estrategia aleatoria
    results = evaluate_strategies_against_random(strategies)
    with open('evaluation_results.pkl', 'wb') as f:
        pickle.dump(results, f)
    print('Evaluación completada y resultados guardados.')
