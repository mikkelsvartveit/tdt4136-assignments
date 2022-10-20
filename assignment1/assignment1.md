# TDT4136 Assignment 1

## Question 1

Three definitions not from the lecture:

- *Artificial intelligence leverages computers and machines to mimic the problem-solving and decision-making capabilities of the human mind* ([definition from IBM](https://www.ibm.com/cloud/learn/what-is-artificial-intelligence))
- *Artificial intelligence (AI) makes it possible for machines to learn from experience, adjust to new inputs and perform human-like tasks* ([definition from SAS](https://www.sas.com/en_us/insights/analytics/what-is-artificial-intelligence.html))
- *The study and development of computer systems that can copy intelligent human behaviour* (definition from [Oxford Dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/artificial-intelligence))

We can see that these definitions vary in the sense that some focuses more on the self-learning capabilities of an AI, while others emphasize mimicking human behavior, either through performing tasks or making decisions.

## Question 2

The Turing test is a test developed by Alan Turing, where a computer attempts to mimic human communication to the degree where a person (interviewer) can not tell that the communicator is actually a computer. The purpose of the test is detecting whether a computer can be considered intelligent.

## Question 3

Rationality is the ability to make good decisions based on the available data at the time of the decision. A rational decision will not always be the correct decision, but it should be the best “guess” taking into account the information we know prior to the decision.

## Question 4

Thinking rationally and acting rationally is often co-existing, but there is certainly a slight difference at place here. While thinking rationally is often a preface to acting rationally, there are situations where this is not the case. An example is situations which require urgent action, such as avoiding a car accident. If an animal suddenly jumps into the road in front of you, most of us would react with slamming the brakes or steering clear of it. This is done on pure instinct, and while it is certainly a rational decision given the circumstances, it is a situation that doesn’t require much rational thinking.

## Question 5

Aristotle argued that actions are done because of a series of logical implications from knowledge suggests that an action is necessary. The first AI researchers to implement this was Newell and Simon with their General Problem Solver (GPS) program, which used logical planning to achieve definite goals.

## Question 6

1. I would say yes. The elk could have crashed into the robot no matter if the robot had started crossing the road or not. It is hard/impossible to predict the movement of an elk.
2. I find this more debatable, since it probably is a good idea to check for passing cars before crossing a road, even if you have a green light.

## Question 7

1. A simple reflex agent would probably not be rational for this environment, because if both tiles are clean, the agent would have no choice but to move back and forth between the squares to check if the tiles are clean, which means the penalizing points would add up quickly.
2. Yes, a reflex agent with state could be rational in this environment, since it could keep track of the state in the other square without moving there all the time.
3. Yes! A simple reflex agent with perception of both squares can act perfectly, only moving to the other square when it is actually dirty. 

## Question 8

- **Partially observable:** The sensors can only percept the tile the robot is standing on.
- **Single-agent:** There are no other agents to take into account.
- **Nondeterministic:** The agent’s action is not what makes the floor dirty. Whether a tile gets dirty is an external factor, hence not completely determined by the previous state and the actions executed by the agent.
- **Episodic:** Previous states and and actions do not affect the current state. Therefore it is episodic.
- **Static:** The agent only needs to take into account whether a tile is dirty or not *right now*.
- **Discrete:** The agent does not need to consider if the tile changes state from one moment to another, only if the tile is dirty in a specific state.
- **Known:** The agent surely knows that its goal is to clean the floor as much as possible.

## Question 9

- **Simple reflex agents:** Primitive, does not require much memory or computing power. However, often not complex enough to be rational in a lot of environments.
- **Model-based reflex agents:** Has memory of previous states to allow for more knowledge of the environment than just what the sensors are percepting at a certain time.
- **Goal-based agents:** More flexible than the two former agents, but less efficient and requires more computing power. Sometimes hard for humans to define clear goals while considering consequences.
- **Utility-based agents:** Allows for more granular indication of success than the binary goal-based agent. However, implementing it can be a difficult task.