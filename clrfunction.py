import clr
def create_cs_function(name, code, dependencies = None):
    clr.AddReference("MagicIPython")
    from MagicIPython import MagicCS
    from System import String
    from System.Collections.Generic import List
 
    if dependencies is not None and len(dependencies) > 0 :
        myarray = List[String]()
        for i,d in enumerate(dependencies):
            myarray.Add( d )
        myarray = myarray.ToArray()
    else:
        myarray = List[String]().ToArray()
     
    obj = MagicCS.CreateFunction(name, code, myarray)
    return lambda *params: run_cs_function(obj, params)
 
def run_cs_function(func, params):
    clr.AddReference("MagicIPython")
    from MagicIPython import MagicCS
    from System.Collections.Generic import List
    from System import Object
 
    par = List[Object]()
    for p in params :
        par.Add ( p )
    return MagicCS.RunFunction(func, par.ToArray())
