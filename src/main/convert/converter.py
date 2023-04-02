import copy
import os

import yaml
from util_helpers import util
from util_helpers.constants_config import ConfigConst as util_ConfigConst
from util_helpers.util import get_tool_name_w_version

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.convert.handler import decode_encode_asn
from src.main.helper.constants_config import ConfigConst
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults
from src.main.helper.formats import Formats
from src.main.helper.formatsGroup import FormatsGroup
from src.main.helper.keys import Keys
from src.main.helper.modes import Modes


def print_data(base_data, input_format, output_format, print_input, print_info, re_parse_output,
               asn1_element, parsed_data, re_parsed_data, mode_key, mode_key_additional_data, mode_value):
    output_dic = {}
    one_line_sep = ': '
    multi_line_sep = ':\n'
    multi_obj_sep = '; '
    mode_key = ' '.join(filter(None, [mode_key, mode_key_additional_data]))
    input_sep = multi_line_sep if input_format in FormatsGroup.TXT_FORMATS else one_line_sep
    output_sep = multi_line_sep if output_format in FormatsGroup.TXT_FORMATS else one_line_sep
    if print_info:
        info = multi_obj_sep.join(filter(None, [
            f'Asn1 Element is{one_line_sep}{asn1_element.fullname()}' if asn1_element else 'Conversion Mode',
            f'Input Format is{one_line_sep}{input_format}',
            f'Output Format is{one_line_sep}{output_format}',
        ]))
        info_additional = f'Input {mode_key} is{one_line_sep}{mode_value}' if mode_key else None
        print(info)
        output_dic.update({'info': info})
        if info_additional:
            print(info_additional)
            output_dic.update({'info_additional': info_additional})
    if print_input:
        print(f'Input Data is{input_sep}{base_data}')
        output_dic.update({'input_data': base_data})
    if parsed_data:
        print(f'OutPut Data is{output_sep}{parsed_data}')
        output_dic.update({'output_data': parsed_data})
    if re_parse_output:
        print(f'Re-parsed Data is{input_sep}{re_parsed_data}')
        output_dic.update({'re_parsed_data': re_parsed_data})
    util.print_separator()
    return output_dic


def files_ext_as_per_input_format(input_format):
    if input_format in FormatsGroup.INPUT_FORMATS_DER:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_HEX
    elif input_format in FormatsGroup.INPUT_FORMATS_DER_BASE_64:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_BASE_64
    elif input_format in FormatsGroup.INPUT_FORMATS_ASN:
        include_files = FormatsGroup.INPUT_FILE_FORMATS_ASN
    else:  # input_format is None or unknown
        include_files = FormatsGroup.INPUT_FILE_FORMATS
    include_files = [('*' + x) for x in include_files]
    return include_files


def validate_config_data(config_data):
    config_data = dict(config_data).get(Keys.INPUT, None)
    if not config_data:
        raise ValueError(f'Mandatory Config "input" is missing.')
    for k, v in config_data.items():
        if v is not None and v in ['None']:
            config_data[k] = None
        if k in [Keys.INPUT_FORMAT, Keys.OUTPUT_FORMAT]:
            temp = str(v).split('.')
            if temp[0] == 'Formats':
                config_data[k] = getattr(Formats, temp[1])
    return config_data


def config_as_per_files_ext(input_file):
    file_dic = yaml.safe_load(input_file)
    config_data = validate_config_data(copy.deepcopy(file_dic))
    return file_dic, Data(**config_data)


def input_output_format_as_per_files_ext(input_file, input_format, output_format):
    file_ext = util.get_file_name_and_extn(file_path=input_file, only_extn=True)
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_HEX:
        input_format = Formats.DER
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_BASE_64:
        input_format = Formats.DER_64
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_ASN:
        input_format = Formats.ASN1
        output_format_temp = Formats.DER
    if output_format is None or output_format == input_format:
        output_format = output_format_temp
    return input_format, output_format


def set_defaults(input_format, output_format, print_input, print_info, re_parse_output):
    # Set Default Values if nothing is set
    if input_format is None: input_format = Defaults.FORMAT_INPUT
    if output_format is None: output_format = Defaults.FORMAT_OUTPUT
    if print_input is None: print_input = Defaults.PRINT_INPUT
    if print_info is None: print_info = Defaults.PRINT_INFO
    if re_parse_output is None: re_parse_output = Defaults.RE_PARSE_OUTPUT
    return input_format, output_format, print_input, print_info, re_parse_output


