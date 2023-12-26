import importlib

# from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32 import SGP32Definitions
# from asn1_play.generated_code.asn1.GSMA.SGP_32.v1_0_1.python_gen.sgp32.sgp32_mapping import sgp_32_mapping

OFFSET_CLASSES = 0
OFFSET_MAPPING_CLASSES = 1

__module_name = '.sgp32'
__module_mapping_name = '.sgp32_mapping'
__class_name = 'SGP32Definitions'
__class_name_mapping = 'sgp_32_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.GSMA.SGP_32'
__package_name_post = 'python_gen.sgp32'

version = None
SGP32Definitions = None
sgp_32_mapping = None


def is_valid_state():
    global version
    return False if version is None else True


def get_version():
    global version
    return version


def set_version(version_user):
    def __set_version(version_user_local):
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

    imported_objects = __set_version(version_user)
    if imported_objects is None:
        return None

    global version, SGP32Definitions, sgp_32_mapping
    version = version_user
    SGP32Definitions = imported_objects[OFFSET_CLASSES][0]
    sgp_32_mapping = imported_objects[OFFSET_MAPPING_CLASSES][0]
