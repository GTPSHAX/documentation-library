---
title: std::num_get::get
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/num_get/get
---


```cpp
dcl|num=1|
public:
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, bool& v ) const;
dcl|num=2|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long& v ) const;
dcl|num=3|since=c++11|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long long& v ) const;
dcl|num=4|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned short& v ) const;
dcl|num=5|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned int& v ) const;
dcl|num=6|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned long& v ) const;
dcl|num=7|since=c++11|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned long long& v ) const;
dcl|num=8|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, float& v ) const;
dcl|num=9|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, double& v ) const;
dcl|num=10|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long double& v ) const;
dcl|num=11|
iter_type get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, void*& v ) const;
dcl|num=12|
protected:
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, bool& v ) const;
dcl|num=13|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long& v ) const;
dcl|num=14|since=c++11|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long long& v ) const;
dcl|num=15|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned short& v ) const;
dcl|num=16|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned int& v ) const;
dcl|num=17|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, unsigned long& v ) const;
dcl|num=18|since=c++11|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err,
unsigned long long& v ) const;
dcl|num=19|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, float& v ) const;
dcl|num=20|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, double& v ) const;
dcl|num=21|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, long double& v ) const;
dcl|num=22|
virtual iter_type do_get( iter_type in, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, void*& v ) const;
```

@1-11@ Public member function, calls the member function `do_get` of the most derived class.
@12-22@ Reads characters from the input iterator `in` and generates the value of the type of `v`, taking into account I/O stream formatting flags from `str.flags()`, character classification rules from `std::use_facet<std::ctype<CharT>>(str.getloc())`, and numeric punctuation characters from `std::use_facet<std::numpunct<CharT>>(str.getloc())`. This function is called by all formatted input stream operators such as `std::cin >> n;`.
Conversion occurs in three stages:

### Stage 1: conversion specifier selection

* I/O format flags are obtained, as if by
: `1=fmtflags basefield = (str.flags() & std::ios_base::basefield);`
: `1=fmtflags boolalpha = (str.flags() & std::ios_base::boolalpha);`
* If the type of `v` is an integer type, the first applicable choice of the following five is selected:
: If `1=basefield == oct`, will use conversion specifier `%o`
: If `1=basefield == hex`, will use conversion specifier `%X`
: If `1=basefield == 0`, will use conversion specifier `%i`
: If the type of `v` is signed, will use conversion specifier `%d`
: If the type of `v` is unsigned, will use conversion specifier `%u`
* For integer types, length modifier is added to the conversion specification if necessary: `h` for `short` and `unsigned short`, `l` for `long` and `unsigned long`<sup>(since C++11)</sup> , `ll` for `long long` and `unsigned long long`
* If the type of `v` is `float`, will use conversion specifier `%g`
* If the type of `v` is `double`, will use conversion specifier `%lg`
* If the type of `v` is `long double`, will use conversion specifier `%Lg`
* If the type of `v` is `void*`, will use conversion specifier `%p`
* If the type of `v` is `bool` and `1=boolalpha == 0`, proceeds as if the type of `v` is `long`, except for the value to be stored in `v` in stage 3.
* If the type of `v` is `bool` and `1=boolalpha != 0`, the following replaces stages 2 and 3:
** Successive characters obtained from the input iterator `in` are matched against the character sequences obtained from `std::use_facet<std::numpunct<CharT>>(str.getloc()).falsename()` and `std::use_facet<std::numpunct<CharT>>(str.getloc()).truename()` only as necessary as to identify the unique match. The input iterator `in` is compared to `end` only when necessary to obtain a character.
** If the target sequence is uniquely matched, `v` is set to the corresponding `bool` value. Otherwise `false` is stored in `v` and `std::ios_base::failbit` is assigned to `err`. If unique match could not be found before the input ended (`1=in == end`), `1=err  is executed.

### Stage 2: character extraction

* If `1=in == end`, stage 2 is terminated immediately, no further characters are extracted.
* The next character is extracted from `in` as if by `1=char_type ct = *in;`:
** If the character matches one of <sup>(until C++11)</sup> `"0123456789abcdefxABCDEFX+-"`<sup>(since C++11)</sup> `"0123456789abcdefpxABCDEFPX+-"`, widened to the locale's char_type as if by `std::use_facet<std::ctype<CharT>>(str.getloc()).widen()`, it is converted to the corresponding `char`.
** If the character matches the decimal point separator (`std::use_facet<std::numpunct<CharT>>(str.getloc()).decimal_point())`), it is replaced by `'.'`.
** If the character matches the thousands separator (`std::use_facet<std::numpunct<CharT>>(str.getloc()).thousands_sep()`) and the thousands separation is in use (as determined by `1=std::use_facet<std::numpunct<CharT>>(str.getloc()).grouping().length() != 0`), then if the decimal point `'.'` has not yet been accumulated, the position of the character is remembered, but the character is otherwise ignored. If the decimal point has already been accumulated, the character is discarded and stage 2 terminates.
** In any case, the check is made whether the `char` obtained from the previous steps is allowed in the input field that would be parsed by `std::scanf` given the conversion specifier selected in stage 1. If it is allowed, it is accumulated in a temporary buffer and stage 2 repeats. If it is not allowed, stage 2 terminates.

### Stage 3: conversion and storage

* The sequence of `char`s accumulated in stage 2 is converted to a numeric value:
rev|until=c++11|
: The input is parsed according to the rules of `std::scanf`.
rev|since=c++11|
: The input is parsed as if by
:* `std::strtoll` for signed integer `v`,
:* `std::strtoull` for unsigned integer `v`,
:* `std::strtof` for `float` `v`,
:* `std::strtod` for `double` `v`, or
:* `std::strtold` for `long double` `v`.
* If the conversion function fails to convert the entire field, the value `0` is stored in `v`.
* If the type of `v` is a signed integer type and the conversion function results in a positive or negative value too large to fit in it, the most positive or negative representable value is stored in `v`, respectively.
* If the type of `v` is an unsigned integer type and the conversion function results in a value that does not fit in it, the most positive representable value is stored in `v`.
* In any case, if the conversion function fails `std::ios_base::failbit` is assigned to `err`.
* Otherwise, the numeric result of the conversion is stored in `v`.
** If the type of `v` is `bool` and boolalpha is not set, then if the value to be stored is `0`, `false` is stored, if the value to be stored is `1`, `true` is stored, for any other value `std::ios_base::failbit` is assigned to `err` and `true` is stored.
* After this, digit grouping is checked. if the position of any of the thousands separators discarded in stage 2 does not match the grouping provided by `std::use_facet<std::numpunct<CharT>>(str.getloc()).grouping()`, `std::ios_base::failbit` is assigned to `err`.
* If stage 2 was terminated by the test `1=in == end`, `1=err  is executed to set the eof bit.

