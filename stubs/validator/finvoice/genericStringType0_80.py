        if ( isinstance( value, BaseStrType_ ) ):
            if ( 0 <= value.__len__() <= 80 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 0..80 characters' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and 0 <= v.__len__() <= 80 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 0..80 characters' )
        return value
