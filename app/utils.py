import configparser

def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config['Database']['DB_PATH']