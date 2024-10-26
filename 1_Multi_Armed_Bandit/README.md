# CA 1, Interactive Learning, Fall 2024
- **Name**: Majid Faridfar
- **Student ID**: 810199569
## Problem 1 (Food Recommendation System)
### Investigating the Effect of Changing Parameters

I explored two things in this section: 1) Effect of **different epsilons** on an RL agent following epsilon greedy policy, 2) Effect of **different c's** on an RL agent following UCB policy.

#### Value-Based Epsilon Greedy with Different Epsilons

![Epsilon Greedy Cumulative Plot](plots/epsilon-greedy-cumulative.png)

![Epsilon Greedy Average Plot](plots/epsilon-greedy-average.png)

Note that for all four agents, $\epsilon$ decreases over time, with the following formula:

$$\epsilon = max(0.05, \epsilon*0.998)$$

It is grantueed that $\epsilon$ never becomes $0$ (its minimum value is set to $0.05$), to always maintain a little possibility of exploring new actions. It is also imporatant that without decreasing the value of $\epsilon$, algorithms never converges! So, we need to do this actually.

My interpretations of the above plots are as follows:

1. Since the agent with $\epsilon = 0.8$  explores the environment more than others at early steps, it follows a somewhat random behaviour for a longer time. So, the amount of cumulative reward it receives remains less than others. Also, the figure for cumulative regret is not only more than other agents with fewer epsilons, but it also starts leveling out later compared to other agents with fewer epsilons.
2. The agents with $\epsilon = 0.1$ and $0.3$ rely on their experience more than two other agents. As a result, they converge faster, meaning that they find the optimal action quickly and consequently start doing it earlier resulting in better results. To clarify, not only is their cumulative regret less, but the cumulative reward they receive is more than agents with $\epsilon = 0.5$ and $0.8$, over time.

#### UCB with different c's

![UCB cumulative plots](plots/ucb-cumulative.png)

![UCB average plots](plots/ucb-average.png)

### Comparison of the Algorithms

In this step, I chose the best agent for epsilon greedy which has $\epsilon = 0.3$. For thompson sampling and UCB, I used casual agents.

![All Cumulative Plots](plots/all-cumulative.png)

![All Average Plots](plots/all-average.png)

Comparisons:
- **Cumulative Reward**: By looking at the top-left digram, we can see that the agents are ranked as follows (based on the amount of cumulative reward they receive over time):
    1. Thompson Sampling
    2. UCB
    3. Epsilon greedy

    Also, by looking at the bottom-left plot showing the average reward, we can see that the figure for thompson sampling policy is more than others for almost every trail. Additionally, while in the early steps (trails 1 to 500) the average reward agent with an epsilon greedy policy receives is more than that of the agent following a UCB policy, from the 500th trial afterwards, the average reward of UCB agent is more that that of epsilon greedy agent.

- **Convergence Speed**: The agent doing tompson sampling finds the optimal action faster, as its average reward is more than others, and its average regret is less, even at the early steps. This can also be seen in the top-right plot showing the cumulative regret. It is clear that the figure for thompson sampling is less than other plots, meaning that it converges faster than other agents. Moreover, 

## Problem 2 (Advertising in an Online Store)
### Formulation of the Problem
Suppose we have an agent with 4 possible actions (`a`):

1. First, show advert 1, then, advert 2.
2. First, show advert 2, then, advert 1.
3. Show advert 1 twice.
4. Show advert 2 twice.
   
And, after doing each of above actions, the agent receives a reward (e.g. users click on the advertisement or they buy the advertised product).

Now, we have a formal n-arm bandit problem.
### Exploration-Exploitation Strategy

Considering the previous question, I want to manage the balance between exploration and exploitation with rhompson sampling.

## Problem 3 (Social Mobile)
### Formulation of the Problem
Suppose we have `m` agents (index of our agent is $0$), with each having `n` possible actions. ALso, the probability of receiving rewards for the `i`th agent is $p_i$ ($0 \le i < m$). 

Since our agent can observe the actions choices of other agents, it can use them to tackle the problem of sparse rewards, by combining individual learning with social learning. To achieve this, I investigate two methods which are explained in the following:

#### Two Q Values:
Here, we have two distinct sets of `Q values`: one is based on agent's own experiences (`q_values_own`), and the other one is based on observations of other agents (`q_values_social`). The former is updated with the direct rewards agent receives from user, while for updating the latter, we should define another reward function:

#### Combined Rewards:


### Exploration-Exploitation Strategy