from .tabular_policy import TabularPolicy
from .tabular_value_function import TabularValueFunction
from .qtable import QTable


class PolicyIteration:
    def __init__(self, mdp, policy):
        self.mdp = mdp
        self.policy = policy

    def policy_evaluation(self, policy, values, theta=0.001):
        """
        TODO: Complete the policy evaluation function that calculates state values V(s) 
        for the current policy until convergence.
        """
        while True:
            # TODO: Initialize delta to track the maximum change in value function
            delta = 0
            new_values = TabularValueFunction()
            for state in self.mdp.get_states():
                # TODO: Get available actions for current state
                actions = self.mdp.get_actions(state)

                # TODO: Get the old value for the current state
                old_value = values.get_value(state)

                # TODO: Calculate new value using the current policy
                new_value = values.get_q_value(self.mdp, state, policy.select_action(state, actions))
                values.add(state, new_value)

                # TODO: Update delta with maximum change in value
                delta = max(delta, abs(old_value - new_value))

            # TODO: Check for convergence
            if delta < theta:
                break

        return values

    """ Implmentation of policy iteration iteration. Returns the number of iterations executed """

    def policy_iteration(self, max_iterations=100, theta=0.001):

        """
        TODO: Complete the policy iteration algorithm that iteratively improves the policy
        until convergence or max_iterations is reached.
        """

        values = TabularValueFunction()

        for i in range(1, max_iterations + 1):
            # TODO: Initialize policy_changed flag to track if policy was updated
            policy_changed = False

            # TODO: Call policy_evaluation to get updated values
            values = self.policy_evaluation(self.policy, values, theta)

            for state in self.mdp.get_states():
                # TODO: Get available actions for current state
                actions = self.mdp.get_actions(state)

                # TODO: Get current action for this state from policy
                old_action = self.policy.select_action(state, actions)

                # TODO: Create Q-table and calculate Q-values for all actions
                q_table = QTable(alpha=1.0)

                # TODO: Get best action based on Q-values
                for action in self.mdp.get_actions(state):
                    new_value = values.get_q_value(self.mdp, state, action)
                    q_table.update(state, action, new_value)

                best_action = q_table.get_argmax_q(state, self.mdp.get_actions(state))

                # TODO: Update policy with best action
                self.policy.update(state, best_action)

                # TODO: Check if policy changed
                if best_action is not old_action:
                    policy_changed = True

            # TODO: If policy hasn't changed, we've converged - return number of iterations
            if not policy_changed:
                return i
        return max_iterations
