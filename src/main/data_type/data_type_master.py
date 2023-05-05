from src.main.convert import converter
from src.main.convert.parser import parse_or_update_any_data_safe
from src.main.helper.data import Data
from src.main.helper.keys import Keys


class DataTypeMaster(object):
    def __init__(self):
        self.print_input = None
        self.print_output = None
        self.print_info = None
        self.re_parse_output = None
        self.output_file = None
        self.output_file_name_keyword = None
        self.remarks_list = None
        self.output_format = None
        self.input_format = None
        self.asn1_element = None
        self.data_pool = []

    def set_print_input(self, print_input):
        self.print_input = print_input

    def set_print_output(self, print_output):
        self.print_output = print_output

    def set_print_info(self, print_info):
        self.print_info = print_info

    def set_re_parse_output(self, re_parse_output):
        self.re_parse_output = re_parse_output

    def set_output_file(self, output_file):
        self.output_file = output_file

    def set_output_file_name_keyword(self, output_file_name_keyword):
        self.output_file_name_keyword = output_file_name_keyword

    def set_remarks_list(self, remarks_list):
        self.remarks_list = remarks_list

    def set_output_format(self, output_format):
        self.output_format = output_format

    def set_input_format(self, input_format):
        self.input_format = input_format

    def set_asn1_element(self, asn1_element):
        self.asn1_element = asn1_element

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def parse(self, error_handling_mode):
        """

        :param error_handling_mode:
        :return:
        """
        for data in self.data_pool:
            if isinstance(data, Data):
                data.asn1_element = data.asn1_element if data.asn1_element is not None else self.asn1_element
                data.input_format = data.input_format if data.input_format is not None else self.input_format
                data.output_format = data.output_format if data.output_format is not None else self.output_format
                data.print_input = data.print_input if data.print_input is not None else self.print_input
                data.print_output = data.print_output if data.print_output is not None else self.print_output
                data.print_info = data.print_info if data.print_info is not None else self.print_info
                data.re_parse_output = data.re_parse_output if data.re_parse_output is not None else self.re_parse_output
                data.output_file = data.output_file if data.output_file is not None else self.output_file
                data.output_file_name_keyword = data.output_file_name_keyword if data.output_file_name_keyword is not None else self.output_file_name_keyword
                data.remarks_list = data.remarks_list if data.remarks_list is not None else self.remarks_list
            else:
                data = Data(
                    raw_data=data,
                    asn1_element=self.asn1_element,
                    input_format=self.input_format,
                    output_format=self.output_format,
                    print_input=self.print_input,
                    print_output=self.print_output,
                    print_info=self.print_info,
                    re_parse_output=self.re_parse_output,
                    output_file=self.output_file,
                    output_file_name_keyword=self.output_file_name_keyword,
                    remarks_list=self.remarks_list,
                )
            converter.path_generalisation(data, Keys.RAW_DATA)
            converter.path_generalisation(data, Keys.OUTPUT_FILE)
            converter.path_generalisation(data, Keys.REMARKS_LIST)
            parse_or_update_any_data_safe(data, error_handling_mode)
