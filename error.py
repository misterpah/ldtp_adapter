class LdtpExecutionError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
        
class client_exception(Exception):
    LdtpExecutionError = LdtpExecutionError
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
        
        

