import importlib

from asn1_play.generated_code.asn1.GSMA.SGP_32.compile_time_version import CompileTimeVersion
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions

####################
# Compile Time Stuff
####################

# Default version to be used in whole system
version = CompileTimeVersion.v1_0_1

if version == CompileTimeVersion.v1_0:
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0.python_gen.sgp32.sgp32 import SGP32Definitions
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0.python_gen.sgp32.sgp32_mapping import \
        sgp_32_mapping as asn1_mapping

    default_asn_version_sgp32 = Asn1Versions.GSMA_SGP_32_v1_0

elif version == CompileTimeVersion.v1_0_1:
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32 import SGP32Definitions
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32_mapping import \
        sgp_32_mapping as asn1_mapping

    default_asn_version_sgp32 = Asn1Versions.GSMA_SGP_32_v1_0_1

else:
    # Default Version
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32 import SGP32Definitions
    from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32_mapping import \
        sgp_32_mapping as asn1_mapping

    default_asn_version_sgp32 = Asn1Versions.GSMA_SGP_32_v1_0_1

####################
# Run Time Stuff
####################
asn1_mapping = None
# SGP32Definitions = None

__module_name = '.sgp32'
__module_mapping_name = '.sgp32_mapping'
__class_name = 'SGP32Definitions'
__class_name_mapping = 'sgp_32_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.GSMA.SGP_32'
__package_name_post = 'python_gen.sgp32'


def __set_asn1_classes(param):
    global SGP32Definitions
    SGP32Definitions = param


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
