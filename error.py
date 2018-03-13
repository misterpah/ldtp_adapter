class client_exception(Exception):
    LdtpExecutionError = ""
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
