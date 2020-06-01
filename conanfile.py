from conans import ConanFile, Meson, tools
import os

class OrcConan(ConanFile):
    name = "orc"
    version = tools.get_env("GIT_TAG", "0.4.31")
    settings = "os", "compiler", "build_type", "arch"
    license = "LGPL-2.1"
    description = "Optimized Inner Loop Runtime Compiler"
    generators = "pkgconf"

    def build_requirements(self):
        self.build_requires("generators/1.0.0@camposs/stable")
        self.build_requires("meson/[>=0.51.2]@camposs/stable")

    def source(self):
        tools.get("https://github.com/GStreamer/orc/archive/%s.tar.gz" % self.version)

    def build(self):
        args = ["-Dgtk_doc=disabled"]
        args.append("-Dbenchmarks=disabled")
        args.append("-Dexamples=disabled")
        meson = Meson(self)
        meson.configure(source_folder="orc-" + self.version, args=args, pkg_config_paths=os.environ["PKG_CONFIG_PATH"].split(":"))
        meson.install()
