''' Task base class
'''

import abc

class Task:
    __metaclass__ = abc.ABCMeta

    def __init__( self, name ):
        self.name = name

    def __str__( self ):
        return self.__print()

    def __print( self, prefix = "" ):
        return  "class: {classname}, name: {name} {subtasks}".format(
            classname = type( self ).__name__,
            name = self.name,
            subtasks = "".join( '\n'+prefix+'-- uses %r'%k+': '+t.__print( prefix = prefix+'--') for k, t in self.requires.iteritems() )
            )

    @property
    def requires( self ):
        return {}

    @property
    @abc.abstractmethod
    def result( self ):
        pass
