# -*- coding: utf-8 -*-

name = 'llvm'

version = '9.0.1-ta.1.0.0'

authors = [
    'benjamin.skinner',
]

build_requires = [
]

requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x64'],
]

build_system = "cmake"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.LLVM_VERSION.set(split_versions[0])
    env.LLVM_PACKAGE_VERSION.set(split_versions[1])

    env.LLVM_ROOT.set("{root}")
    env.LLVM_INCLUDE_DIR.set("{root}/include")
    env.LLVM_LIBRARY_DIR.set("{root}/lib")
    env.LLVM_BINARY_DIR.set("{root}/bin")

    env.PATH.append( str(env.LLVM_BINARY_DIR) )
