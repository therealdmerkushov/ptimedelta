import sys

PY3 = sys.version_info.major == 3

if PY3:
    string_types = (str,)
else:
    string_types = (basestring,)
