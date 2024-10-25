# CA 1, Interactive Learning, Fall 2024
- **Name**: Majid Faridfar
- **Student ID**: 810199569
## Problem 1 (Food Recommendation System)
### Comparison of the Algorithms
### Investigating the Effect of Changing Parameters

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

## Problem 3 (Social Mobile)
### Formulation of the Problem
Suppose we have `m` agents (index of our agent is $0$), with each having `n` possible actions. ALso, the probability of receiving rewards for the `i`th agent is $p_i$ ($0 \le i < m$). 

Since our agent can observe the actions choices of other agents, it can use them to tackle the problem of sparse rewards, by combining individual learning with social learning. To achieve this, I investigate two methods which are explained in the following:

#### Two Q Values:
Here, we have two distinct sets of `Q values`: one is based on agent's own experiences (`q_values_own`), and the other one is based on observations of other agents (`q_values_social`). The former is updated with the direct rewards agent receives from user, while for updating the latter, we should define another reward function:

#### Combined Rewards:


### Exploration-Exploitation Strategy