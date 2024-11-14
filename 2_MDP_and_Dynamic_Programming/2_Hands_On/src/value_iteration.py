from .tabular_value_function import TabularValueFunction
from .qtable import QTable


class ValueIteration:
    def __init__(self, mdp, values):
        self.mdp = mdp
        self.values = values

    def value_iteration(self, max_iterations=100, theta=0.001):
        """
        TODO: Complete the value iteration algorithm that finds the optimal value function
        by iteratively computing state values until convergence.
        """
        for i in range(max_iterations):
            # TODO: Initialize delta to track the maximum change in value function
            delta = 0

            new_values = TabularValueFunction()
            for state in self.mdp.get_states():
                # Initialize a Q_table
                qtable = QTable(alpha=1.0)

                for action in self.mdp.get_actions(state):
                    # TODO: Calculate Q(s,a) using Bellman equation
                    new_value = 0.0

                    # TODO: For each possible next state and its probability
                    for (new_state, probability) in self.mdp.get_transitions(state, action):
                    #     1. Get reward for this transition
                        reward = self.mdp.get_reward(state, action, new_state)
                    #     2. Calculate value using Bellman equation:
                        new_value += probability * (reward + (self.mdp.get_discount_factor() * self.values.get_value(new_state)))             

                    qtable.update(state, action, new_value)

                # TODO: Update value function with maximum Q-value
                # 1. Get maximum Q-value for current state
                max_q = qtable.get_max_q(state, self.mdp.get_actions(state))
                
                # 2. Update delta with maximum change in value
                delta = max(delta, abs(self.values.get_value(state) - max_q))

                new_values.add(state, max_q)

            self.values.merge(new_values)

            # TODO: Check for convergence
            # If change in value function is less than theta, return iteration count
            if delta < theta:
                return i
