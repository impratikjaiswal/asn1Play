import importlib

from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22 import RSPDefinitions
from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22_mapping import sgp_22_mapping
from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import PKIX1Explicit88, PKIX1Implicit88


class Version:
    v1_0 = 'v1_0'
    v1_1 = 'v1_1'
    v1_2 = 'v1_2'
    v2_0 = 'v2_0'
    v2_1 = 'v2_1'
    v2_2 = 'v2_2'
    v2_2_1 = 'v2_2_1'
    v2_2_2 = 'v2_2_2'
    v2_3 = 'v2_3'
    v2_4 = 'v2_4'
    v2_4_sgp23_1_11 = 'v2_4_sgp23_1_11'
    v2_5 = 'v2_5'
    v3_0_0 = 'v3_0_0'
    v3_1 = 'v3_1'


# Default version to be used in whole system
version = Version.v3_0_0

if version == Version.v1_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping
if version == Version.v1_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v1_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_2_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_3:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_4:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v2_4_sgp23_1_11:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22_mapping import sgp_22_mapping

if version == Version.v3_0_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22_mapping import sgp_22_mapping