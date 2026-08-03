import re


class SkillNormalizer:

    def __init__(self):

        self.synonyms = {

            # Spark
            "apache spark": "spark",
            "spark sql": "spark",

            # Azure
            "azure data factory (adf)": "azure data factory",
            "azure data lake storage (adls)": "azure data lake storage",
            "adls": "azure data lake storage",
            "adf": "azure data factory",

            # ETL
            "etl/elt development": "etl",
            "etl elt development": "etl",

            # DevOps
            "azure dev ops": "azure devops",

            # ML
            "ml ops": "mlops",

            # SQL
            "structured query language": "sql",

            # Python
            "python3": "python",
            "python 3": "python",

            # Databricks
            "databricks": "azure databricks"
        }

    def normalize(self, skill):

        skill = skill.lower().strip()

        # Remove anything inside brackets
        skill = re.sub(r"\(.*?\)", "", skill)

        # Replace separators with spaces
        skill = re.sub(r"[-_/]", " ", skill)

        # Remove multiple spaces
        skill = " ".join(skill.split())

        # Apply synonym mapping
        if skill in self.synonyms:
            skill = self.synonyms[skill]

        return skill