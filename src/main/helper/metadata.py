from collections import OrderedDict


class MetaData:
    def __init__(self, raw_data_org):
        self.raw_data_org = raw_data_org
        self.operation_mode = None
        self.input_mode_key = None
        self.output_file_name = None
        self.default_output_file_ext = None
        self.re_output_file_name = None
        self.parsed_data = None
        self.re_parsed_data = None
        self.include_files = None
        self.excludes = None
        self.export_mode = None
        self.output_dic = OrderedDict()
        self.input_mode_value = str(self.raw_data_org)
