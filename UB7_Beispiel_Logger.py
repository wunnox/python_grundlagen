####################################################
#
# Schreiben von Logmeldungen mit dem Logger_Modul
#
####################################################

# Module
import logging
import time

# Logger Konfiguration
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='Beispiel.log'
    )
logger = logging.getLogger('bespiel_logger')

# Logger Ausgabe
for i in range(10):
    print(f"Druchgang {i}")
    logger.info(f"Logmeldung {i}")
    time.sleep(1)
