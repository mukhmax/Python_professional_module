from datetime import datetime
import csv


def logger(log_path):
    def logger_(some_function):
        def new_function(*args, **kwargs):
            log_line = [datetime.now(), some_function]
            log_line.extend(args)
            log_line.extend(kwargs.values())
            with open(f'{log_path}log.txt', 'a') as log:
                writer = csv.writer(log)
                writer.writerow(log_line)
            result = some_function(*args, **kwargs)
            return result
        return new_function
    return logger_
