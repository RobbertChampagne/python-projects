# python projects/project-template/src/script2.py

import sys
import os
import logging

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loggingSetup import setup_logging
from src import script1 as function

def main():
    # Initialize logging
    setup_logging()
    sum = function.add(1, 2)
    print(sum)
    logging.info(f"In script2.py, the sum of 1 and 2 is {sum}")
    

if __name__ == '__main__':
    main()