import copy
import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import PreservedScalarString

from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.TCA import eUICC_Profile_Package
from src.main.helper.constants import Constants as Constants_local
from src.main.helper.data import Data
from src.main.helper.defaults import Defaults
from src.main.helper.file_extensions import FileExtensions
from src.main.helper.formats import Formats
from src.main.helper.formats_group import FormatsGroup
from src.main.helper.keys import Keys
from src.main.helper.keywords import KeyWords
from src.main.helper.mode_operation import OperationModes


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    if value is not None and '\n' in value:
        value = PreservedScalarString(value)
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def print_data(data, meta_data):
    input_sep = PhConstants.SEPERATOR_MULTI_LINE if data.input_format in FormatsGroup.TXT_FORMATS else PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE if data.output_format in FormatsGroup.TXT_FORMATS else PhConstants.SEPERATOR_ONE_LINE
    if data.print_info:
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(Keys.ASN1_ELEMENT, PhConstants.SEPERATOR_ONE_LINE, data.get_asn1_element_name(),
                                   dic_format=False,
                                   print_also=False) if data.get_asn1_element_name() else Constants_local.STR_CONVERSION_MODE,
            get_dic_data_and_print(Keys.INPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.input_format,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(Keys.OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.output_format,
                                   dic_format=False, print_also=False),
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(Keys.INFO, PhConstants.SEPERATOR_INFO, info))
        if meta_data.input_mode_key:
            meta_data.output_dic.update(get_dic_data_and_print(meta_data.input_mode_key, PhConstants.SEPERATOR_ONE_LINE,
                                                               meta_data.input_mode_value))
            if len(data.get_input_modes_hierarchy()) > 1:
                meta_data.output_dic.update(
                    get_dic_data_and_print(Keys.INPUT_MODES_HIERARCHY, PhConstants.SEPERATOR_ONE_LINE,
                                           data.get_input_modes_hierarchy_as_str()))
        if meta_data.export_mode or (meta_data.parsed_data and meta_data.output_file_name) :
            meta_data.output_dic.update(
                get_dic_data_and_print(Keys.EXPORT_FILE if meta_data.export_mode else Keys.OUTPUT_FILE,
                                       PhConstants.SEPERATOR_ONE_LINE, meta_data.output_file_name))
        if meta_data.re_parsed_data and meta_data.re_output_file_name:
            meta_data.output_dic.update(get_dic_data_and_print(Keys.RE_OUTPUT_FILE, PhConstants.SEPERATOR_ONE_LINE,
                                                               meta_data.re_output_file_name))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(Keys.INPUT_DATA, input_sep, data.raw_data))
    if data.print_output and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(Keys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    if data.print_output and meta_data.re_parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(Keys.RE_PARSED_DATA, input_sep, meta_data.re_parsed_data))
    PhUtil.print_separator()


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
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


def prepare_config_data(data, existing_file_dic):
    data_dic = dict()
    if existing_file_dic:
        config_data = dict(existing_file_dic).get(Keys.INPUT, None)
    else:
        config_data = data.__dict__
    for k, v in config_data.items():
        if not v:
            continue
        if k in [Keys.OUTPUT_FILE_NAME_KEYWORD]:
            # Here we need to be ready for further usage of exported file
            data_dic[k] = KeyWords.OUTPUT_FILE_NAME_KEYWORD
            continue
        data_dic[k] = v
    file_dic = dict()
    file_dic[Keys.INPUT] = data_dic
    return file_dic


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
            if temp[0] == KeyWords.CLASS_SGP22:
                config_data[k] = getattr(SGP_22.RSPDefinitions, value)
            if temp[0] == KeyWords.CLASS_EPP:
                config_data[k] = getattr(eUICC_Profile_Package.PEDefinitions, value)
        if k in [Keys.INPUT_FORMAT, Keys.OUTPUT_FORMAT, Keys.OUTPUT_FILE_NAME_KEYWORD]:
            temp = str(v).split('.')
            value = temp[-1]
            if temp[0] == KeyWords.CLASS_FORMATS:
                config_data[k] = getattr(Formats, value)
            if temp[0] == KeyWords.CLASS_KEYWORDS:
                config_data[k] = getattr(KeyWords, value)
    return config_data


def set_input_output_format(data):
    """

    :param data:
    :return:
    """
    input_format_temp = None
    output_format_temp = None
    file_ext = PhUtil.get_file_name_and_extn(file_path=data.raw_data, only_extn=True)
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


