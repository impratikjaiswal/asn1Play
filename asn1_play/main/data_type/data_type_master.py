import traceback

import binascii
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData
from python_helpers.ph_exceptions import PhExceptions
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from ruamel.yaml.representer import RepresenterError

from asn1_play.main.convert import converter
from asn1_play.main.convert.converter import read_web_request
from asn1_play.main.convert.parser import parse_or_update_any_data
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.metadata import MetaData


class DataTypeMaster(object):
    def __init__(self):
        self.print_input = None
        self.print_output = None
        self.print_info = None
        self.output_file = None
        self.remarks_list = None
        self.re_parse_output = None
        self.output_file_name_keyword = None
        self.output_format = None
        self.input_format = None
        self.asn1_element = None
        self.data_pool = []
        self.__master_data = (Data(raw_data=None), MetaData(raw_data_org=None), PhExceptions(msg=None))

    def set_print_input(self, print_input):
        self.print_input = print_input

    def set_print_output(self, print_output):
        self.print_output = print_output

    def set_print_info(self, print_info):
        self.print_info = print_info

    def set_output_file(self, output_file):
        self.output_file = output_file

    def set_remarks_list(self, remarks_list):
        self.remarks_list = remarks_list

    def set_re_parse_output(self, re_parse_output):
        self.re_parse_output = re_parse_output

    def set_output_file_name_keyword(self, output_file_name_keyword):
        self.output_file_name_keyword = output_file_name_keyword

    def set_output_format(self, output_format):
        self.output_format = output_format

    def set_input_format(self, input_format):
        self.input_format = input_format

    def set_asn1_element(self, asn1_element):
        self.asn1_element = asn1_element

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def parse_safe(self, error_handling_mode, data=None):
        """

        :param data:
        :param error_handling_mode:
        :return:
        """
        if data is None:
            data = self.data_pool
        if isinstance(data, list):
            """
            Handle Pool
            """
            for data_item in data:
                self.parse_safe(error_handling_mode=error_handling_mode, data=data_item)
            return
        """
        Handle Individual Request
        """
        try:
            if isinstance(data, dict):
                """
                Web Form
                """
                data = read_web_request(data)
            self.__parse_safe_individual(data)
        except Exception as e:
            known = False
            additional_msg = None
            if isinstance(e.args[0], PhExceptions):
                exception_msg = e.args[0].get_details()
                self.__master_data = (
                    self.__master_data[PhMasterData.INDEX_DATA], self.__master_data[PhMasterData.INDEX_META_DATA],
                    e.args[0])
            else:
                # for scenarios like FileExistsError where a touple is returned, (17, 'Cannot create a file when that file already exists')
                exception_msg = str(e)
                self.__master_data = (
                    self.__master_data[PhMasterData.INDEX_DATA], self.__master_data[PhMasterData.INDEX_META_DATA],
                    PhExceptions(exception_msg))
            if isinstance(e, binascii.Error):
                known = True
                additional_msg = 'raw_data is invalid'
            elif isinstance(e, ValueError):
                known = True
            elif isinstance(e, RepresenterError):
                known = True
                additional_msg = 'export error'
            elif isinstance(e, PermissionError):
                known = True
                additional_msg = 'input/output path reading/writing error'
            elif isinstance(e, FileExistsError):
                known = True
                additional_msg = 'Output path writing error'
            elif isinstance(e, AttributeError):
                known = True
                additional_msg = 'Input/OutPut/AsnElement is not correct'
            processed_data = self.__master_data[PhMasterData.INDEX_DATA]
            processed_meta_data = self.__master_data[PhMasterData.INDEX_META_DATA]
            converter.print_data(processed_data, processed_meta_data)
            msg = PhUtil.get_key_value_pair(PhConstants.EXCEPTION_KNOWN if known else PhConstants.EXCEPTION_UNKNOWN,
                                            PhConstants.SEPERATOR_MULTI_OBJ.join(
                                                filter(None, [additional_msg, exception_msg])))
            print(f'{msg}')
            if not known:
                traceback.print_exc()
            if error_handling_mode == PhErrorHandlingModes.STOP_ON_ERROR:
                raise

    def __parse_safe_individual(self, data):
        """
        Handle Individual Request
        :param data:
        :return:
        """
        if isinstance(data, Data):
            data.print_input = data.print_input if data.print_input is not None else self.print_input
            data.print_output = data.print_output if data.print_output is not None else self.print_output
            data.print_info = data.print_info if data.print_info is not None else self.print_info
            data.output_file = data.output_file if data.output_file is not None else self.output_file
            data.remarks_list = data.remarks_list if data.remarks_list is not None else self.remarks_list
            data.asn1_element = data.asn1_element if data.asn1_element is not None else self.asn1_element
            data.input_format = data.input_format if data.input_format is not None else self.input_format
            data.output_format = data.output_format if data.output_format is not None else self.output_format
            data.re_parse_output = data.re_parse_output if data.re_parse_output is not None else self.re_parse_output
            data.output_file_name_keyword = data.output_file_name_keyword if data.output_file_name_keyword is not None else self.output_file_name_keyword
        else:
            data = Data(
                raw_data=data,
                print_input=self.print_input,
                print_output=self.print_output,
                print_info=self.print_info,
                output_file=self.output_file,
                remarks_list=self.remarks_list,
                asn1_element=self.asn1_element,
                input_format=self.input_format,
                output_format=self.output_format,
                re_parse_output=self.re_parse_output,
                output_file_name_keyword=self.output_file_name_keyword,
            )
        converter.path_generalisation(data, PhKeys.RAW_DATA)
        converter.path_generalisation(data, PhKeys.OUTPUT_FILE)
        converter.path_generalisation(data, PhKeys.REMARKS_LIST)
        meta_data = MetaData(raw_data_org=data.raw_data)
        self.__master_data = (data, meta_data)
        parse_or_update_any_data(data, meta_data)

    def get_output_data(self):
        """

        :return:
        """
        output_data = ''
        if len(self.__master_data) > PhMasterData.INDEX_ERROR_DATA:
            # Exception Object is Present
            exception_data = self.__master_data[PhMasterData.INDEX_ERROR_DATA]
            output_data = exception_data.get_details() if isinstance(exception_data, PhExceptions) else exception_data
            return output_data
        if len(self.__master_data) > PhMasterData.INDEX_META_DATA:
            # MetaData Object is Present
            meta_data = self.__master_data[PhMasterData.INDEX_META_DATA]
            output_data = meta_data.parsed_data if isinstance(meta_data, MetaData) else output_data
        return output_data