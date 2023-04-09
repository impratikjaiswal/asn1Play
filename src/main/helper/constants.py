import os


class Constants:
    STR_CONVERSION_MODE = 'Conversion Mode'
    DEFAULT_OUTPUT_FOLDER = os.sep.join([os.pardir, os.pardir, 'UserData'])
    MAX_HEADING_LENGTH= 100
    DEFAULT_REMARKS_MAX_LENGTH= 94
    DEFAULT_TRIM_STRING = '...'
    DEFAULT_TRIM_STRING_LENGTH = len(DEFAULT_TRIM_STRING)
