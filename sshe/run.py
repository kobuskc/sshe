import sys, os
sys.path.insert(0, os.path.abspath('..'))

from sshe import sshe

if __name__ == '__main__':
    client = sshe.sshe()
    client.run()
