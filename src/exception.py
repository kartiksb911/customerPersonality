import sys

def error_msg_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    return f"Error in file [{file_name}], line [{exc_tb.tb_lineno}], message [{str(error)}]"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message