import importlib

from asn1_play.generated_code.asn1.GSMA.SGP_22.compile_time_version import CompileTimeVersion
from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import PKIX1Explicit88, PKIX1Implicit88
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions

####################
# Compile Time Stuff
####################

# Default version to be used in whole system
version = CompileTimeVersion.v3_0_0

if version == CompileTimeVersion.v1_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_0.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v1_0

elif version == CompileTimeVersion.v1_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_1.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v1_1

elif version == CompileTimeVersion.v1_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v1_2.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v1_2

elif version == CompileTimeVersion.v2_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_0.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_0

elif version == CompileTimeVersion.v2_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_1.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_1

elif version == CompileTimeVersion.v2_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_2

elif version == CompileTimeVersion.v2_2_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_1.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_2_1

elif version == CompileTimeVersion.v2_2_2:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_2_2.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_2_2

elif version == CompileTimeVersion.v2_3:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_3.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_3

elif version == CompileTimeVersion.v2_4:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_4

elif version == CompileTimeVersion.v2_4_sgp23_1_11:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_4_sgp23_1_11.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_4_sgp23_1_11

elif version == CompileTimeVersion.v2_5:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_5.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v2_5.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v2_5

elif version == CompileTimeVersion.v3_0_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_0_0.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v3_0_0

elif version == CompileTimeVersion.v3_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_1.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v3_1

else:
    # Default Version
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_1.python_gen.sgp22.sgp22 import RSPDefinitions
    from asn1_play.generated_code.asn1.GSMA.SGP_22.v3_1.python_gen.sgp22.sgp22_mapping import \
        sgp_22_mapping as asn1_mapping

    default_asn_version_sgp22 = Asn1Versions.SGP_22_v3_1

####################
# Run Time Stuff
####################
asn1_mapping = None
# RSPDefinitions = None

__module_name = '.sgp22'
__module_mapping_name = '.sgp22_mapping'
__class_name = 'RSPDefinitions'
__class_name_mapping = 'sgp_22_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.GSMA.SGP_22'
__package_name_post = 'python_gen.sgp22'


def __set_asn1_classes(param):
    global RSPDefinitions
    RSPDefinitions = param


def __set_asn1_mapping(param):
    pkix_mapping = {
        'Certificate': PKIX1Explicit88.Certificate,
        'CertificateList': PKIX1Explicit88.CertificateList,
        'Time': PKIX1Explicit88.Time,
        'SubjectKeyIdentifier': PKIX1Implicit88.SubjectKeyIdentifier,
    }
    # TODO: SML-332
    all_mapping = {
        **param,
        **pkix_mapping
    }
    global asn1_mapping
    asn1_mapping = all_mapping


def is_valid_state():
    return False if version is None else True


def get_version():
    return version


def set_version(version_user):
    OFFSET_CLASSES = 0
    OFFSET_MAPPING_CLASSES = 1

    def __set_version_duck_typing(version_user_local):
        try:
            package_name = '.'.join([__package_name_pre, version_user_local, __package_name_post])

            module_imported = importlib.import_module(__module_name, package_name)
            class_imported = getattr(module_imported, __class_name)

            module_mapping_imported = importlib.import_module(__module_mapping_name, package_name)
            class_mapping_imported = getattr(module_mapping_imported, __class_name_mapping)
        except Exception:
            return None
            # raise AttributeError(
            #     PhExceptionHelper(msg=f'Unknown version {version}', function_name=set_version))
        # PhUtil.print_modules(filter_string=package_name)
        # PhUtil.get_classes_list(module_to_explore=module_imported, print_also=True)
        return [class_imported], [class_mapping_imported]

    imported_objects = __set_version_duck_typing(version_user)
    if imported_objects is None:
        return None
    __set_version(version_user)
    __set_asn1_classes(imported_objects[OFFSET_CLASSES][0])
    __set_asn1_mapping(imported_objects[OFFSET_MAPPING_CLASSES][0])


def __set_version(param):
    global version
    version = param


def get_asn1_mapping():
    return asn1_mapping


def get_asn1_mapping_keys():
    return list(asn1_mapping.keys())


def get_class_name():
    return __class_name
