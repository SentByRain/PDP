import logging

import graypy

from src.config import CONFIG


class Logger:
    def __init__(self):
        self.logs = []
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        handler = graypy.GELFUDPHandler(CONFIG.GRAYLOG_HOST, CONFIG.GRAYLOG_PORT)
        self.logger.addHandler(handler)
        self.extra = {}

    def error(self, record: str, extra: dict = None):
        record = f"ОШИБКА: {record}"
        self.info(record, extra)

    def info(self, record: str, extra: dict = None):
        self.logs.append(record)
        if extra:
            self.extra.update(extra)

    def get_logs(self) -> str:
        return "\n".join(self.logs)

    def dump(self):
        log = self.get_logs()
        self.logs.clear()
        if CONFIG.SEND_LOGS_TO_GRAYLOG:
            _extra = self.extra | {"env": CONFIG.ENV, "service": CONFIG.PROJECT_NAME}
            self.extra = {}
            self.logger.info(log, extra=_extra)
        else:
            print(log)


logger = Logger()
