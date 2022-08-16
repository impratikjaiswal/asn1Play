from src.helper.formats import Formats


class Data:
    def __init__(self, raw_data, asn1_element, input_format=Formats.DEFAULT_INPUT,
                 output_format=Formats.DEFAULT_OUTPUT):
        self.raw_data = raw_data
        self.asn1_element = asn1_element
        self.input_format = input_format
        self.output_format = output_format
