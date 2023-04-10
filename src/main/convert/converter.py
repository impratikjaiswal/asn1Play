import copy
import os
from collections import OrderedDict

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import PreservedScalarString
from util_helpers import util
from util_helpers.constants import Constants
from util_helpers.constants_config import ConfigConst

from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA import eUICC_Profile_Package
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.convert.handler import decode_encode_asn
from src.main.helper.constants import Constants as Constants_local
from src.main.helper.constants_config import ConfigConst as ConfigConst_local
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults
from src.main.helper.file_extensions import FileExtensions
from src.main.helper.formats import Formats
from src.main.helper.formats_group import FormatsGroup
from src.main.helper.keys import Keys
from src.main.helper.metadata import MetaData
from src.main.helper.mode_operation import OperationModes


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    if value is not None and '\n' in value:
        value = PreservedScalarString(value)
    return util.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def print_data(data, meta_data):
    output_dic = OrderedDict()
    input_sep = Constants.SEPERATOR_MULTI_LINE if data.input_format in FormatsGroup.TXT_FORMATS else Constants.SEPERATOR_ONE_LINE
    output_sep = Constants.SEPERATOR_MULTI_LINE if data.output_format in FormatsGroup.TXT_FORMATS else Constants.SEPERATOR_ONE_LINE
    if data.print_info:
        info = Constants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(Keys.ASN1_ELEMENT, Constants.SEPERATOR_ONE_LINE, meta_data.asn1_element_name,
                                   dic_format=False,
                                   print_also=False) if meta_data.asn1_element_name else Constants_local.STR_CONVERSION_MODE,
            get_dic_data_and_print(Keys.INPUT_FORMAT, Constants.SEPERATOR_ONE_LINE, data.input_format,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(Keys.OUTPUT_FORMAT, Constants.SEPERATOR_ONE_LINE, data.output_format,
                                   dic_format=False, print_also=False),
        ]))
        output_dic.update(get_dic_data_and_print(Keys.INFO, Constants.SEPERATOR_INFO, info))
        if meta_data.input_mode_key:
            output_dic.update(get_dic_data_and_print(meta_data.input_mode_key, Constants.SEPERATOR_ONE_LINE,
                                                     meta_data.input_mode_value))
        if meta_data.output_file_name:
            output_dic.update(
                get_dic_data_and_print(Keys.OUTPUT_FILE, Constants.SEPERATOR_ONE_LINE, meta_data.output_file_name))
        if data.re_parse_output and meta_data.re_output_file_name:
            output_dic.update(get_dic_data_and_print(Keys.RE_OUTPUT_FILE, Constants.SEPERATOR_ONE_LINE,
                                                     meta_data.re_output_file_name))
    if data.print_input:
        output_dic.update(get_dic_data_and_print(Keys.INPUT_DATA, input_sep, data.raw_data))
    if meta_data.parsed_data:
        output_dic.update(get_dic_data_and_print(Keys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    if data.re_parse_output:
        output_dic.update(get_dic_data_and_print(Keys.RE_PARSED_DATA, input_sep, meta_data.re_parsed_data))
    util.print_separator()
    return output_dic


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + Constants_local.DEFAULT_OUTPUT_FILE_NAME_KEYWORD + '.*']
    if data.input_format in FormatsGroup.INPUT_FORMATS_DER:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_HEX
    elif data.input_format in FormatsGroup.INPUT_FORMATS_DER_BASE_64:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_BASE_64
    elif data.input_format in FormatsGroup.INPUT_FORMATS_ASN:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_ASN
    elif data.input_format in FormatsGroup.INPUT_FORMATS_YML:
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS_YML
    else:  # input_format is None or unknown
        meta_data.include_files = FormatsGroup.INPUT_FILE_FORMATS
    meta_data.include_files = [('*' + x) for x in meta_data.include_files]


def validate_config_data(config_data):
    config_data = dict(config_data).get(Keys.INPUT, None)
    if not config_data:
        raise ValueError(f'Mandatory Config "input" is missing.')
    for k, v in config_data.items():
        if v is not None and v in ['None']:
            config_data[k] = None
        if k in [Keys.ASN1_ELEMENT]:
            temp = str(v).split('.')
            value = temp[-1]
            if temp[0] == 'SGP_22':
                config_data[k] = getattr(SGP_22.RSPDefinitions, value)
            if temp[0] == 'eUICC_Profile_Package':
                config_data[k] = getattr(eUICC_Profile_Package.PEDefinitions, value)
        if k in [Keys.INPUT_FORMAT, Keys.OUTPUT_FORMAT]:
            temp = str(v).split('.')
            value = temp[-1]
            if temp[0] == 'Formats':
                config_data[k] = getattr(Formats, value)
    return config_data


def set_input_output_format(data):
    """

    :param data:
    :return:
    """
    input_format_temp = None
    output_format_temp = None
    file_ext = util.get_file_name_and_extn(file_path=data.raw_data, only_extn=True)
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_HEX:
        input_format_temp = Formats.DER
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_BASE_64:
        input_format_temp = Formats.DER_64
        output_format_temp = Formats.ASN1
    if file_ext in FormatsGroup.INPUT_FILE_FORMATS_ASN:
        input_format_temp = Formats.ASN1
        output_format_temp = Formats.DER
    if data.output_format is None or not data.output_format:
        data.output_format = output_format_temp
    if data.input_format is None or not data.input_format:
        data.input_format = input_format_temp


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.input_format is None: data.input_format = Defaults.FORMAT_INPUT
    if data.output_format is None: data.output_format = Defaults.FORMAT_OUTPUT
    if data.print_input is None: data.print_input = Defaults.PRINT_INPUT
    if data.print_info is None: data.print_info = Defaults.PRINT_INFO
    if data.re_parse_output is None: data.re_parse_output = Defaults.RE_PARSE_OUTPUT
    if data.asn1_element:
        meta_data.operation_mode = OperationModes.ENCODE_DECODE
        meta_data.set_asn1_element_name(data.asn1_element)
    else:
        meta_data.operation_mode = OperationModes.CONVERSION
    default_output_file_mapping = {
        Formats.ASN1: FileExtensions.ASN1,
        Formats.DER: FileExtensions.HEX,
        Formats.DER_64: FileExtensions.BASE_64,
        Formats.JSON: FileExtensions.JSON,
        Formats.YML: FileExtensions.YML,
    }
    meta_data.default_output_file_ext = default_output_file_mapping.get(data.output_format, FileExtensions.TXT)


def read_yaml(input_file):
    yaml_object = YAML()
    file_dic = yaml_object.load(input_file)
    config_data = validate_config_data(copy.deepcopy(file_dic))
    return file_dic, Data(**config_data)


def write_yml_file(output_file_name, file_dic, output_dic, output_versions_dic):
    with open(output_file_name, 'w') as file:
        file_dic[Keys.OUTPUT] = dict(output_dic)
        file_dic[Keys.OUTPUT_VERSION] = dict(output_versions_dic)
        file_dic[Keys.TIME_STAMP] = util.get_time_stamp(files_format=False, default_format=True)
        yaml_object = YAML()
        yaml_object.width = 1000
        yaml_object.indent(mapping=4)
        yaml_object.dump(file_dic, file)


def set_output_file_name(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    file_name_keyword_needed = False
    if not (meta_data.input_mode_key == Keys.INPUT_YML or data.output_file or data.output_file_name_keyword):
        return
    if data.output_file:
        meta_data.output_file_name = data.output_file
    if meta_data.input_mode_key == Keys.INPUT_YML or meta_data.input_mode_key == Keys.INPUT_FILE:
        # YML File writing is mandatory, But Output File is not Provided, so Dest File will be source File only
        # File writing is needed, But OutputFile is not Provided,so Dest FileName will be prepared from source file name
        if not meta_data.output_file_name:
            meta_data.output_file_name = meta_data.raw_data_org
            file_name_keyword_needed = True if meta_data.input_mode_key == Keys.INPUT_FILE else file_name_keyword_needed
    if not meta_data.output_file_name:
        # output_file_name is not decided yet, so need to prepare
        # Direct Data is provided, Name Needs to be set
        initial_name = Constants.SEPERATOR_TWO_WORDS.join(filter(None, [
            # Append ASN name always if available
            meta_data.asn1_element_name,
            data.get_remarks_as_str(),
        ]))
        initial_name = initial_name.replace(Constants.SEPERATOR_MULTI_OBJ, '_')
        initial_name = initial_name.replace(Constants_local.DEFAULT_TRIM_STRING, '')
        initial_name = util.get_python_friendly_name(initial_name)
        meta_data.output_file_name = os.sep.join([Constants_local.DEFAULT_OUTPUT_FOLDER,
                                                  util.append_in_file_name(
                                                      str_file_path=meta_data.default_output_file_ext,
                                                      str_append=initial_name)])
    if not data.output_file_name_keyword:
        # output_file_name_keyword is not there, so need to prepare
        pass
    if data.output_file_name_keyword:
        meta_data.output_file_name = util.append_in_file_name(str_file_path=meta_data.output_file_name,
                                                              str_append=data.output_file_name_keyword,
                                                              new_ext=None if meta_data.input_mode_key == Keys.INPUT_YML else meta_data.default_output_file_ext)

    if meta_data.input_mode_key == Keys.INPUT_DIR:
        # Nothing to Do, One file at a time will be provided
        return
    if meta_data.input_mode_key == Keys.INPUT_LIST:
        # Nothing to Do, One data at a time will be provided
        return


def set_re_output_file_name(data, meta_data):
    if meta_data.output_file_name and data.re_parse_output:
        meta_data.re_output_file_name = util.append_in_file_name(str_file_path=meta_data.output_file_name,
                                                                 str_append='re_parsed')
    return


def write_output_file(output_file_name, parsed_data):
    with open(output_file_name, 'w') as file:
        file.writelines(parsed_data)


def parse_or_update_any_data(data):
    """

    :param data:
    :return:
    """
    """
    Pool
    """
    meta_data = MetaData(raw_data_org=data.raw_data, asn1_element=data.asn1_element)
    if isinstance(data.raw_data, list):
        # List is provided
        meta_data.input_mode_key = Keys.INPUT_LIST
        data.set_default_internal_remarks_if_not_set(f'({len(data.raw_data)} Elements)')
        util.print_heading(data.get_remarks_as_str(), heading_level=3, count=Constants_local.MAX_HEADING_LENGTH)
        print_data(data, meta_data)
        parsed_data_list = []
        for index, raw_data_item in enumerate(data.raw_data, start=1):
            sub_data = copy.deepcopy(data)
            sub_data.raw_data = raw_data_item
            sub_data.set_default_remarks_if_not_set()
            sub_data.internal_remarks = util.get_key_value_pair(key='item', value=index,
                                                                sep=Constants.SEPERATOR_TWO_WORDS,
                                                                dic_format=False)
            parsed_data_list.append(parse_or_update_any_data(sub_data))
        return parsed_data_list
    if data.raw_data and os.path.isdir(os.path.abspath(data.raw_data)):
        # directory is provided
        util.print_heading(data.get_remarks_as_str(), heading_level=3, count=Constants_local.MAX_HEADING_LENGTH)
        meta_data.input_mode_key = Keys.INPUT_DIR
        print_data(data, meta_data)
        set_includes_excludes_files(data, meta_data)
        files_list = util.traverse_it(top=os.path.abspath(data.raw_data), traverse_mode='Regex',
                                      include_files=meta_data.include_files, excludes=meta_data.excludes)
        if files_list:
            files_list_data = data
            files_list_data.raw_data = files_list
            return parse_or_update_any_data(files_list_data)
    """
    Individual
    """
    data.set_default_remarks_if_not_set()
    util.print_heading(data.get_remarks_as_str(), heading_level=2, count=Constants_local.MAX_HEADING_LENGTH)
    if data.raw_data and os.path.isfile(data.raw_data):
        # file is provided
        try:
            with open(data.raw_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(data.raw_data, 'rb') as the_file:
                resp = the_file.read()
        file_ext = util.get_file_name_and_extn(file_path=data.raw_data, only_extn=True)
        if file_ext in FormatsGroup.INPUT_FILE_FORMATS_YML:
            meta_data.input_mode_key = Keys.INPUT_YML
            file_dic, data = read_yaml(resp)
        else:
            meta_data.input_mode_key = Keys.INPUT_FILE
            set_input_output_format(data)
            data.raw_data = resp

    set_defaults(data, meta_data)
    output_versions_dic = OrderedDict()
    output_versions_dic.update(util.get_tool_name_w_version(dic_format=True))
    output_versions_dic.update(
        util.get_tool_name_w_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(
        util.get_tool_name_w_version(ConfigConst_local.TOOL_NAME, ConfigConst_local.TOOL_VERSION, dic_format=True))
    output_versions_dic.update(util.get_tool_name_w_version(Keys.SGP22, sgp_22_version, dic_format=True))
    output_versions_dic.update(util.get_tool_name_w_version(Keys.EUICC_PROFILE_PACKAGE, epp_version, dic_format=True))
    # parse Data
    meta_data.parsed_data = decode_encode_asn(input_data=data.raw_data, parse_only=True, input_format=data.input_format,
                                              output_format=data.output_format, asn1_element=data.asn1_element)
    if data.re_parse_output:
        meta_data.re_parsed_data = decode_encode_asn(input_data=meta_data.parsed_data, parse_only=True,
                                                     input_format=data.output_format,
                                                     output_format=data.input_format, asn1_element=data.asn1_element)
    set_output_file_name(data, meta_data)
    set_re_output_file_name(data, meta_data)
    output_dic = print_data(data, meta_data)
    if meta_data.input_mode_key == Keys.INPUT_YML:
        write_yml_file(meta_data.output_file_name, file_dic, output_dic, output_versions_dic)
    elif meta_data.output_file_name:
        util.makedirs(util.get_file_name_and_extn(file_path=meta_data.output_file_name, only_path=True))
        write_output_file(meta_data.output_file_name, meta_data.parsed_data)
        if meta_data.re_parsed_data:
            write_output_file(meta_data.re_output_file_name, meta_data.re_parsed_data)
    return meta_data.parsed_data
