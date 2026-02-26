import logging
import traceback
from datetime import datetime
import json
import os

def write_json_log(record, file_path):

    try:
        exception = None
        if record.exc_info:
            exception = ''.join(traceback.format_exception(*record.exc_info))

        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'exception': exception
        }
        with open(file_path, 'a', encoding='utf-8') as f:
           f.write(json.dumps(log_entry) + '\n')
    except Exception as e:
        print(f'Failed to write log entry: {e}')

def custom_handler(record, file_path):
    write_json_log(record, file_path)

def setup_logger():
    logger = logging.getLogger('AppLogger')
    logger.setLevel(logging.ERROR)

    file_path = 'logs/errors.json'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


#### CONFIGURAÇÃO DO HANDLER PERSONALIZADO ####
    handler = logging.StreamHandler()
    handler.emit = lambda record: custom_handler(record, file_path)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
