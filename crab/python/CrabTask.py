'''
CrabTask class. 
'''

# ATM
from ATM.core.standard import *

# Logging
import logging
logger = logging.getLogger( __name__ )

class CrabTask( TaskBase ):

    def __init__( self, name, dataset, requires = None):
        #super(CrabTask, self).__init__( name, requires) #That creates an infinite recursion because the retry decorator makes a new class
        TaskBase.__init__( self, name, requires)
        self.dataset = dataset

    def _evaluate( self ):
        logger.info( " CrabTask %r dataset %r", self.name, self.dataset )
        #result = self._function( self )
        result = 0
        return result

if __name__ == "__main__":

    from ATM.core.logger import get_logger
    logger = get_logger('DEBUG')
   
    dataset = '/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD' 

    task = CrabTask('DoubleMu-03Feb2017', dataset )

    logger.info( "Task %r has result %r", task.name, task.result() )
