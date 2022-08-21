from src.main.helper.formats import Formats

txt_formats = [Formats.ASN1, Formats.GET_VAL, Formats.GET_VAL_PATHS]

base64_formats = [Formats.DER_64, Formats.BER_64]

hex_formats = [Formats.DER, Formats.BER]

input_formats_supported = [Formats.DER, Formats.DER_64, Formats.ASN1]

parsing_format_mapping = {
    Formats.ASN1: 'to_asn1',
    Formats.DER: 'to_der',
    Formats.DER_64: 'to_der',
    Formats.GET_VAL: 'get_val',
    Formats.GET_VAL_PATHS: 'get_val_paths',
    Formats.GET_PROTO: 'get_proto',
    Formats.BER: 'to_ber',
    Formats.BER_64: 'to_ber',
    Formats.APER: 'to_aper',
    Formats.BER_WS: 'to_ber_ws',
    Formats.CER: 'to_cer',
    Formats.CER_WS: 'to_cer_ws',
    Formats.DER_WS: 'to_der_ws',
    Formats.JER: 'to_jer',
    Formats.JSON: 'to_json',
    Formats.UPER: 'to_uper',
}
