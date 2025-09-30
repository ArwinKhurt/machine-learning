Deterministic Finite Automaton (DFA) in Python
1. Introduction

This project presents the implementation of a Deterministic Finite Automaton (DFA) using Python.
The DFA operates over the alphabet {a, b} and determines whether given input strings are accepted based on predefined state transitions.

2. DFA Specifications

Start State: q0

Accept State(s): {q3}

Alphabet: {a, b}

Transition Table:

Current State	Input a	Input b
q0	q1	q0
q1	q1	q2
q2	q1	q3
q3	q1	q0

Acceptance Condition:
A string is accepted if, after processing all input symbols, the DFA terminates in the accept state q3.

3. Code Structure

Class: DFA

Defines states, transitions, and the accepting condition.

accepts(string): Evaluates whether the input string is accepted by the DFA.

Main Execution Block

Creates an instance of the DFA.

Tests multiple input strings and outputs their acceptance results.

4. Usage Instructions

Save the implementation in a file, e.g., dfa.py.

Run the program using:

python dfa.py

5. Sample Output
abb      → True
aabb     → False
babb     → True
abab     → False
abba     → False
bbababb  → True
ab       → False
bbb      → False

6. Explanation of Results

abb → Accepted because it ends in state q3.

babb → Accepted for the same reason.

bbb → Rejected because it remains in q0 and never reaches q3.

Only input strings that lead the DFA to state q3 upon completion are accepted.