txt_formats = ['asn1', 'get_val', 'get_val_paths']

base64_formats = ['der_with_base64', 'ber_with_base64']

hex_formats = ['der', 'ber']

input_formats_supported = ['der', 'asn1']

parsing_format_mapping = {
    'asn1': 'to_asn1',
    'der': 'to_der',
    'der_with_base64': 'to_der',
    'get_val': 'get_val',
    'get_val_paths': 'get_val_paths',
    'get_proto': 'get_proto',
    'ber': 'to_ber',
    'ber_with_base64': 'to_ber',
    'aper': 'to_aper',
    'ber_ws': 'to_ber_ws',
    'cer': 'to_cer',
    'cer_ws': 'to_cer_ws',
    'der_ws': 'to_der_ws',
    'jer': 'to_jer',
    'json': 'to_json',
    'uper': 'to_uper',
}
