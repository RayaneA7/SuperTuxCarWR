import gymnasium as gym
from bbrl.agents import Agent
    
class MyWrapper(gym.wrappers.ActionWrapper):
    ...

class Actor(Agent):
    """Stochastic policy actor"""
    ...
    
class ArgmaxActor(Agent):
    """Actor that computes the action"""
    ...