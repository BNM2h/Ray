import numpy as np
import matplotlib.pyplot as plt

class Env():
    def __init__(self):
        self.q_star_init=np.random.randn(10)
        
    def step(self,action):
        seed=np.random.normal(0, 0.01, 10)
        q_star=self.q_star_init+seed
        reward=np.random.normal(q_star[action-1], 1, 1)
        optimal_action=np.argmax(q_star)+1
        info=0
        if optimal_action==action:
            info=1
        #print(q_star,self.q_star_init)
        return reward,info

class MAB():
    def __init__(self):
        self.q_table=np.zeros(10)
        self.Num=np.zeros(10)
        self.alpha=0.1
    def update(self,action,reward):
        self.Num[action-1]+=1
        q=self.q_table[action-1]
        q_1=q*(1-self.alpha)+self.alpha*reward
        self.q_table[action-1]=q_1
        print(self.q_table)
    
    def choose_action(self,epsilon):
        seed=np.random.rand(1)
        if seed>epsilon:
            action=np.argmax(self.q_table)+1
        else:
            action=np.random.randint(1,11)
        return action

def main():
    env=Env()
    mab=MAB()
    avg_reward=[]
    optimal_action_percentage=[]
    sr=0
    so=0
    epsilon=0.1
    for s in range(5000):
        a=mab.choose_action(epsilon)
        r,info=env.step(a)
        mab.update(a,r)
        print(a)
        sr+=r
        so+=info
        avg_reward.append(sr/(s+1))
        optimal_action_percentage.append(so/(s+1))

    plt.subplot(221)
    plt.plot(avg_reward)
    plt.subplot(222)
    plt.plot(optimal_action_percentage)
    plt.show()

if __name__ == '__main__':
    main()