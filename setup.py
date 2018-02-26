#!/usr/bin/env python

import os
import tensorflow as tf
from setuptools import setup, Extension


include_dirs = [".", tf.sysconfig.get_include()]
include_dirs.append(os.path.join(
    include_dirs[1], "external/nsync/public"))

extensions = [
    Extension(
        "maelstrom.kepler.kepler_op",
        sources=["maelstrom/kepler/kepler_op.cc"],
        language="c++",
        include_dirs=include_dirs,
        extra_compile_args=["-std=c++11", "-stdlib=libc++"],
    ),
    Extension(
        "maelstrom.interp.interp_op",
        sources=[
            "maelstrom/interp/searchsorted_op.cc",
        ],
        language="c++",
        include_dirs=include_dirs,
        extra_compile_args=["-std=c++11", "-stdlib=libc++"],
    ),
]

setup(
    name="maelstrom",
    license="MIT",
    packages=["maelstrom", "maelstrom.kepler", "maelstrom.interp"],
    ext_modules=extensions,
    zip_safe=True,
)
