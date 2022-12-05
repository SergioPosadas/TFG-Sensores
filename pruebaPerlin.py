#!/usr/bin/python3

from datetime import datetime

import time, datetime, logging

import numpy as np

if __name__ == '__main__':

        logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        
        logging.info('Hello!')

        m = 20
        n = 20
        
        pl = np.random.random((m,n))
        
        logging.info(pl)
        # print(pl)
        
