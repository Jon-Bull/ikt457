import random

class TsetlinAutomaton:
    def __init__(self):
        # Automaton starts in a random state
        self.state = random.choice([0, 1])  # 0 represents "No", 1 represents "Yes"
        
    def action(self):
        # The action is "Yes" if in state 1, otherwise "No"
        return "Yes" if self.state == 1 else "No"
    
    def reward(self):
        # If rewarded, the automaton moves towards state 1 ("Yes")
        if self.state == 0:
            self.state = 1
        # If in state 1 and rewarded, it stays in state 1

    def penalty(self):
        # If penalized, the automaton moves towards state 0 ("No")
        if self.state == 1:
            self.state = 0
        # If in state 0 and penalized, it stays in state 0

def main():
    # Step 1: Create 5 Tsetlin Automata
    automata = [TsetlinAutomaton() for _ in range(5)]
    
    # Repeat indefinitely
    while True:
        # Step 2: Count the number of "Yes" actions
        yes_count = sum(1 for automaton in automata if automaton.action() == "Yes")
        
        # Step 3: Determine reward/penalty based on yes_count
        if yes_count in [0, 1, 2, 3]:
            reward_probability = yes_count * 0.2
        else:  # yes_count is 4 or 5
            reward_probability = 0.6 - (yes_count - 3) * 0.2
            
        # Step 4: Apply reward or penalty to each automaton independently
        for automaton in automata:
            if random.random() < reward_probability:
                automaton.reward()
            else:
                automaton.penalty()
        
        # Optionally, print out the states or actions to observe the process
        actions = [automaton.action() for automaton in automata]
        print(f"Automata actions: {actions} | Yes count: {yes_count} | Reward probability: {reward_probability}")

        # Exit condition or limit loop iterations for testing (e.g., 100 iterations)
        # In this example, let's stop after 100 iterations for testing purposes
        if sum(1 for automaton in automata if automaton.action() == "Yes") >= 100:
            break

if __name__ == "__main__":
    main()
