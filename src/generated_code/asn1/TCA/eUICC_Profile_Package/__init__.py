from src.generated_code.asn1.TCA.eUICC_Profile_Package.version import Version

# Default version to be used in whole system
version = Version.v3_2

if version == Version.v1_0:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v1_0.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v1_0.epp_mapping import epp_mapping

if version == Version.v2_0:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_0.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_0.epp_mapping import epp_mapping

if version == Version.v2_1:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_1.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_1.epp_mapping import epp_mapping

if version == Version.v2_2:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_2.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_2.epp_mapping import epp_mapping

if version == Version.v2_3:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3.epp_mapping import epp_mapping

if version == Version.v2_3_1:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3_1.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3_1.epp_mapping import epp_mapping

if version == Version.v3_0:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_0.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_0.epp_mapping import epp_mapping

if version == Version.v3_1:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_1.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_1.epp_mapping import epp_mapping

if version == Version.v3_2:
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_2.epp import PEDefinitions
    from src.generated_code.asn1.TCA.eUICC_Profile_Package.v3_2.epp_mapping import epp_mapping
