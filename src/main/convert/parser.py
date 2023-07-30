import copy
import os
import traceback
from collections import OrderedDict

import binascii
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_constants_config import PhConfigConst
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from ruamel.yaml.representer import RepresenterError

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.convert import converter
from src.main.convert.handler import decode_encode_asn
from src.main.helper.constants_config import ConfigConst as ConfigConst_local
from src.main.helper.formats import Formats
from src.main.helper.formats_group import FormatsGroup
from src.main.helper.keys import Keys
from src.main.helper.metadata import MetaData


def parse_or_update_any_data_safe(data, error_handling_mode):
    try:
        meta_data = MetaData(raw_data_org=data.raw_data)
        return parse_or_update_any_data(data, meta_data)
    except Exception as e:
        known = False
        additional_msg = None
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
        converter.print_data(data, meta_data)
        print(PhUtil.get_key_value_pair(PhConstants.EXCEPTION_KNOWN if known else PhConstants.EXCEPTION_UNKNOWN,
                                        PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [additional_msg, str(e)]))))
        if not known:
            traceback.print_exc()
        if error_handling_mode == PhErrorHandlingModes.STOP_ON_ERROR:
            raise
        return None


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    """
    Bulk Mode
    """
    converter.set_defaults_for_printing(data)
    byte_array_format = True if data.input_format in FormatsGroup.INPUT_FORMATS_BYTE_ARRAY else False
    if meta_data is None:
        meta_data = MetaData(raw_data_org=data.raw_data)
    if not byte_array_format and isinstance(data.raw_data, list):
        # List is provided
        meta_data.input_mode_key = Keys.INPUT_LIST
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        data.set_auto_generated_remarks_if_needed()
        data.set_one_time_remarks(f'({len(data.raw_data)} Elements)')
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        converter.print_data(data, meta_data)
        parsed_data_list = []
        actual_remarks_length = len(data.remarks_list)
        current_remarks_list = PhUtil.extend_list(data.remarks_list, expected_length=len(data.raw_data))
        for index, raw_data_item in enumerate(data.raw_data, start=1):
            sub_data = copy.deepcopy(data)
            sub_data.raw_data = raw_data_item
            sub_data.reset_auto_generated_remarks()
            sub_data.set_extended_remarks_available(False if index <= actual_remarks_length else True)
            sub_data.set_user_remarks(current_remarks_list[index - 1])
            sub_data.set_auto_generated_remarks_if_needed(PhUtil.get_key_value_pair(key='item', value=index,
                                                                                    sep=PhConstants.SEPERATOR_TWO_WORDS,
                                                                                    dic_format=False))
            parsed_data_list.append(parse_or_update_any_data(sub_data))
        return parsed_data_list
    if not byte_array_format and data.raw_data and os.path.isdir(os.path.abspath(data.raw_data)):
        # directory is provided
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        meta_data.input_mode_key = Keys.INPUT_DIR
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        converter.print_data(data, meta_data)
        converter.set_includes_excludes_files(data, meta_data)
        files_list = PhUtil.traverse_it(top=os.path.abspath(data.raw_data), traverse_mode='Regex',
                                        include_files=meta_data.include_files, excludes=meta_data.excludes)
        if files_list:
            files_list_data = data
            files_list_data.raw_data = files_list
            return parse_or_update_any_data(files_list_data)
    """
    Individual
    """
    file_dic_all_str = {}
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    if not byte_array_format and data.raw_data and os.path.isfile(data.raw_data):
        # file is provided
        try:
            with open(data.raw_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(data.raw_data, 'rb') as the_file:
                resp = the_file.read()
        file_ext = PhUtil.get_file_name_and_extn(file_path=data.raw_data, only_extn=True)
        if file_ext in FormatsGroup.INPUT_FILE_FORMATS_YML:
            meta_data.input_mode_key = Keys.INPUT_YML
            file_dic_all_str, data = converter.read_yaml(resp)
            converter.set_defaults_for_printing(data)
        else:
            meta_data.input_mode_key = Keys.INPUT_FILE
            converter.set_input_output_format(data)
            data.raw_data = resp
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
    # print_data(data, meta_data)
    # Needed for scenario when remarks will be fetched from YML
    data.set_auto_generated_remarks_if_needed()
    converter.set_defaults(data, meta_data)
    converter.set_output_file_path(data, meta_data)
    converter.set_re_output_file_name(data, meta_data)
    if meta_data.export_mode:
        converter.print_data(data, meta_data)
        converter.write_yml_file(meta_data.output_file_path, converter.prepare_config_data(data))
        return None
    output_versions_dic = OrderedDict()
    output_versions_dic.update(PhUtil.get_tool_name_w_version(dic_format=True))
    output_versions_dic.update(
        PhUtil.get_tool_name_w_version(PhConfigConst.TOOL_NAME, PhConfigConst.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(
        PhUtil.get_tool_name_w_version(ConfigConst_local.TOOL_NAME, ConfigConst_local.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(PhUtil.get_tool_name_w_version(Keys.SGP22, sgp_22_version, dic_format=True))
    output_versions_dic.update(PhUtil.get_tool_name_w_version(Keys.EUICC_PROFILE_PACKAGE, epp_version, dic_format=True))
    output_versions_dic.update(
        PhUtil.get_key_value_pair(Keys.TIME_STAMP, PhUtil.get_time_stamp(files_format=False), dic_format=True))
    # parse Data
    meta_data.parsed_data = decode_encode_asn(raw_data=data.raw_data, parse_only=True, input_format=data.input_format,
                                              output_format=data.output_format, asn1_element=data.asn1_element)
    if data.re_parse_output:
        meta_data.re_parsed_data = decode_encode_asn(raw_data=meta_data.parsed_data, parse_only=True,
                                                     input_format=data.output_format,
                                                     output_format=data.input_format, asn1_element=data.asn1_element)
    converter.print_data(data, meta_data)
    if meta_data.input_mode_key == Keys.INPUT_YML:
        converter.write_yml_file(meta_data.output_file_path, file_dic_all_str, meta_data.output_dic,
                                 output_versions_dic)
    elif meta_data.output_file_path:
        PhUtil.makedirs(PhUtil.get_file_name_and_extn(file_path=meta_data.output_file_path, only_path=True))
        converter.write_output_file(meta_data.output_file_path, meta_data.parsed_data)
        if meta_data.re_parsed_data:
            converter.write_output_file(meta_data.re_output_file_path, meta_data.re_parsed_data)
    return meta_data.parsed_data
