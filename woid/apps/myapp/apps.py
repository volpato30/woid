from django.apps import AppConfig
from scripts.top import main, prepare_service
import logging
import threading
#some thing wrong with this class
# TODO: fix the startup code, make this class run
class MyAppConfig(AppConfig):
    name = 'myapp'
    verbose_name = 'My Application'
    def ready(self):
        print('startup')
        # define a new Handler to log to console as well
        console = logging.StreamHandler()
        # optional, set the logging level
        console.setLevel(logging.INFO)
        # set a format which is the same for console use
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)
        logging.info('startup')
        # prepare_service()
        # t = threading.Thread(target=main)
        # t.setDaemon(True)
        # t.start()
        return
