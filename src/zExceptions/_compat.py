import codecs
import sys


PY3 = sys.version_info[0] == 3
if PY3:
    import builtins
    class_types = type,
    string_types = (str, bytes)
    unicode = str
    u = lambda s: s
else:
    import __builtin__ as builtins  # noqa
    from types import ClassType
    class_types = (type, ClassType)
    string_types = basestring,
    unicode = unicode

    def u(s):
        return codecs.unicode_escape_decode(s)[0]