## A child went to toy shop with his father,to buy a topy 
## child = customException
## Toy = Error message
## Father = main Exception
## cctv in shop = sys


import sys ## CCtv of toy shop


def error_message_detail(error_msg,error_detail:sys):

    ''' Crafting our own custom message'''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error_msg))
    
    return error_message





class CustomException(Exception):   ## customException is child
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message


    