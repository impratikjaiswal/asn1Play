class Asn1Schema:
    def __init__(self, asn1_family=None, asn1_version=None, asn1_class_name=None):
        self.asn1_family = asn1_family
        self.asn1_version = asn1_version
        self.asn1_class_name = asn1_class_name

    def get_asn1_family(self):
        return self.asn1_family

    def get_asn1_version(self):
        return self.asn1_version

    def get_asn1_class_name(self):
        return self.asn1_class_name

    def get_name(self, full_name=False):
        if full_name:
            return '_'.join(filter(None, [self.asn1_family, self.asn1_version, self.asn1_class_name]))
        else:
            return '_'.join(filter(None, [self.asn1_family, self.asn1_version]))
