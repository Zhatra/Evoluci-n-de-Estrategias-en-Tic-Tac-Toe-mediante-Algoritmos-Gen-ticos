# main.py

import pickle
from genetic_algorithm import GeneticAlgorithm
from strategies import random_strategy, heuristic_strategy, minimax_strategy
import random

def evaluate_against_strategies(individual, num_games=100):
    from tic_tac_toe import TicTacToe
    results = {
        'Random': {'wins': 0, 'draws': 0, 'losses': 0},
        'Heuristic': {'wins': 0, 'draws': 0, 'losses': 0},
        'Minimax': {'wins': 0, 'draws': 0, 'losses': 0}
    }
    strategies = {
        'Random': random_strategy,
        'Heuristic': heuristic_strategy,
        'Minimax': minimax_strategy
    }
    for strategy_name, strategy_func in strategies.items():
        for _ in range(num_games):
            game = TicTacToe()
            current_player = 'X'
            while not game.is_full():
                if current_player == 'X':
                    state_int = GeneticAlgorithm.state_to_int(GeneticAlgorithm, game.get_state())
                    move = individual.get(state_int, random.choice(game.available_moves()))
                    if move not in game.available_moves():
                        move = random.choice(game.available_moves())
                    game.make_move(move, 'X')
                    if game.check_winner('X'):
                        results[strategy_name]['wins'] +=1
                        break
                else:
                    move = strategy_func(game, 'O')
                    game.make_move(move, 'O')
                    if game.check_winner('O'):
                        results[strategy_name]['losses'] +=1
                        break
                if game.is_full():
                    results[strategy_name]['draws'] +=1
                    break
                current_player = 'O' if current_player == 'X' else 'X'
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
    # Evaluar contra otras estrategias
    results = evaluate_against_strategies(best_individual)
    with open('evaluation_results.pkl', 'wb') as f:
        pickle.dump(results, f)
    print('Evaluación completada y resultados guardados.')