## Return value

`in`

## Notes

Before the resolutions of  and , `v` was left unchanged if an error occurs.
Before the resolution of , strings representing hexadecimal integers (e.g. `"0xA0"`) were rejected by `do_get(int)` even if they are valid input to `cpp/string/byte/strtol` because stage 2 filters out characters `'X'` and `'x'`.
Before the resolution of , converting a negative number string into an unsigned integer might produce zero (since the value represented by the string is smaller than what the target type can represent).
rrev|since=c++11|
Before the resolution of , strings representing hexadecimal floating-point numbers with exponents (e.g. `"0x1.23p-10"`) were rejected by `do_get(double)` even if they are valid input to `cpp/string/byte/strtof|strtod` because stage 2 filters out characters `'P'` and `'p'`.
The strings representing infinity or not-a-number (e.g. `"NaN"` and `"inf"`) are rejected by `do_get(double)` even if they are valid input to `strtod` because stage 2 filters out characters such as `'N'` or `'i'`.

## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <locale>

struct base { long x; };

template<class CharT, class Traits>
std::basic_istream<CharT, Traits>&
    operator >>(std::basic_istream<CharT, Traits>& is, base& b)
{
    std::ios_base::iostate err = std::ios_base::goodbit;

    try // setting err could throw
    {
        typename std::basic_istream<CharT, Traits>::sentry s(is);

        if (s) // if stream is ready for input
            std::use_facet<std::num_get<CharT>>(is.getloc()).get(is, {}, is, err, b.x);
    }
    catch (std::ios_base::failure& error)
    {
        // handle the exception
    }

    return is;
}

int main()
{
    base b;
    std::cin >> b;
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-17 | C++98 | the process of parsing text boolean values was errornous | corrected |
| lwg-23 | C++98 | overflowing input resulted in undefined behavior | overflow handled |
| lwg-358 | C++98 | thousand separators after the decimal point were ignored | stage 2 is terminated if encountered |
| lwg-696 | C++98 | the result was unchanged on conversion failure | set to zero |
| lwg-1169 | C++98 | overflow handling was inconsistent between floating-point types | made consistent<br>with tt |


## See also


| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |

