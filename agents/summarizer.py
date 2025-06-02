class Summarizer:
    def summarize(self, verified_data: list) -> str:
        summary = ""
        for item in verified_data:
            summary += (
                f"\n- {item['task']}: {item['wikipedia']} | {item['news']}\n"
                f"  Notes: {item['verification_notes']}\n"
            )
        return summary.strip()
