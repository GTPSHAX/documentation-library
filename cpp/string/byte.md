---
title: Null-terminated byte strings
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte
---


# Null-terminated byte strings

A null-terminated byte string (NTBS) is a possibly empty sequence of nonzero bytes followed by a byte with value zero (the terminating null character). Each byte in a byte string encodes one character of some character set. For example, the character array } is an NTBS holding the string `"cat"` in ASCII encoding.

## Functions


#### Character classification

| cctype | |
| cpp/string/byte/dsc isalnum | (see dedicated page) |
| cpp/string/byte/dsc isalpha | (see dedicated page) |
| cpp/string/byte/dsc islower | (see dedicated page) |
| cpp/string/byte/dsc isupper | (see dedicated page) |
| cpp/string/byte/dsc isdigit | (see dedicated page) |
| cpp/string/byte/dsc isxdigit | (see dedicated page) |
| cpp/string/byte/dsc iscntrl | (see dedicated page) |
| cpp/string/byte/dsc isgraph | (see dedicated page) |
| cpp/string/byte/dsc isspace | (see dedicated page) |
| cpp/string/byte/dsc isblank | (see dedicated page) |
| cpp/string/byte/dsc isprint | (see dedicated page) |
| cpp/string/byte/dsc ispunct | (see dedicated page) |

#### Character manipulation

| cpp/string/byte/dsc tolower | (see dedicated page) |
| cpp/string/byte/dsc toupper | (see dedicated page) |


#### Conversions to numeric formats

| cstdlib | |
| cpp/string/byte/dsc atof | (see dedicated page) |
| cpp/string/byte/dsc atoi | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtoul | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/string/byte/dsc strfromf | (see dedicated page) |
| cinttypes | |
| cpp/string/byte/dsc strtoimax | (see dedicated page) |

#### String manipulation

| cstring | |
| cpp/string/byte/dsc strcpy | (see dedicated page) |
| cpp/string/byte/dsc strncpy | (see dedicated page) |
| cpp/string/byte/dsc strcat | (see dedicated page) |
| cpp/string/byte/dsc strncat | (see dedicated page) |
| cpp/string/byte/dsc strxfrm | (see dedicated page) |
| cpp/string/byte/dsc strdup | (see dedicated page) |
| cpp/string/byte/dsc strndup | (see dedicated page) |

#### String examination

| cstring | |
| cpp/string/byte/dsc strlen | (see dedicated page) |
| cpp/string/byte/dsc strcmp | (see dedicated page) |
| cpp/string/byte/dsc strncmp | (see dedicated page) |
| cpp/string/byte/dsc strcoll | (see dedicated page) |
| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/byte/dsc strrchr | (see dedicated page) |
| cpp/string/byte/dsc strspn | (see dedicated page) |
| cpp/string/byte/dsc strcspn | (see dedicated page) |
| cpp/string/byte/dsc strpbrk | (see dedicated page) |
| cpp/string/byte/dsc strstr | (see dedicated page) |
| cpp/string/byte/dsc strtok | (see dedicated page) |

#### Character array functions

| cstring | |
| cpp/string/byte/dsc memchr | (see dedicated page) |
| cpp/string/byte/dsc memcmp | (see dedicated page) |
| cpp/string/byte/dsc memset | (see dedicated page) |
| cpp/string/byte/dsc memcpy | (see dedicated page) |
| cpp/string/byte/dsc memmove | (see dedicated page) |
| cpp/string/byte/dsc memccpy | (see dedicated page) |

#### Miscellaneous

| cstring | |
| cpp/string/byte/dsc strerror | (see dedicated page) |


## See also

