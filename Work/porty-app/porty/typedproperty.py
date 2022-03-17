'''
Created on 04.03.2022

@author: ho_ksk
__updated__='2022-03-05 10:01:19'
'''

# typedproperty.py


def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Got {value} but expected type is {expected_type}')
        setattr(self, private_name, value)
        
        
    return prop

String  = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float   = lambda name: typedproperty(name, float)
