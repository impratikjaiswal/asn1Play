from src.main.helper.defaults import Defaults


class Data:
    def __init__(self,
                 raw_data,
                 asn1_element=None,
                 input_format=None,
                 output_format=None,
                 print_input=None,
                 print_info=None,
                 re_parse_output=None,
                 ):
        self.raw_data = raw_data
        self.asn1_element = asn1_element
        self.input_format = Defaults.FORMAT_INPUT if input_format is None else input_format
        self.output_format = Defaults.FORMAT_OUTPUT if output_format is None else output_format
        self.print_input = Defaults.PRINT_INPUT if print_input is None else print_input
        self.print_info = Defaults.PRINT_INFO if print_info is None else print_info
        self.re_parse_output = Defaults.RE_PARSE_OUTPUT if re_parse_output is None else re_parse_output
