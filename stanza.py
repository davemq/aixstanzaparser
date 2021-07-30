from configparser import _default_dict
from configparser import _UNSET
from configparser import ConfigParser
from configparser import DEFAULTSECT
import re

class AIXStanzaParser(ConfigParser):
    """ Parse AIX stanza files """

    def __init__(self, defaults=None, dict_type=_default_dict,
                 allow_no_value=False, *, delimiters=('='),
                 comment_prefixes=('#', ';'), inline_comment_prefixes=None,
                 strict=True, empty_lines_in_values=True,
                 default_section=DEFAULTSECT,
                 interpolation=_UNSET, converters=_UNSET,
                 sectionBegin="", sectionEnd=":", keyValuePrefix="\t"):

        super().__init__(defaults, dict_type,
                         allow_no_value, delimiters=delimiters,
                         comment_prefixes=comment_prefixes,
                         inline_comment_prefixes=inline_comment_prefixes,
                         strict=strict, empty_lines_in_values=empty_lines_in_values,
                         default_section=default_section,
                         interpolation=interpolation, converters=converters)
        self._sectionBegin   = sectionBegin
        self._sectionEnd     = sectionEnd
        self._keyValuePrefix = keyValuePrefix
        self.SECTCRE         = re.compile(r"""
        """ + self._sectionBegin + r"(?P<header>[^" +
                                        self._sectionEnd + r"]*)" +
                                        self._sectionEnd + r"""
                                        """,
                                        re.VERBOSE)

