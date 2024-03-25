import sys
sys.path.append('path/to/src')
from logger import logging

def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frmae.f_code.co_filename
    error_message=" error occured in python scripts name[{0}] linenumber[{1}] error_message[{2}]".format(
        filename,exc_tb.tb_lineno.str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message