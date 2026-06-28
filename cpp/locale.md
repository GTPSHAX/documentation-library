---
title: Localization library
type: Localizations
source: https://en.cppreference.com/w/cpp/locale
---


# Localization library

The locale facility includes internationalization support for character classification and string collation, numeric, monetary, and date/time formatting and parsing, and message retrieval. Locale settings control the behavior of stream I/O, regular expression library, and other components of the C++ standard library.

## Locales and facets


| locale | |

#### Locales

| cpp/locale/dsc locale | (see dedicated page) |
| cpp/locale/dsc use_facet | (see dedicated page) |
| cpp/locale/dsc has_facet | (see dedicated page) |

#### Facet category base classes

| cpp/locale/dsc ctype_base | (see dedicated page) |
| cpp/locale/dsc codecvt_base | (see dedicated page) |
| cpp/locale/dsc messages_base | (see dedicated page) |
| cpp/locale/dsc time_base | (see dedicated page) |
| cpp/locale/dsc money_base | (see dedicated page) |

#### ctype facets

| cpp/locale/dsc ctype | (see dedicated page) |
| cpp/locale/dsc ctype_byname | (see dedicated page) |
| cpp/locale/dsc ctype_char | (see dedicated page) |
| cpp/locale/dsc codecvt | (see dedicated page) |
| cpp/locale/dsc codecvt_byname | (see dedicated page) |

#### numeric facets

| cpp/locale/dsc num_get | (see dedicated page) |
| cpp/locale/dsc num_put | (see dedicated page) |
| cpp/locale/dsc numpunct | (see dedicated page) |
| cpp/locale/dsc numpunct_byname | (see dedicated page) |

#### collate facets

| cpp/locale/dsc collate | (see dedicated page) |
| cpp/locale/dsc collate_byname | (see dedicated page) |

#### time facets

| cpp/locale/dsc time_get | (see dedicated page) |
| cpp/locale/dsc time_get_byname | (see dedicated page) |
| cpp/locale/dsc time_put | (see dedicated page) |
| cpp/locale/dsc time_put_byname | (see dedicated page) |

#### monetary facets

| cpp/locale/dsc money_get | (see dedicated page) |
| cpp/locale/dsc money_put | (see dedicated page) |
| cpp/locale/dsc moneypunct | (see dedicated page) |
| cpp/locale/dsc moneypunct_byname | (see dedicated page) |

#### messages facets

| cpp/locale/dsc messages | (see dedicated page) |
| cpp/locale/dsc messages_byname | (see dedicated page) |


## Character classification and conversion


| locale | |

#### Character classification

| cpp/locale/dsc isspace | (see dedicated page) |
| cpp/locale/dsc isblank | (see dedicated page) |
| cpp/locale/dsc iscntrl | (see dedicated page) |
| cpp/locale/dsc isupper | (see dedicated page) |
| cpp/locale/dsc islower | (see dedicated page) |
| cpp/locale/dsc isalpha | (see dedicated page) |
| cpp/locale/dsc isdigit | (see dedicated page) |
| cpp/locale/dsc ispunct | (see dedicated page) |
| cpp/locale/dsc isxdigit | (see dedicated page) |
| cpp/locale/dsc isalnum | (see dedicated page) |
| cpp/locale/dsc isprint | (see dedicated page) |
| cpp/locale/dsc isgraph | (see dedicated page) |

#### Character conversions

| cpp/locale/dsc toupper | (see dedicated page) |
| cpp/locale/dsc tolower | (see dedicated page) |

#### String and stream conversions

| cpp/locale/dsc wstring_convert | (see dedicated page) |
| cpp/locale/dsc wbuffer_convert | (see dedicated page) |

rrev|until=c++26|

## Locale-independent unicode conversion facets


| codecvt | |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf16 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |
| cpp/locale/dsc codecvt_mode | (see dedicated page) |


## C library locales


| clocale | |
| cpp/locale/dsc setlocale | (see dedicated page) |
| cpp/locale/dsc LC_categories | (see dedicated page) |
| cpp/locale/dsc localeconv | (see dedicated page) |
| cpp/locale/dsc lconv | (see dedicated page) |


## See also

