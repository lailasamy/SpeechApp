class SessionSummary:
    def __init__(self):
        self.entries = []

    def add_entry(self, transcript, disorder_status, material, facial_expressions):
        self.entries.append({
            'transcript': transcript,
            'disorder_status': disorder_status,
            'material': material,
            'facial_expressions': facial_expressions
        })

    def is_session_complete(self):
        return len(self.entries) >= 10  # Example condition for session completion

    def generate_summary(self):
        # Generate a session summary
        summary = {
            'total_entries': len(self.entries),
            'correct': sum(1 for entry in self.entries if entry['disorder_status'] == "Dialect"),
            'incorrect': sum(1 for entry in self.entries if entry['disorder_status'] == "Disordered 
Speech"),
            'repeat_words': [entry['material'] for entry in self.entries if 
entry['disorder_status'] == "Disordered Speech"]
        }
        print(f"Session Summary: {summary}")
        return summary

