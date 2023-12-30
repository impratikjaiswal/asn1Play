import importlib

# from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp import PEDefinitions
# from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.v3_3_1.python_gen.epp.epp_mapping import epp_mapping

OFFSET_CLASSES = 0
OFFSET_MAPPING_CLASSES = 1

__module_name = '.epp'
__module_mapping_name = '.epp_mapping'
__class_name = 'PEDefinitions'
__class_name_mapping = 'epp_mapping'
__package_name_pre = 'asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package'
__package_name_post = 'python_gen.epp'

version = None
asn1_mapping = None
PEDefinitions = None


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
