genrule(
    name = "example",
    srcs = ["example.i"],
    outs = [
               "example.py",
               "example_wrap.c"
           ],
    cmd = "swig -python -outdir $(@D) -o $(@D)/example_wrap.c $<",
)

cc_binary(
    name = "_example.so",
    srcs = [
                "example.c",
		":example_wrap.c",
		"example.h"	
           ],
    includes = ["."],
    copts = ["-I/usr/include/python2.7"],
    linkstatic = 1,
    linkshared = 1,
)

py_library(
    name = "py_lib",
    data = [
               ":example.py",
               ":_example.so",
           ],
    imports = [":example.py"],
    visibility = ["//test:__pkg__"],
)
