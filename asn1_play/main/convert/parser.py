import copy
import os
from collections import OrderedDict

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_constants_config import PhConfigConst
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modules import PhModules
from python_helpers.ph_util import PhUtil
from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.helper.constants_config import ConfigConst as tlvConfigConst
from tlv_play.main.helper.data import Data

from asn1_play.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from asn1_play.generated_code.asn1.GSMA.SGP_32 import version as sgp_32_version
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.main.convert import converter
from asn1_play.main.convert.handler import handle_data
from asn1_play.main.helper.constants_config import ConfigConst
from asn1_play.main.helper.formats_group import FormatsGroup
from asn1_play.main.helper.infodata import InfoData
from asn1_play.main.helper.metadata import MetaData


def process_all_data_types(data, meta_data=None, info_data=None):
    """

    :param info_data:
    :param meta_data:
    :param data:
    :return:
    """
    converter.set_defaults_for_common_objects(data)
    byte_array_format = True if data.input_format in FormatsGroup.BYTE_ARRAY_FORMATS else False
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    if info_data is None:
        info_data = InfoData()
    """
    Bulk Data Handling (Recursive; List / Tuple / Dict)
    """
    multiple_inputs = False
    dict_format = False
    if not byte_array_format and isinstance(data.input_data, list):
        # List is provided
        multiple_inputs = True
        meta_data.input_mode_key = PhKeys.INPUT_LIST
    if not byte_array_format and isinstance(data.input_data, tuple):
        # CUI (Click) Multi is a tuple
        multiple_inputs = True
        meta_data.input_mode_key = PhKeys.INPUT_TUPLE
    if isinstance(data.input_data, dict):
        multiple_inputs = True
        dict_format = True
        meta_data.input_mode_key = PhKeys.INPUT_DICT
    if multiple_inputs:
        elements_count = len(data.input_data)
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        data.set_auto_generated_remarks_if_needed()
        data.set_one_time_remarks(f'({elements_count} Elements)')
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        converter.print_data(data, meta_data)
        parsed_data_list = []
        actual_remarks_length = len(data.remarks)
        current_remarks = PhUtil.extend_list(data.remarks, expected_length=len(data.input_data))
        iterator = data.input_data
        for index, input_data_item in enumerate(iterator, start=1):
            sub_data = copy.deepcopy(data)
            if dict_format:
                sub_data.input_data = data.input_data.get(input_data_item, None)
                sub_data.set_asn1_element(Asn1(asn1_object=input_data_item))
            else:
                sub_data.input_data = input_data_item
            sub_data.reset_auto_generated_remarks()
            sub_data.set_extended_remarks_available(False if index <= actual_remarks_length else True)
            sub_data.set_user_remarks(current_remarks[index - 1])
            if elements_count > 1:
                sub_data.set_auto_generated_remarks_if_needed(
                    PhUtil.get_key_value_pair(key='item', value=index, sep=PhConstants.SEPERATOR_TWO_WORDS,
                                              dic_format=False))
            parsed_data_list.append(process_all_data_types(sub_data))
        meta_data.parsed_data = parsed_data_list
        return meta_data.parsed_data
    """
    Dir Handling (Bulk Mode)
    """
    if data.input_data and isinstance(data.input_data, str) and os.path.isdir(os.path.abspath(data.input_data)):
        # XXX: path should be string, bytes or os.PathLike; throwing error during full testing
        # directory is provided
        meta_data.input_mode_key = PhKeys.INPUT_DIR
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        # TODO: Creating problems
        # converter.set_defaults(data, meta_data)
        converter.print_data(data, meta_data)
        converter.set_includes_excludes_files(data, meta_data)
        files_list = PhUtil.traverse_it(top=os.path.abspath(data.input_data), traverse_mode='Regex',
                                        include_files=meta_data.include_files, excludes=meta_data.excludes)
        if files_list:
            files_list_data = data
            files_list_data.input_data = files_list
            return process_all_data_types(files_list_data)
    """
    Individual File Handling
    """
    file_dic_all_str = {}
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    if data.input_data and isinstance(data.input_data, str) and os.path.isfile(os.path.abspath(data.input_data)):
        # file is provided
        resp = converter.read_input_file(data=data, meta_data=meta_data, info_data=info_data)
        file_ext = PhUtil.get_file_name_and_extn(file_path=data.input_data, only_extn=True)
        if file_ext in FormatsGroup.INPUT_FILE_FORMATS_YML:
            meta_data.input_mode_key = PhKeys.INPUT_YML
            file_dic_all_str, data = converter.handle_yml_request(resp)
            converter.set_defaults_for_common_objects(data)
        else:
            meta_data.input_mode_key = PhKeys.INPUT_FILE
            converter.set_input_output_format(data)
            data.input_data = resp
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
    """
    Individual Data Handling
    """
    # Needed for a scenario when remarks will be fetched from YML
    data.set_auto_generated_remarks_if_needed()
    converter.set_defaults(data, meta_data)
    data.set_user_remarks_expand_variables()
    converter.set_output_file_path(data, meta_data)
    converter.set_re_output_file_name(data, meta_data)
    if meta_data.export_mode:
        converter.print_data(data, meta_data)
        converter.write_yml_file(meta_data.output_file_path, converter.prepare_config_data_for_yml(data))
        return None
    output_versions_dic = OrderedDict()
    version_parameters_pool = [
        {},
        {'tool_name': ConfigConst.TOOL_NAME, 'tool_version': ConfigConst.TOOL_VERSION},
        {'tool_name': PhConfigConst.TOOL_NAME, 'tool_version': PhConfigConst.TOOL_VERSION},
        {'tool_name': PhModules.PYCRATE, 'fetch_tool_version': True},
        {'tool_name': tlvConfigConst.TOOL_NAME, 'tool_version': tlvConfigConst.TOOL_VERSION},
        {'tool_name': PhKeys.SGP22, 'tool_version': sgp_22_version},
        {'tool_name': PhKeys.SGP32, 'tool_version': sgp_32_version},
        {'tool_name': PhKeys.EUICC_PROFILE_PACKAGE, 'tool_version': epp_version},
    ]
    versions_data = PhUtil.print_version(parameters_pool=version_parameters_pool, get_only=True, dic_format=True)
    output_versions_dic = PhUtil.dict_update(output_versions_dic, versions_data)
    output_versions_dic.update(
        PhUtil.get_key_value_pair(PhKeys.TIME_STAMP, PhUtil.get_time_stamp(files_format=False), dic_format=True))
    """
    Data Processing
    """
    handle_data(data=data, meta_data=meta_data, info_data=info_data)
    """
    Output Handling
    """
    if meta_data.parsed_data and data.tlv_parsing_of_output is True:
        data_type_tlv = DataTypeMaster()
        data_type_tlv.set_data_pool(data_pool=Data(input_data=meta_data.parsed_data, quite_mode=True))
        data_type_tlv.process_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
        meta_data.parsed_data_tlv = data_type_tlv.get_output_data()
        if meta_data.parsed_data_tlv and PhConstants.EXCEPTION_OCCURRED not in meta_data.parsed_data_tlv:
            meta_data.parsed_data = meta_data.parsed_data_tlv
    if data.re_parse_output:
        handle_data(data=data, meta_data=meta_data, info_data=info_data, flip_output=True)
    converter.print_data(data=data, meta_data=meta_data, info_data=info_data)
    if meta_data.input_mode_key == PhKeys.INPUT_YML:
        converter.write_yml_file(meta_data.output_file_path, file_dic_all_str, meta_data.output_dic,
                                 output_versions_dic)
    elif meta_data.output_file_path:
        PhUtil.make_dirs(file_path=meta_data.output_file_path)
        converter.write_output_file(data=data, meta_data=meta_data, info_data=info_data)
        if meta_data.re_parsed_data:
            converter.write_output_file(data=data, meta_data=meta_data, info_data=info_data, flip_output=True)
    return meta_data.parsed_data
