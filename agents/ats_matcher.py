class ATSMatcher:

    def compare(self, resume_data, jd_data):

        # Resume Technologies
        resume_items = set()

        for category in [
            "skills",
            "tools",
            "cloud",
            "databases",
            "frameworks"
        ]:

            for item in resume_data.get(category, []):
                resume_items.add(item.lower().strip())

        # JD Technologies
        jd_items = set()

        for category in [
            "skills",
            "tools",
            "cloud",
            "databases",
            "frameworks"
        ]:

            for item in jd_data.get(category, []):
                jd_items.add(item.lower().strip())

        matched = sorted(resume_items & jd_items)

        missing = sorted(jd_items - resume_items)

        extra = sorted(resume_items - jd_items)

        score = 0

        if len(jd_items) > 0:
            score = round((len(matched) / len(jd_items)) * 100)

        return {
            "matched": matched,
            "missing": missing,
            "extra": extra,
            "score": score
        }