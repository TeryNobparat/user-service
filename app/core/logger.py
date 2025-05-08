import logging
import os
from datetime import datetime

class LevelFilter(logging.Filter):
    """Custom filter to allow only specific log levels."""
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

class AppLogger:
    def __init__(self, name: str = 'app', log_dir: str = 'logs', level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not self.logger.handlers:
            date_str = datetime.now().strftime('%Y%m%d')

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(funcName)s - %(message)s')
            # Console Handler (รวมทุกระดับ)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # แยก log ตามระดับ
            for log_level, folder_name in [
                (logging.INFO, 'info'),
                (logging.WARNING, 'warning'),
                (logging.ERROR, 'error'),
                (logging.CRITICAL, 'critical'),
                (logging.DEBUG, 'debug')
            ]:
                folder_path = os.path.join(log_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                file_path = os.path.join(folder_path, f'{name}_{date_str}.log')

                file_handler = logging.FileHandler(file_path)
                file_handler.setLevel(log_level)
                file_handler.addFilter(LevelFilter(log_level))
                file_handler.setFormatter(formatter)

                self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger