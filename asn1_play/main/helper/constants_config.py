from asn1_play import _defaults
from asn1_play._tool_name import TOOL_NAME, TOOL_TITLE, TOOL_SW_PACKAGE_NAME, TOOL_TEST_PACKAGE_NAME, TOOL_SW_MODULE_NAME

_run_time_incremental = False
_run_time_play_helpers = False
try:
    from asn1_play._version import __version__

    # incremental module is available post installation, run time only,
    _run_time_incremental = True
except ImportError:
    pass
try:
    from play_helpers.ph_defaults import PhDefaults
    from tlv_play._git_info import GIT_SUMMARY

    # play_helpers module is available post installation, run time only,
    _run_time_play_helpers = True
except ImportError:
    pass


class ConfigConst:
    TOOL_VERSION = __version__.public() if _run_time_incremental else (
        PhDefaults.VERSION if _run_time_play_helpers else _defaults.VERSION)
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = TOOL_TITLE
    TOOL_SW_PACKAGE_NAME = TOOL_SW_PACKAGE_NAME
    TOOL_TEST_PACKAGE_NAME = TOOL_TEST_PACKAGE_NAME
    TOOL_SW_MODULE_NAME = TOOL_SW_MODULE_NAME
    TOOL_GIT_SUMMARY = GIT_SUMMARY if _run_time_play_helpers else _defaults.GIT_SUMMARY
    TOOL_DESCRIPTION = f'ASN.1 Encoder, Decoder & validator. Supports various versions of GSMA SGP.22, GSMA SGP.32, TCA eUICC Profile Package (SAIP) specifications along with their inherited specs.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION} Supports large variety of encoding-decoding rules (DER, JER, JSON, BER, CER, APER, COER, OER, UPER etc).'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, ASN.1, ASN1, ASN, ASN 1, ASN1 der, Abstract Syntax Notation One, GSMA, TCA, SGP22, SGP.22, SGP32, SGP.32, Asn1 Encoder, Asn1 Decoder, Asn1 Validator, DER, Converter, Encoder, Decoder'
    TOOL_URL = 'https://github.com/impratikjaiswal/asn1play'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/asn1play/issues'
