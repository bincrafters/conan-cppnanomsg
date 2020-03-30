import os
from conans import ConanFile, tools


class CppnanomsgConan(ConanFile):
    name = "cppnanomsg"
    version = "20181216"
    _commit_id = "a36d44db1827a36bbd3868825c1b82d23f10e491"
    description = "C++ binding for nanomsg"
    topics = ("conan", "cppnanomsg", "nanomsg", "binding")
    url = "https://github.com/bincrafters/conan-cppnanomsg"
    homepage = "https://github.com/nanomsg/cppnanomsg"
    license = "MIT"
    requires = ("nanomsg/1.1.2@bincrafters/stable")

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/{1}.zip".format(self.homepage, self._commit_id),
                  sha256="a857c0d4698cb68128071711fc9c3e7aaa7751f4d6f20d9ba2e86d94ce6695d7")
        extracted_dir = self.name + "-" + self._commit_id
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        self.copy("nn.hpp", dst="include/cppnanomsg", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
