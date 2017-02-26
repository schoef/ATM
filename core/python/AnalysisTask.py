'''
AnalysisTask class. Task wrapper for function.
'''

# ATM
from ATM.core.standard import *

# Logging
import logging
logger = logging.getLogger( __name__ )

class AnalysisTask( TaskBase ):

    def __init__( self, name, function, requires = None):
        #super(AnalysisTask, self).__init__( name, requires) #That creates an infinite recursion because the retry decorator makes a new class
        TaskBase.__init__( self, name, requires)
        self._function = function

    def _evaluate( self ):
        logger.info( "Evaluating AnalysisTask %r", self.name )
        result = self._function( self )
        logger.debug( "Result for task %r is %r", self.name, result )
        return result

if __name__ == "__main__":

    from ATM.core.logger import get_logger
    logger = get_logger('DEBUG')

    # 1st simple task
    def simpleCalculation1( base ):
        import random

        result = random.random()

        #if result<0.9: raise RuntimeError
        return result

    simple1 = AnalysisTask( "simple1", function = simpleCalculation1 )

    # 2nd simple task
    def simpleCalculation2( base ):
        return 27

    simple2 = AnalysisTask( "simple2", function = simpleCalculation2 )

    # now add the two
    def complicatedCalculation( base ):
        return base.simple1 + base.simple2

    t = AnalysisTask( "complicated", complicatedCalculation, requires = [ simple1, simple2 ] )

    logger.info( "Task %r has result %r", t.name, t.result() )
