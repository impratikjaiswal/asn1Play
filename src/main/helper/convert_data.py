from src.generated_code.asn1.GSMA.SGP_22 import version
from src.main.convert.converter import parse_or_update_any_data_safe
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults


class ConvertData(object):
    def __init__(self):
        self.re_parse_output = None
        self.print_info = None
        self.print_input = None
        self.print_output = None
        self.asn1_element = None
        self.data_pool = []

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def set_asn_element(self, asn1_element):
        self.asn1_element = asn1_element

    def set_print_input(self, print_input):
        self.print_input = Defaults.PRINT_INPUT if print_input is None else print_input

    def set_print_output(self, print_output):
        self.print_output = Defaults.PRINT_OUTPUT if print_output is None else print_output

    def set_print_info(self, print_info):
        self.print_info = Defaults.PRINT_INFO if print_info is None else print_info

    def set_re_parse_output(self, re_parse_output):
        self.re_parse_output = Defaults.RE_PARSE_OUTPUT if re_parse_output is None else re_parse_output

    def parse(self, error_handling_mode):
        """

        :param error_handling_mode:
        :return:
        """
        for data in self.data_pool:
            if isinstance(data, Data):
                data.asn1_element = data.asn1_element if data.asn1_element is not None else self.asn1_element
                data.print_input = data.print_input if data.print_input is not None else self.print_input
                data.print_output = data.print_output if data.print_output is not None else self.print_output
                data.print_info = data.print_info if data.print_info is not None else self.print_info
                data.re_parse_output = data.re_parse_output if data.re_parse_output is not None else self.re_parse_output
            else:
                data = Data(raw_data=data, asn1_element=self.asn1_element, print_input=self.print_input,
                            print_info=self.print_info, re_parse_output=self.re_parse_output)
            # Path Correction as per versions
            if isinstance(data.raw_data, str) and '$VERSION' in data.raw_data:
                data.raw_data = data.raw_data.replace('$VERSION', version)
            parse_or_update_any_data_safe(data, error_handling_mode)
