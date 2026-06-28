---
title: std::regex_constants::match_flag_type
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_flag_type
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
using match_flag_type = /* implementation-defined */;
|1=
constexpr match_flag_type match_default =     {};
constexpr match_flag_type match_not_bol =     /* unspecified */;
constexpr match_flag_type match_not_eol =     /* unspecified */;
constexpr match_flag_type match_not_bow =     /* unspecified */;
constexpr match_flag_type match_not_eow =     /* unspecified */;
constexpr match_flag_type match_any =         /* unspecified */;
constexpr match_flag_type match_not_null =    /* unspecified */;
constexpr match_flag_type match_continuous =  /* unspecified */;
constexpr match_flag_type match_prev_avail =  /* unspecified */;
constexpr match_flag_type format_default =    {};
constexpr match_flag_type format_sed =        /* unspecified */;
constexpr match_flag_type format_no_copy =    /* unspecified */;
constexpr match_flag_type format_first_only = /* unspecified */;
```

1. `match_flag_type` is a *BitmaskType* that specifies additional regular expression matching options.

## Constants

Note: [first, last) refers to the character sequence being matched.


| Item | Description |
|------|-------------|
| **Name** | Explanation |

All constants, except for `match_default` and `format_default`, are bitmask elements. The `match_default` and `format_default` constants are empty bitmasks.

## Defect reports


## See also


| cpp/regex/dsc regex_match | (see dedicated page) |
| cpp/regex/dsc syntax_option_type | (see dedicated page) |
| cpp/regex/dsc error_type | (see dedicated page) |

