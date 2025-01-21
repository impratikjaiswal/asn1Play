import subprocess
import traceback

import binascii
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from ruamel.yaml.representer import RepresenterError

from asn1_play.generated_code.asn1.GSMA.SGP_22 import default_asn_version_sgp22
from asn1_play.generated_code.asn1.GSMA.SGP_32 import default_asn_version_sgp32
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import default_asn_version_epp
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.main.convert import converter
from asn1_play.main.convert.converter import handle_web_request, set_defaults
from asn1_play.main.convert.parser import process_all_data_types
from asn1_play.main.helper.data import Data
from asn1_play.main.helper.infodata import InfoData
from asn1_play.main.helper.keywords import KeyWords
from asn1_play.main.helper.metadata import MetaData


class DataTypeMaster(object):
    def __init__(self):
        # Common Objects
        self.print_input = None
        self.print_output = None
        self.print_info = None
        self.quite_mode = None
        self.remarks = None
        self.encoding = None
        self.encoding_errors = None
        self.output_path = None
        self.output_file_name_keyword = None
        self.archive_output = None
        self.archive_output_format = None
        # Specific Objects
        self.input_format = None
        self.output_format = None
        self.asn1_element = None
        self.tlv_parsing_of_output = None
        self.re_parse_output = None
        self.data_pool = []
        self.__master_data = PhMasterData(
            data=Data(input_data=None),
            meta_data=MetaData(input_data_org=None),
            error_data=PhExceptionHelper(msg_key=None),
            info_data=InfoData(info=None)
        )

    def set_print_input(self, print_input):
        self.print_input = print_input

    def set_print_output(self, print_output):
        self.print_output = print_output

    def set_print_info(self, print_info):
        self.print_info = print_info

    def set_quiet_mode(self, quite_mode):
        self.quite_mode = quite_mode

    def set_remarks(self, remarks):
        self.remarks = remarks

    def set_encoding(self, encoding):
        self.encoding = encoding

    def set_encoding_errors(self, encoding_errors):
        self.encoding_errors = encoding_errors

    def set_output_path(self, output_path):
        self.output_path = output_path

    def set_output_file_name_keyword(self, output_file_name_keyword):
        self.output_file_name_keyword = output_file_name_keyword

    def set_archive_output(self, archive_output):
        self.archive_output = archive_output

    def set_archive_output_format(self, archive_output_format):
        self.archive_output_format = archive_output_format

    def set_input_format(self, input_format):
        self.input_format = input_format

    def set_output_format(self, output_format):
        self.output_format = output_format

    def set_asn1_element(self, asn1_element):
        self.asn1_element = asn1_element

    def set_tlv_parsing_of_output(self, tlv_parsing_of_output):
        self.tlv_parsing_of_output = tlv_parsing_of_output

    def set_re_parse_output(self, re_parse_output):
        self.re_parse_output = re_parse_output

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def process_safe(self, error_handling_mode, data=None):
        """

        :param data:
        :param error_handling_mode:
        :return:
        """
        if data is None:
            data = self.data_pool
        if isinstance(data, list):
            """
            Handle Requests Pool; Multiple Data Request are sent
            """
            for data_item in data:
                self.process_safe(error_handling_mode=error_handling_mode, data=data_item)
            return
        """
        Handle Individual Request
        """
        try:
            if isinstance(data, dict):
                """
                Web Form
                """
                data = handle_web_request(data)
            self.__process_safe_individual(data)
        except Exception as e:
            known = False
            summary_msg = None
            exception_object = e.args[0] if len(e.args) > 0 else e
            if not isinstance(exception_object, PhExceptionHelper):
                # for scenarios like FileExistsError where a touple is returned, (17, 'Cannot create a file when that file already exists')
                exception_object = PhExceptionHelper(exception=e)
            if isinstance(e, binascii.Error):
                known = True
                summary_msg = PhConstants.INVALID_INPUT_DATA
            elif isinstance(e, ValueError):
                known = True
                summary_msg = PhConstants.INPUTS_ERROR
            elif isinstance(e, RepresenterError):
                known = True
                summary_msg = PhConstants.EXPORT_ERROR
            elif isinstance(e, PermissionError):
                known = True
                summary_msg = PhConstants.READ_WRITE_ERROR
            elif isinstance(e, FileExistsError):
                known = True
                summary_msg = PhConstants.WRITE_PATH_ERROR
            elif isinstance(e, AttributeError):
                known = True
                summary_msg = PhConstants.INPUTS_ERROR
            elif isinstance(e, subprocess.TimeoutExpired):
                known = True
                summary_msg = PhConstants.TIME_OUT_ERROR
            elif isinstance(e, subprocess.CalledProcessError):
                known = True
                summary_msg = e.stderr if e.stderr else PhConstants.NON_ZERO_EXIT_STATUS_ERROR
            exception_object.set_summary_msg(summary_msg)
            self.__master_data.set_master_data(PhMasterDataKeys.ERROR_DATA, exception_object)
            converter.print_data(master_data=self.__master_data)
            msg = PhConstants.SEPERATOR_TWO_WORDS.join(
                [PhConstants.KNOWN if known else PhConstants.UNKNOWN, exception_object.get_details()])
            print(f'{msg}')
            if not known:
                traceback.print_exc()
            if error_handling_mode == PhErrorHandlingModes.STOP_ON_ERROR:
                raise

    def __process_safe_individual(self, data):
        """
        Handle Individual Request
        :param data:
        :return:
        """
        if isinstance(data, Data):
            data.print_input = data.print_input if data.print_input is not None else self.print_input
            data.print_output = data.print_output if data.print_output is not None else self.print_output
            data.print_info = data.print_info if data.print_info is not None else self.print_info
            data.quite_mode = data.quite_mode if data.quite_mode is not None else self.quite_mode
            data.remarks = data.remarks if data.remarks is not None else self.remarks
            data.encoding = data.encoding if data.encoding is not None else self.encoding
            data.encoding_errors = data.encoding_errors if data.encoding_errors is not None else self.encoding_errors
            data.output_path = data.output_path if data.output_path is not None else self.output_path
            data.output_file_name_keyword = data.output_file_name_keyword if data.output_file_name_keyword is not None else self.output_file_name_keyword
            data.archive_output = data.archive_output if data.archive_output is not None else self.archive_output
            data.archive_output_format = data.archive_output_format if data.archive_output_format is not None else self.archive_output_format
            data.input_format = data.input_format if data.input_format is not None else self.input_format
            data.output_format = data.output_format if data.output_format is not None else self.output_format
            data.asn1_element = data.asn1_element if data.asn1_element is not None else self.asn1_element
            data.tlv_parsing_of_output = data.tlv_parsing_of_output if data.tlv_parsing_of_output is not None else self.tlv_parsing_of_output
            data.re_parse_output = data.re_parse_output if data.re_parse_output is not None else self.re_parse_output
        else:
            data = Data(
                input_data=data,
                print_input=self.print_input,
                print_output=self.print_output,
                print_info=self.print_info,
                quite_mode=self.quite_mode,
                remarks=self.remarks,
                encoding=self.encoding,
                encoding_errors=self.encoding_errors,
                output_path=self.output_path,
                output_file_name_keyword=self.output_file_name_keyword,
                archive_output=self.archive_output,
                archive_output_format=self.archive_output_format,
                input_format=self.input_format,
                output_format=self.output_format,
                asn1_element=self.asn1_element,
                tlv_parsing_of_output=self.tlv_parsing_of_output,
                re_parse_output=self.re_parse_output,
            )
        current_asn1_element = data.get_asn1_element()
        if current_asn1_element:
            if isinstance(current_asn1_element, Asn1):
                pass
            elif isinstance(current_asn1_element, str):
                data.set_asn1_element(Asn1(asn1_object=current_asn1_element))
            else:  # Existing Asn Object; Legacy Code
                name = current_asn1_element.fullname()
                mod = current_asn1_element._mod
                asn1_schema = None
                if mod:
                    if mod == KeyWords.MODULE_SGP22:
                        asn1_schema = default_asn_version_sgp22
                    if mod == KeyWords.MODULE_SGP32:
                        asn1_schema = default_asn_version_sgp32
                    if mod == KeyWords.MODULE_EPP:
                        asn1_schema = default_asn_version_epp
                data.set_asn1_element(Asn1(asn1_schema=asn1_schema, asn1_object=name))
        converter.path_generalisation(data, PhKeys.INPUT_DATA)
        converter.path_generalisation(data, PhKeys.OUTPUT_FILE)
        converter.path_generalisation(data, PhKeys.REMARKS)
        meta_data = MetaData(input_data_org=data.input_data)
        info_data = InfoData()
        self.__master_data = PhMasterData(data=data, meta_data=meta_data, error_data=None, info_data=info_data)
        process_all_data_types(data, meta_data, info_data)

    def get_output_data(self, only_output=True):
        """

        :return:
        """
        return self.__master_data.get_output_data(only_output=only_output)

    def to_dic(self, data):
        """

        :param data:
        :return:
        """
        set_defaults(data, None)
        common_data = {
            #
            PhKeys.INPUT_DATA: data.input_data,
            PhKeys.PRINT_INPUT: data.print_input,
            PhKeys.PRINT_OUTPUT: data.print_output,
            PhKeys.PRINT_INFO: data.print_info,
            PhKeys.QUITE_MODE: data.quite_mode,
            PhKeys.REMARKS: data.get_remarks_as_str(),
            PhKeys.ENCODING: data.encoding,
            PhKeys.ENCODING_ERRORS: data.encoding_errors,
            PhKeys.OUTPUT_PATH: data.output_path,
            PhKeys.OUTPUT_FILE_NAME_KEYWORD: data.output_file_name_keyword,
            PhKeys.ARCHIVE_OUTPUT: data.archive_output,
            PhKeys.ARCHIVE_OUTPUT_FORMAT: data.archive_output_format,
            #
            PhKeys.INPUT_FORMAT: data.input_format,
            PhKeys.OUTPUT_FORMAT: data.output_format,
            # asn1_element
            PhKeys.RE_PARSE_OUTPUT: data.re_parse_output,
            PhKeys.TLV_PARSING_OF_OUTPUT: data.tlv_parsing_of_output,
            #
            PhKeys.DATA_GROUP: data.data_group,
        }
        return PhUtil.dict_clean(PhUtil.dict_merge(common_data, data.get_asn1_element_info()))
