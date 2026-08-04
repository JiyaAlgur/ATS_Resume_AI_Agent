import logging
import os


class ProjectLogger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/project.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("ATS_Project")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)