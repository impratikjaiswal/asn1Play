import os


class Constants:
    # Verified
    UNKNOWN_INPUT_DATA = 'Unknown Input Data'
    UNKNOWN_INPUT_FORMAT = 'Unknown Input Format'
    UNKNOWN_OUTPUT_FORMAT = 'Unknown Output Format'
    UNKNOWN_ASN1_SCHEMA = 'Unknown Asn1 Schema'
    UNKNOWN_ASN1_OBJECT = 'Unknown Asn1 Object'
    #
    INPUT_FILE_EMPTY = 'Input File Is empty.'
    ASN1_OBJECT_IS_EMPTY_OR_MISSING = 'Asn1 Object is either empty or not provided.'
    ASN1_SCHEMA_IS_EMPTY_OR_MISSING = 'Asn1 Schema is either empty or not provided.'
    # Not Verified
    INPUT_DATA_ASN1_FORMATION_ISSUE = 'input data is not a valid ASN'
    UNKNOWN_PARENT_OF_ASN1_OBJECT = 'asn1_element must be child of Asn1'
    ASN1_ELEMENT_MAPPING_IS_DONE = 'asn1_element mapping conversion is done'
    ASN1_ELEMENT_MAPPING_IS_FAIL = 'asn1_element mapping conversion is fail'
    INPUT_DATA_CONVERSION_NOT_POSSIBLE = 'input data conversion is not possible'
    INPUT_DATA_HEX_CONVERSION_IS_DONE = 'input data hex conversion is done'
    INPUT_DATA_BASE_64_CONVERSION_IS_DONE = 'input data base64 conversion is done'
    ASN1_ELEMENT_IS_NOT_NEEDED = 'asn1_element is not needed; Conversion can be performed'
    INPUT_DATA_TRIMMING_IS_DONE = 'input data trimming is done'
    INPUT_DATA_MISSING = 'Mandatory input data is missing.'
    CONFIG_INPUT_MISSING = 'Mandatory Config "input" is missing.'
    STR_CONVERSION_MODE = 'Conversion'
    STR_ENCODING_MODE = 'Encoding'
    STR_DECODING_MODE = 'Decoding'
    STR_YML_MODE = 'Yml'
    STR_LIST = 'List'
    STR_DIR = 'Dir'
    STR_DIR_LIST = 'Dir_List'
    STR_MODE = 'Mode'
    STR_FORMATTING = 'Formatting'
    DEFAULT_OUTPUT_FOLDER = os.sep.join([os.pardir, os.pardir, 'Data', 'UserData'])
