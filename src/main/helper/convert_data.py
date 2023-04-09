import traceback

from src.main.convert.converter import parse_or_update_any_data
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults
from src.main.helper.modes_error_handling import ErrorHandlingModes


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

    def parse(self, error_handling_mode):
        """

        :param error_handling_mode:
        :return:
        """
        for data in self.data_pool:
            try:
                if isinstance(data, Data):
                    data.asn1_element = data.asn1_element if data.asn1_element else self.asn1_element
                    data.print_input = data.print_input if data.print_input else self.print_input
                    data.print_info = data.print_info if data.print_info else self.print_info
                    data.re_parse_output = data.re_parse_output if data.re_parse_output else self.re_parse_output
                else:
                    data = Data(raw_data=data, asn1_element=self.asn1_element, print_input=self.print_input,
                                print_info=self.print_info, re_parse_output=self.re_parse_output)
                parse_or_update_any_data(data)
            except Exception as e:
                traceback.print_exc()
                print(f'Exception Occurred {e}')
                if error_handling_mode == ErrorHandlingModes.STOP_ON_ERROR:
                    raise
