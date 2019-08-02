from databroker import Broker
from eiger_io.fs_handler_dask import EigerHandlerDask
import chxtools
import eiger_io
import numpy as np
import pyCHX


db = Broker.named('isr')
db.reg.register_handler('AD_EIGER2', EigerHandlerDask, overwrite=True)

