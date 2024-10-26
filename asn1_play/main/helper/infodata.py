from python_helpers.ph_util import PhUtil


class InfoData:
    def __init__(self, info=[]):
        self.info = info
        self.set_info(self.info)

    def set_info(self, info):
        self.info = PhUtil.to_list(info, trim_data=True, all_str=True)

    def get_info_list(self):
        return self.info

    def get_info_count(self):
        return len(self.info)

    def get_info_str(self, sep='\n\t'):
        return sep.join(filter(None, self.info))
