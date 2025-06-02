class SourceVerifier:
    def verify(self, collected_data: list) -> list:
        verified = []
        for item in collected_data:
            score = 1.0 if item['wikipedia'] and item['news'] else 0.5
            notes = "Verified from multiple sources." if score == 1.0 else "Partial or weak verification."
            item.update({
                "credibility_score": score,
                "verification_notes": notes
            })
            verified.append(item)
        return verified
