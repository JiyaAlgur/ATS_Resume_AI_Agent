from agents.skill_normalizer import SkillNormalizer


class ATSMatcher:

    def __init__(self):

        self.normalizer = SkillNormalizer()

    def compare(self, resume_data, jd_data):

        resume_items = {}

        # Collect Resume Technologies
        for category in [
            "skills",
            "tools",
            "cloud",
            "databases",
            "frameworks"
        ]:

            for item in resume_data.get(category, []):

                normalized = self.normalizer.normalize(item)

                resume_items[normalized] = item

        jd_items = {}

        # Collect JD Technologies
        for category in [
            "skills",
            "tools",
            "cloud",
            "databases",
            "frameworks"
        ]:

            for item in jd_data.get(category, []):

                normalized = self.normalizer.normalize(item)

                jd_items[normalized] = item

        matched = []
        missing = []

        for normalized_skill, original_skill in jd_items.items():

            if normalized_skill in resume_items:
                matched.append(original_skill)
            else:
                missing.append(original_skill)

        extra = []

        for normalized_skill, original_skill in resume_items.items():

            if normalized_skill not in jd_items:
                extra.append(original_skill)

        if len(jd_items) > 0:
            score = round((len(matched) / len(jd_items)) * 100)
        else:
            score = 0

        return {
            "matched": sorted(matched),
            "missing": sorted(missing),
            "extra": sorted(extra),
            "score": score
        }