
import helpers
from Task import Task

class ProxyCertificate( Task ):
    ''' Task to hold the grid proxy certificate
    '''

    # https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

    import helpers
    __metaclass__ = type( 'ProxyCertificateMeta', (type(Task), helpers.Singleton), {} )

    filename = 'default'

    def __init__ ( self ):
        super( ProxyCertificate, self ).__init__( 'proxy' )

    @property
    def result( self ):
        return "Here it is: %s" % self.filename

