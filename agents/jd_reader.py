from agents.exceptions import FileReadError


class JDReader:

    def __init__(self, jd_path):
        self.jd_path = jd_path

    def read_jd(self):

        try:

            with open(self.jd_path, "r", encoding="utf-8") as file:
                return file.read()

        except Exception as e:
            raise FileReadError(
                f"Unable to read Job Description: {e}"
            )