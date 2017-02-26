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
