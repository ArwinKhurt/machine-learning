Deterministic Finite Automaton (DFA) in Python

This project implements a simple Deterministic Finite Automaton (DFA) in Python. The DFA is designed to recognize certain strings over the alphabet {a, b} based on defined transition rules.

DFA Description

Start State: q0

Accept State(s): {q3}

Alphabet: {a, b}

Transitions:

Current State	Input a	Input b
q0	q1	q0
q1	q1	q2
q2	q1	q3
q3	q1	q0

A string is accepted if, after consuming all its characters, the DFA ends in the accept state q3.

Code Overview

DFA class

Initializes the DFA with states, transitions, and accept states.

accepts(string): Simulates the DFA on an input string and returns True if accepted, otherwise False.

Main section

Creates a DFA object.

Tests multiple input strings to see if they are accepted.

Example Usage

Run the script:

python dfa.py

Sample Output
abb      → True
aabb     → False
babb     → True
abab     → False
abba     → False
bbababb  → True
ab       → False
bbb      → False

Explanation of Results

abb → Accepted because the DFA ends in q3.

babb → Accepted for the same reason.

bbb → Rejected because it loops in q0 and never reaches q3.

Only strings that guide the DFA into q3 after reading the last symbol are accepted.