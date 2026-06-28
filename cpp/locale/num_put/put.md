---
title: std::num_put::put
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/num_put/put
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|
public:
iter_type put( iter_type out, std::ios_base& str,
char_type fill, bool val ) const;
dcl|num=2|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, long val ) const;
dcl|num=3|since=c++11|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, long long val ) const;
dcl|num=4|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, unsigned long val ) const;
dcl|num=5|since=c++11|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, unsigned long long val ) const;
dcl|num=6|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, double val ) const;
dcl|num=7|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, long double val ) const;
dcl|num=8|
iter_type put( iter_type out, std::ios_base& str,
char_type fill, const void* val ) const;
dcl|num=9|
protected:
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, bool val ) const;
dcl|num=10|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, long val ) const;
dcl|num=11|since=c++11|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, long long val ) const;
dcl|num=12|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, unsigned long val ) const;
dcl|num=13|since=c++11|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, unsigned long long val ) const;
dcl|num=14|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, double val ) const;
dcl|num=15|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, long double val ) const;
dcl|num=16|
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, const void* val ) const;
```

@1-8@ Public member function, calls the protected virtual member function `do_put` of the most derived class.
@9-16@ Writes characters to the output sequence `out` which represent the value of `val`, formatted as requested by the formatting flags `str.flags()` and the `std::numpunct` and `std::ctype` facets of the locale imbued in the stream `str`. This function is called by all formatted output stream operators, such as `std::cout << n;`.
Conversion occurs in four stages:

### Stage 1: conversion specifier selection

* I/O format flags are obtained, as if by
: `1=fmtflags basefield = (str.flags() & std::ios_base::basefield);`
: `1=fmtflags uppercase = (str.flags() & std::ios_base::uppercase);`
: `1=fmtflags floatfield = (str.flags() & std::ios_base::floatfield);`
: `1=fmtflags showpos = (str.flags() & std::ios_base::showpos);`
: `1=fmtflags showbase = (str.flags() & std::ios_base::showbase);`
: `1=fmtflags showpoint = (str.flags() & std::ios_base::showpoint);`
* If the type of `val` is `bool`:
** If `1=boolalpha == 0`, then converts `val` to type `int` and performs integer output.
** If `1=boolalpha != 0`, obtains `std::use_facet<std::numpunct<CharT>>(str.getloc()).truename()` if `1=val == true` or `std::use_facet<std::numpunct<CharT>>(str.getloc()).falsename()` if `1=val == false`, and outputs each successive character `c` of that string to `out` with `1=*out++ = c`. No further processing is done in this case, the function returns `out`.
* If the type of `val` is an integer type, the first applicable choice of the following is selected:
** If `1=basefield == oct`, will use conversion specifier `%o`.
** If `1=basefield == hex && !uppercase`, will use conversion specifier `%x`.
** If `1=basefield == hex`, will use conversion specifier `%X`.
** If the type of `val` is signed, will use conversion specifier `%d`.
** If the type of `val` is unsigned, will use conversion specifier `%u`.
* For integer types, length modifier is added to the conversion specification if necessary: `l` for `long` and `unsigned long`<sup>(since C++11)</sup> , `ll` for `long long` and `unsigned long long`.
* If the type of `val` is a floating-point type, the first applicable choice of the following is selected:
rev|until=c++11|
:* If `1=floatfield == std::ios_base::fixed`, will use conversion specifier `%f`.
rev|since=c++11|
:* If `1=floatfield == std::ios_base::fixed && !uppercase`, will use conversion specifier `%f`.
:* If `1=floatfield == std::ios_base::fixed`, will use conversion specifier `%F`.
:* If `1=floatfield == std::ios_base::scientific && !uppercase`, will use conversion specifier `%e`.
:* If `1=floatfield == std::ios_base::scientific`, will use conversion specifier `%E`.
rrev|since=c++11|
:* If `1=floatfield == (std::ios_base::fixed , will use conversion specifier `%a`.
:* If `1=floatfield == (std::ios_base::fixed , will use conversion specifier `%A`.
:* If `1=!uppercase`, will use conversion specifier `%g`.
:* Otherwise, will use conversion specifier `%G`.
: Also:
:* If the type of `val` is `long double`, the length modifier `L` is added to the conversion specifier.
:* If the type of `val` is a floating-point type <sup>(since C++11)</sup> and `1=floatfield != (ios_base::fixed , the precision modifier is added and set to `str.precision()`. Otherwise, no precision is specified.
* For both integer and floating-point types, if `showpos` is set, the modifier `+` is prepended.
* For integer types, if `showbase` is set, the modifier `#` is prepended.
* For floating-point types, if `showpoint` is set, the modifier `#` is prepended.
* If the type of `val` is `void*`, will use conversion specifier `%p`
* A narrow character string is created as if by a call to `std::printf(spec, val)` in the "C" locale, where `spec` is the chosen conversion specifier.

### Stage 2: locale-specific conversion

* Every character `c` obtained in Stage 1, other than the decimal point `'.'`, is converted to `CharT` by calling `std::use_facet<std::ctype<CharT>>(str.getloc()).widen(c)`.
* For arithmetic types, the thousands separator character, obtained from `std::use_facet<std::numpunct<CharT>>(str.getloc()).thousands_sep()`, is inserted into the sequence according to the grouping rules provided by `std::use_facet<std::numpunct<CharT>>(str.getloc()).grouping()`.
* Decimal point characters (`'.'`) are replaced by `std::use_facet<std::numpunct<CharT>>(str.getloc()).decimal_point()`.

### Stage 3: padding

* The adjustment flag is obtained as if by `1=std::fmtflags adjustfield = (flags & (std::ios_base::adjustfield))` and examined to identify padding location, as follows:
** If `1=adjustfield == std::ios_base::left`, will pad after.
** If `1=adjustfield == std::ios_base::right`, will pad before.
** If `1=adjustfield == std::ios_base::internal` and a sign character occurs in the representation, will pad after the sign.
** If `1=adjustfield == std::ios_base::internal` and Stage 1 representation began with 0x or 0X, will pad after the x or X.
** Otherwise, will pad before.
* If `str.width()` is non-zero (e.g. `std::setw` was just used) and the number of `CharT`'s after Stage 2 is less than `str.width()`, then copies of the `fill` character are inserted at the position indicated by padding to bring the length of the sequence to `str.width()`.
In any case, `str.width(0)` is called to cancel the effects of `std::setw`.

### Stage 4: output

Every successive character `c` from the sequence of `CharT`'s from Stage 3 is output as if by `1=*out++ = c`.

## Parameters


### Parameters

- `out` - iterator pointing to the first character to be overwritten
- `str` - stream to retrieve the formatting information from
- `fill` - padding character used when the results needs to be padded to the field width
- `val` - value to convert to string and output

## Return value

`out`

## Notes

The leading zero generated by the conversion specification `#o` (resulting from the combination of `std::showbase` and `std::oct` for example) is not counted as a padding character.
rrev|since=c++11|1=
When formatting a floating point value as hexfloat (i.e., when `1=floatfield == (std::ios_base::fixed ), the stream's precision is not used; instead, the number is always printed with enough precision to exactly represent the value.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

// this custom num_put outputs squares of all integers (except long long)
struct squaring_num_put : std::num_put<char>
{
    iter_type do_put(iter_type out, std::ios_base& str,
                     char_type fill, long val) const
    {
        return std::num_put<char>::do_put(out, str, fill, val * val);
    }

    iter_type do_put(iter_type out, std::ios_base& str,
                     char_type fill, unsigned long val) const
    {
        return std::num_put<char>::do_put(out, str, fill, val * val);
    }
};

int main()
{
    auto& facet = std::use_facet<std::num_put<char>>(std::locale());
    facet.put(std::cout, std::cout, '0', 2.71);
    std::cout << '\n';

    std::cout.imbue(std::locale(std::cout.getloc(), new squaring_num_put));
    std::cout << 6 << ' ' << -12 << '\n';
}
```


**Output:**
```
2.71
36 144
```

|code=
#include <iostream>
#include <iterator>
#include <locale>
struct base { long x = 10; };
template<class CharT, class Traits>
std::basic_ostream<CharT, Traits>&
operator<<(std::basic_ostream<CharT, Traits>& os, const base& b)
{
try
{
typename std::basic_ostream<CharT, Traits>::sentry s(os);
if (s)
{
std::ostreambuf_iterator<CharT, Traits> it(os);
std::use_facet<std::num_put<CharT>>(os.getloc())
.put(it, os, os.fill(), b.x);
}
}
catch (...)
{
// set badbit on os and rethrow if required
}
return os;
}
int main()
{
base b;
std::cout << b;
}
|output=
10

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-282 | C++98 | the thousand separators were only<br>inserted for integral types in stage 2 | also inserted for<br>floating-point types |


## See also


| cpp/io/basic_ostream/dsc operator ltlt | (see dedicated page) |

