        if ( isinstance( value, BaseStrType_ ) ):
            if ( 1 <= value.__len__() <= 20 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 1..20 characters' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and 1 <= v.__len__() <= 20 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 1..20 characters' )
        return value
