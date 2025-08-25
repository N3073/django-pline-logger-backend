from collections.abc import Callable

def debug_printer(bDebug:bool)->Callable[[str],None]:
    if bDebug:
        return print
    else:
        def func(string:str)->None:
            return
        return func
