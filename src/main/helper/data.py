class Data:
    def __init__(self,
                 raw_data,
                 asn1_element=None,
                 input_format=None,
                 output_format=None,
                 print_input=None,
                 print_info=None,
                 re_parse_output=None,
                 output_file=None,
                 ):
        self.raw_data = raw_data
        self.asn1_element = asn1_element
        self.input_format = input_format
        self.output_format = output_format
        self.print_input = print_input
        self.print_info = print_info
        self.re_parse_output = re_parse_output
        self.output_file = output_file