def set_defaults_for_printing(data):
    if data.print_input is None: data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None: data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None: data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.input_format is None: data.input_format = Defaults.FORMAT_INPUT
    if data.output_format is None: data.output_format = Defaults.FORMAT_OUTPUT
    if data.re_parse_output is None: data.re_parse_output = Defaults.RE_PARSE_OUTPUT
    data.set_asn1_element_name()
    if data.asn1_element:
        meta_data.operation_mode = OperationModes.ENCODE_DECODE
    else:
        meta_data.operation_mode = OperationModes.CONVERSION
    default_output_file_mapping = {
        Formats.ASN1: FileExtensions.ASN1,
        Formats.DER: FileExtensions.HEX,
        Formats.DER_64: FileExtensions.BASE_64,
        Formats.JSON: FileExtensions.JSON,
        Formats.YML: FileExtensions.YML,
    }
    meta_data.export_mode = True if data.output_file_name_keyword == KeyWords.EXPORT_FILE_NAME_KEYWORD else False
    meta_data.default_output_file_ext = default_output_file_mapping.get(
        Formats.YML if meta_data.export_mode else data.output_format, FileExtensions.TXT)


def read_yaml(input_file):
    yaml_object = YAML()
    file_dic = yaml_object.load(input_file)
    config_data = validate_config_data(copy.deepcopy(file_dic))
    return file_dic, Data(**config_data)


def write_yml_file(output_file_name, file_dic, output_dic=None, output_versions_dic=None, time_stamp=True):
    with open(output_file_name, 'w') as file:
        if output_dic:
            file_dic[Keys.OUTPUT] = dict(output_dic)
        if output_versions_dic:
            file_dic[Keys.OUTPUT_VERSION] = dict(output_versions_dic)
        if time_stamp:
            file_dic[Keys.TIME_STAMP] = PhUtil.get_time_stamp(files_format=False, default_format=True)
        yaml_object = YAML()
        yaml_object.width = 1000
        yaml_object.indent(mapping=4)
        yaml_object.dump(file_dic, file)


def set_output_file_name(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    file_mode = False
    if not (meta_data.input_mode_key == Keys.INPUT_YML or data.output_file or data.output_file_name_keyword):
        return
    if data.output_file:
        meta_data.output_file_name = data.output_file
    if meta_data.input_mode_key == Keys.INPUT_YML or meta_data.input_mode_key == Keys.INPUT_FILE:
        # YML File writing is mandatory, But Output File is not Provided, so Dest File will be source File only
        # File writing is needed, But OutputFile is not Provided,so Dest FileName will be prepared from source file name
        file_mode = True
        if not meta_data.output_file_name:
            meta_data.output_file_name = meta_data.raw_data_org
    name_as_per_remarks = data.get_remarks_as_str().replace(PhConstants.SEPERATOR_MULTI_OBJ, '_').replace(
        Constants_local.DEFAULT_TRIM_STRING, '')
    name_as_per_remarks = PhUtil.get_python_friendly_name(name_as_per_remarks)
    if not meta_data.output_file_name or (data.validate_if_input_modes_hierarchy(Keys.INPUT_LIST) and not file_mode):
        # output_file_name is not decided yet, so need to prepare
        output_folder = Constants_local.DEFAULT_OUTPUT_FOLDER
        sample_file_name = meta_data.default_output_file_ext
        if meta_data.output_file_name:
            sample_file_ext = PhUtil.get_file_name_and_extn(meta_data.output_file_name, only_extn=True)
            if sample_file_ext:
                # Target File Provided
                output_folder = PhUtil.get_file_name_and_extn(meta_data.output_file_name, only_path=True)
                sample_file_name = PhUtil.get_file_name_and_extn(meta_data.output_file_name)
            else:
                # Target Directory File Provided
                output_folder = meta_data.output_file_name
        # Direct Data is provided, Name Needs to be set
        meta_data.output_file_name = os.sep.join(
            [output_folder, PhUtil.append_in_file_name(str_file_path=sample_file_name, str_append=name_as_per_remarks)])
    if data.output_file_name_keyword:
        meta_data.output_file_name = PhUtil.append_in_file_name(str_file_path=meta_data.output_file_name,
                                                                str_append=data.output_file_name_keyword,
                                                                new_ext=None if meta_data.input_mode_key == Keys.INPUT_YML else meta_data.default_output_file_ext)


def set_re_output_file_name(data, meta_data):
    if meta_data.output_file_name and data.re_parse_output:
        meta_data.re_output_file_name = PhUtil.append_in_file_name(str_file_path=meta_data.output_file_name,
                                                                   str_append='re_parsed')
    return


def write_output_file(output_file_name, parsed_data):
    with open(output_file_name, 'w') as file:
        file.writelines(parsed_data)
