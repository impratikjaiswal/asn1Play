from collections import OrderedDict


class MetaData:
    def __init__(self,
                 raw_data_org,
                 operation_mode=None,
                 input_mode_key=None,
                 output_file_name=None,
                 default_output_file_ext=None,
                 re_output_file_name=None,
                 parsed_data=None,
                 re_parsed_data=None,
                 include_files=None,
                 excludes=None,
                 ):
        self.raw_data_org = raw_data_org
        self.operation_mode = operation_mode
        self.input_mode_key = input_mode_key
        self.input_mode_value = str(self.raw_data_org)
        self.default_output_file_ext = default_output_file_ext
        self.output_file_name = output_file_name
        self.re_output_file_name = re_output_file_name
        self.parsed_data = parsed_data
        self.re_parsed_data = re_parsed_data
        self.include_files = include_files
        self.excludes = excludes
        self.output_dic = OrderedDict()
