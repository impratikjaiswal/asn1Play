class Asn1Source:
    def __init__(self, asn1_paths=None, specification_paths=None):
        self.asn1_paths = asn1_paths
        self.specification_paths = specification_paths

    def get_asn1_paths(self):
        return self.asn1_paths

    def get_specification_paths(self):
        return self.specification_paths
