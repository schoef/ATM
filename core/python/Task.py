''' Analysis Task Manager - core functionality of task 
'''

# Abstract class
import abc

# Logging
import logging
logger = logging.getLogger( __name__ )

class Task:
    __metaclass__ = abc.ABCMeta

    def __init__( self, name, requires = None ):

        self.name       = name
        self.requires   = requires

        return

    def result( self ):
        ''' Return result of the task
        '''

        # Evaluate everything the task depends on
        if self.requires is not None:
            if isinstance( self.requires, (list, tuple)):
                for requirement in self.requires:
                    setattr( self, requirement.name, requirement.result() )
            else:
                raise ValueError( "Don't know what the class requires. Expect list or tuple of tasks. Got %r" % self.requires )

        # Evaluate the task 
        return self._evaluate()

    @abc.abstractmethod
    def _evaluate( self ):
        ''' Evaluate result
        '''
        return
