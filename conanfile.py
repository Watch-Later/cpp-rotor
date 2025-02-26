from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

required_conan_version = ">=1.43.0"


class RotorConan(ConanFile):
    name = "rotor"
    license = "MIT"
    homepage = "https://github.com/basiliscos/cpp-rotor"
    url = "https://github.com/conan-io/conan-center-index"
    description = (
        "Event loop friendly C++ actor micro-framework, supervisable"
    )
    topics = ("concurrency", "actor-framework", "actors", "actor-model", "erlang", "supervising", "supervisor")

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "fPIC": [True, False],
        "boost_asio": [True, False],
        "thread": [True, False],
    }
    default_options = {
        "fPIC": True,
        "boost_asio": True,
        "thread": True,
    }

    exports_sources = ["CMakeLists.txt", "include*", "src*", "test_package*", "cmake*"]
    generators = "cmake_find_package"
    _cmake = None

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("boost/1.69.0")


    def validate(self):
        minimal_cpp_standard = "17"
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, minimal_cpp_standard)
        minimal_version = {
            "gcc": "7",
            "clang": "6",
            "apple-clang": "10",
            "Visual Studio": "15"
        }
        compiler = str(self.settings.compiler)
        if compiler not in minimal_version:
            self.output.warn(
                "%s recipe lacks information about the %s compiler standard version support" % (self.name, compiler))
            self.output.warn(
                "%s requires a compiler that supports at least C++%s" % (self.name, minimal_cpp_standard))
            return

        version = tools.Version(self.settings.compiler.version)
        if version < minimal_version[compiler]:
            raise ConanInvalidConfiguration("%s requires a compiler that supports at least C++%s" % (self.name, minimal_cpp_standard))

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake

        self._cmake = CMake(self)
        self._cmake.definitions["BUILD_BOOST_ASIO"] = self.options.boost_asio
        self._cmake.definitions["BUILD_THREAD"] = self.options.thread
        self._cmake.definitions["BUILD_TESTING"] = False
        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.components["core"].libs = ["rotor"]
        self.cpp_info.components["core"].requires = ["boost::date_time", "boost::system", "boost::regex"]

        self.cpp_info.components["asio"].libs = ["rotor_asio"]
        self.cpp_info.components["asio"].requires = ["core"]

        self.cpp_info.components["thread"].libs = ["rotor_thread"]
        self.cpp_info.components["thread"].requires = ["core"]

        # TODO: to remove in conan v2 once cmake_find_package* generators removed
        self.cpp_info.names["cmake_find_package"] = "rotor"
        self.cpp_info.names["cmake_find_package_multi"] = "rotor"

