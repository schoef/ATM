from standard import *

class HeppySampleTask( Task ):
    ''' Task to handle a grid job 
    '''

    db_file = None

    def __init__ ( self, heppy_sample_name ):
        super( HeppySampleTask, self ).__init__( '%s'%( heppy_sample_name ) )
        self.heppy_sample_name = heppy_sample_name
        self.cache = {}

    def result_from_cache( self ):
        return self.cache[ self.heppy_sample_name ]

    @property
    def requires( self ):
        return { 'proxy': ProxyCertificate() }
        
    @property
    def result( self ):
        try:
            return self.result_from_cache()
        except KeyError:

            import uuid
            self.cache[self.heppy_sample_name] = str(uuid.uuid4()) 

            return self.result 

heppy_sample_name = 'TTJets_NNNNNNLO'
s = HeppySampleTask( heppy_sample_name )
print s
