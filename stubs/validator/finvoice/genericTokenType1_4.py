        if ( isinstance( value, BaseStrType_ ) ):
            if ( 1 <= value.__len__() <= 4 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 1..4 characters' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and 1 <= v.__len__() <= 4 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 1..4 characters' )
        import re
        return re.sub( ' {2,}',' ', re.sub( '\t|\r|\n', '', value.strip() ) )
