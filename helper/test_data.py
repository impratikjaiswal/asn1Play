class TestData:
    def __init__(self, data, asn1_element, input_format='der', output_format='asn1'):
        self.data = data
        self.asn1_element = asn1_element
        self.input_format = input_format
        self.output_format = output_format
