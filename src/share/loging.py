import datetime

__log_path = "log.txt"


def log_info(message: str):
    complete_message = str(datetime.datetime.now()) + ": " + str(message)
    print(complete_message)
    __write_to_log_file(complete_message)


def log_error(message: str):
    complete_message = "ERROR: " + str(datetime.datetime.now()) + ": " + str(message)
    print(complete_message)
    __write_to_log_file(complete_message)


def set_log_path(path: str):
    __log_path = path


def __write_to_log_file(message: str):
    try:
        log_file = open(__log_path, "a")
        log_file.write(message + "\n")
        log_file.close()
    except FileNotFoundError:
        print("FATAL LOGGING ERROR: Writing fo file " + str(__log_path) + " was not possible")
