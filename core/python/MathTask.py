from Task import Task

# Logging
import logging
logger = logging.getLogger( __name__ )

# Retry decorator
class retry():
    ''' Decorator, that retries 'n_retry' times on exceptions 'excpetion'
    '''
    def __init__(self, n_retry, exception ):
        # how often to try
        self.n_retry    = n_retry
        # which exceptions to catch
        self.exception  = exception

    def __call__(self, cls):
        class Wrapped( cls ):

            n_retry     = self.n_retry # n_retry is attribute of the decorated class
            exception   = self.exception

            # Implement retry loop
            def _evaluate( self ):
                counter = 0
                while True: #for i in range( Wrapped.n_retry ):

                    if counter == 0:
                        logger.debug( "First try" )
                    else:
                        logger.info( "Retry number %i.", counter )

                    try:
                        return super(Wrapped, self)._evaluate()
                    except Wrapped.exception:
                        if counter >= Wrapped.n_retry:
                            raise # A blank raise rereaises the last exception. Needed for stacktrace
                        else:
                            counter += 1
                            continue
        return Wrapped

#@retry( 2, RuntimeError)
class AnalysisTask( Task ):

    def __init__( self, name, function, requires = None):
        #super(AnalysisTask, self).__init__( name, requires) #That creates an infinite recursion because the retry decorator makes a new class
        Task.__init__( self, name, requires)
        self._function = function

    def _evaluate( self ):
        logger.info( "Evaluating AnalysisTask %r", self.name )
        result = self._function( self )
        logger.debug( "Result for task %r is %r", self.name, result )
        return result

if __name__ == "__main__":

    import logger as logger
    logger = logger.get_logger('DEBUG')

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
