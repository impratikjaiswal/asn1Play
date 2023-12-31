import importlib

from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.compile_time_version import CompileTimeVersion
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions

####################
# Compile Time Stuff
####################

# Default version to be used in whole system
version = CompileTimeVersion.v3_2

if version == CompileTimeVersion.v1_0:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v1_0.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v1_0.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v1_0

elif version == CompileTimeVersion.v2_0:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_0.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_0.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v2_0

elif version == CompileTimeVersion.v2_1:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_1.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_1.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v2_1

elif version == CompileTimeVersion.v2_2:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_2.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_2.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v2_2

elif version == CompileTimeVersion.v2_3:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v2_3

elif version == CompileTimeVersion.v2_3_1:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3_1.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v2_3_1.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v2_3_1

elif version == CompileTimeVersion.v3_0:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_0.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_0.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_0

elif version == CompileTimeVersion.v3_1:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_1.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_1.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_1

elif version == CompileTimeVersion.v3_2:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_2.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_2.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_2

elif version == CompileTimeVersion.v3_3:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_3

elif version == CompileTimeVersion.v3_3_1:
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_3_1

else:
    # Default Version
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp import PEDefinitions
    from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp_mapping import \
        epp_mapping as asn1_mapping

    default_asn_version_epp = Asn1Versions.TCA_EPP_v3_3_1

####################
# Run Time Stuff
####################
asn1_mapping = None
# PEDefinitions = None

__module_name = '.epp'
__module_mapping_name = '.epp_mapping'
__class_name = 'PEDefinitions'
__class_name_mapping = 'epp_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package'
__package_name_post = 'python_gen.epp'


def __set_asn1_classes(param):
    global PEDefinitions
    PEDefinitions = param


def __set_asn1_mapping(param):
    all_mapping = {
        **param,
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
