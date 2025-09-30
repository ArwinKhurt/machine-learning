class DFA:
    def __init__(self):
        self.start_state = "q0"
        self.accept_states = {"q3"}
        self.transitions = {
            "q0": {"a": "q1", "b": "q0"},
            "q1": {"a": "q1", "b": "q2"},
            "q2": {"a": "q1", "b": "q3"},
            "q3": {"a": "q1", "b": "q0"},
        }

    def accepts(self, string):
        state = self.start_state
        for symbol in string:
            if symbol not in self.transitions[state]:
                return False
            state = self.transitions[state][symbol]
        return state in self.accept_states


if __name__ == "__main__":
    dfa = DFA()
    tests = ["abb", "aabb", "babb", "abab", "abba", "bbababb", "ab", "bbb"]
    for t in tests:
        print(f"{t:8} → {dfa.accepts(t)}")