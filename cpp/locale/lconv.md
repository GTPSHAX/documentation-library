---
title: std::lconv
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/lconv
---


```cpp
dcl | 1=
struct lconv;
```

The class `std::lconv` contains numeric and monetary formatting rules as defined by a C locale. Objects of this struct may be obtained with `std::localeconv`. The members of `std::lconv` are values of type `char` and of type `char*`. Each `char*` member except `decimal_point` may be pointing at a null character (that is, at an empty C-string). The members of type `char` are all non-negative numbers, any of which may be `CHAR_MAX` if the corresponding value is not available in the current C locale.

## Member objects


### Non-monetary numeric formatting parameters


### Monetary numeric formatting parameters


### Local monetary numeric formatting parameters


### International monetary numeric formatting parameters

The characters of the C-strings pointed to by `grouping` and `mon_grouping` are interpreted according to their numeric values. When the terminating `'\0'` is encountered, the last value seen is assumed to repeat for the remainder of digits. If `CHAR_MAX` is encountered, no further digits are grouped. the typical grouping of three digits at a time is `"\003"`.
The values of `p_sep_by_space`, `n_sep_by_space`, `int_p_sep_by_space`, `int_n_sep_by_space` are interpreted as follows:
The values of `p_sign_posn`, `n_sign_posn`, `int_p_sign_posn`, `int_n_sign_posn` are interpreted as follows:

## Example


## See also

