class MetaData:
    def __init__(self,
                 raw_data_org,
                 asn1_element=None,
                 operation_mode=None,
                 input_mode_key=None,
                 input_mode_value=None,
                 output_file_name=None,
                 default_output_file_name=None,
                 re_output_file_name=None,
                 parsed_data=None,
                 re_parsed_data=None,
                 include_files=None,
                 excludes=None,
                 ):
        self.raw_data_org = raw_data_org
        self.asn1_element_name = None
        self.set_asn1_element_name(asn1_element)
        self.operation_mode = operation_mode
        self.input_mode_key = input_mode_key
        self.input_mode_value = str(self.raw_data_org)
        self.default_output_file_name = default_output_file_name
        self.output_file_name = output_file_name
        self.re_output_file_name = re_output_file_name
        self.parsed_data = parsed_data
        self.re_parsed_data = re_parsed_data
        self.include_files = include_files
        self.excludes = excludes

    def set_asn1_element_name(self, asn1_element):
        self.asn1_element_name = asn1_element.fullname() if asn1_element else None
