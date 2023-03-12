from src.generated_code.asn1.GSMA.SGP_22.version import Version

# Default version to be used in whole system
version = Version.v3_0_0

if version == Version.v1_0:
    from src.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping
if version == Version.v1_1:
    from src.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v1_2:
    from src.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_0:
    from src.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_1:
    from src.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2:
    from src.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2_1:
    from src.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2_2:
    from src.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_3:
    from src.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_4:
    from src.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_4_sgp23_1_11:
    from src.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v3_0_0:
    from src.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from src.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

