import traceback

from src.main.convert.converter import parse_or_update_any_data
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults


class ConvertData(object):
    def __init__(self):
        self.re_parse_output = None
        self.print_info = None
        self.print_input = None
        self.asn1_element = None
        self.data_pool = []

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def set_asn_element(self, asn1_element):
        self.asn1_element = asn1_element

    def set_print_input(self, print_input):
        self.print_input = Defaults.PRINT_INPUT if print_input is None else print_input

    def set_print_info(self, print_info):
        self.print_info = Defaults.PRINT_INFO if print_info is None else print_info

    def set_re_parse_output(self, re_parse_output):
        self.re_parse_output = Defaults.RE_PARSE_OUTPUT if re_parse_output is None else re_parse_output

    def parse(self):
        for data in self.data_pool:
            try:
                if isinstance(data, Data):
                    parse_or_update_any_data(
                        data.raw_data,
                        print_input=data.print_input,
                        print_info=data.print_info,
                        re_parse_output=data.re_parse_output,
                        asn1_element=data.asn1_element if data.asn1_element else self.asn1_element,
                        input_format=data.input_format,
                        output_format=data.output_format
                    )
                else:
                    parse_or_update_any_data(
                        data,
                        print_input=self.print_input,
                        print_info=self.print_info,
                        re_parse_output=self.re_parse_output,
                        asn1_element=self.asn1_element
                    )
            except Exception as e:
                traceback.print_exc()
                print(f'Exception Occurred {e}')