def parse_or_update_any_data(base_data, input_format=None, output_format=None, print_input=None, print_info=None,
                             re_parse_output=None, asn1_element=None):
    mode_key = None
    mode_key_additional_data = None
    base_data_org = base_data
    input_format, output_format, print_input, print_info, re_parse_output = set_defaults(input_format=input_format,
                                                                                         output_format=output_format,
                                                                                         print_input=print_input,
                                                                                         print_info=print_info,
                                                                                         re_parse_output=re_parse_output)
    if isinstance(base_data, list):
        mode_key = Modes.LIST
        mode_key_additional_data = f'({len(base_data)} Elements)'
        print_data(base_data=base_data, input_format=input_format, output_format=output_format, print_input=print_input,
                   print_info=print_info, re_parse_output=re_parse_output, asn1_element=asn1_element, parsed_data=None,
                   re_parsed_data=None, mode_key=mode_key, mode_key_additional_data=mode_key_additional_data,
                   mode_value=base_data_org)
        parsed_data_list = []
        for data in base_data:
            parsed_data_list.append(
                parse_or_update_any_data(base_data=data, input_format=input_format, output_format=output_format,
                                         print_input=print_input, print_info=print_info,
                                         re_parse_output=re_parse_output,
                                         asn1_element=asn1_element))
        return parsed_data_list
    if base_data and os.path.isdir(os.path.abspath(base_data)):
        # directory is provided
        mode_key = Modes.DIRECTORY
        print_data(base_data=base_data, input_format=input_format, output_format=output_format, print_input=print_input,
                   print_info=print_info, re_parse_output=re_parse_output, asn1_element=asn1_element, parsed_data=None,
                   re_parsed_data=None, mode_key=mode_key, mode_key_additional_data=mode_key_additional_data,
                   mode_value=base_data_org)
        files_list = util.traverse_it(top=os.path.abspath(base_data), traverse_mode='Regex',
                                      include_files=files_ext_as_per_input_format(input_format))
        if files_list:
            return parse_or_update_any_data(base_data=files_list, input_format=input_format,
                                            output_format=output_format,
                                            print_input=print_input, print_info=print_info,
                                            re_parse_output=re_parse_output,
                                            asn1_element=asn1_element)
    if base_data and os.path.isfile(base_data):
        # file is provided
        try:
            with open(base_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(base_data, 'rb') as the_file:
                resp = the_file.read()
        file_ext = util.get_file_name_and_extn(file_path=base_data, only_extn=True)
        if file_ext in FormatsGroup.INPUT_FILE_FORMATS_YML:
            mode_key = Modes.YML
            file_dic, data = config_as_per_files_ext(resp)
            #
            base_data = data.raw_data
            input_format = data.input_format
            output_format = data.output_format
            print_input = data.print_input
            print_info = data.print_info
            re_parse_output = data.re_parse_output
            asn1_element = data.asn1_element
            input_format, output_format, print_input, print_info, re_parse_output = set_defaults(
                input_format=input_format,
                output_format=output_format,
                print_input=print_input,
                print_info=print_info,
                re_parse_output=re_parse_output)
        else:
            mode_key = Modes.FILE
            input_format, output_format = input_output_format_as_per_files_ext(base_data, input_format, output_format)
            base_data = resp

    output_versions_dic = {}
    output_versions_dic.update(get_tool_name_w_version(dic_format=True))
    output_versions_dic.update(
        get_tool_name_w_version(util_ConfigConst.TOOL_NAME, util_ConfigConst.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(
        get_tool_name_w_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(get_tool_name_w_version(ConfigConst.ASN_SGP_22_NAME, sgp_22_version, dic_format=True))
    output_versions_dic.update(get_tool_name_w_version(ConfigConst.ASN_EPP_NAME, epp_version, dic_format=True))
    re_parsed_data = None
    # parse Data
    parsed_data = decode_encode_asn(input_data=base_data, parse_only=True,
                                    input_format=input_format, output_format=output_format,
                                    asn1_element=asn1_element)
    if re_parse_output:
        re_parsed_data = decode_encode_asn(input_data=parsed_data, parse_only=True,
                                           input_format=output_format, output_format=input_format,
                                           asn1_element=asn1_element)
    output_dic = print_data(base_data=base_data, input_format=input_format, output_format=output_format,
                            print_input=print_input, print_info=print_info, re_parse_output=re_parse_output,
                            asn1_element=asn1_element, parsed_data=parsed_data, re_parsed_data=re_parsed_data,
                            mode_key=mode_key, mode_key_additional_data=mode_key_additional_data,
                            mode_value=base_data_org)
    if mode_key == Modes.YML:
        output_file = file_dic.get(Keys.INPUT).get(Keys.OUTPUT_FILE, None)
        file_name = util.append_in_file_name(str_file_path=base_data_org,
                                             str_append=output_file) if output_file else base_data_org
        with open(file_name, 'w') as file:
            file_dic['output'] = output_dic
            file_dic['output_version'] = output_versions_dic
            file_dic['time_stamp'] = util.get_time_stamp(files_format=False, default_format=True)
            yaml.dump(file_dic, file)
    return parsed_data
