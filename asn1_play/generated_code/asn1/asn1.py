from asn1_play.generated_code.asn1.GSMA import SGP_22 as package_sgp_22
from asn1_play.generated_code.asn1.GSMA import SGP_32 as package_sgp_32
from asn1_play.generated_code.asn1.TCA import eUICC_Profile_Package as package_epp
from asn1_play.generated_code.asn1.asn1_schema import Asn1Schema
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions, Asn1Family
from asn1_play.main.helper.defaults import Defaults


class Asn1:
    def __init__(self, asn1_schema=None, asn1_object=None):
        self.asn1_schema = None
        self.asn1_mapping = None
        self.__set_asn1_schema(asn1_schema)
        self.asn1_object = None
        self.__set_asn1_object(asn1_object)

    def __set_asn1_schema(self, asn1_schema):
        if asn1_schema is None or not isinstance(asn1_schema, Asn1Schema):
            # set defaults:
            asn1_schema = Defaults.ASN1_SCHEMA
        asn1_family = asn1_schema.asn1_family
        asn1_user_version = asn1_schema.asn1_version
        package = None
        if asn1_family == Asn1Family.SGP_22:
            package = package_sgp_22
        if asn1_family == Asn1Family.SGP_32:
            package = package_sgp_32
        if asn1_family == Asn1Family.TCA_EPP:
            package = package_epp
        if package is None:
            raise
        package.set_version(asn1_user_version)
        state = package.is_valid_state()
        if state is False:
            raise
        self.asn1_schema = asn1_schema
        self.asn1_mapping = package.get_asn1_mapping()

    def get_asn1_schema(self):
        return self.asn1_schema

    def __set_asn1_object(self, asn1_object):
        self.asn1_object = asn1_object.strip() if asn1_object else None

    def get_asn1_object(self):
        return self.asn1_object

    def get_asn1_mapping(self):
        return self.asn1_mapping
