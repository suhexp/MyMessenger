
import logging
import sys
from logging import handlers

format = logging.Formatter('%(asctime)s    %(levelname)s   %(message)s')


crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)



applog_hand = handlers.TimedRotatingFileHandler('app.log','D',1,)

applog_hand.setFormatter(format)

app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

logging.getLogger('app.net').setLevel(logging.ERROR)
