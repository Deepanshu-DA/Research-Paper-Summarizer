class TaskPlanner:
    def plan(self, query: str) -> list:
        return [
            f"Research key concepts of: {query}",
            f"Gather latest news related to: {query}",
            f"Look for scholarly resources about: {query}",
            f"Verify information consistency for: {query}",
            f"Summarize key findings on: {query}"
        ]
