---
title: std::numeric_limits
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits
---

ddcl|header=limits|
template< class T > class numeric_limits;
The `std::numeric_limits` class template provides a standardized way to query various properties of arithmetic types (e.g. the largest possible value for type `int` is `std::numeric_limits<int>::max()`).
This information is provided via specializations of the `std::numeric_limits` template. The  makes available specializations for all arithmetic types (only lists the specializations for cv-unqualified arithmetic types):

```cpp
**Header:** `<`limits`>`
dcl|
template<> class numeric_limits<bool>;
dcl|
template<> class numeric_limits<char>;
dcl|
template<> class numeric_limits<signed char>;
dcl|
template<> class numeric_limits<unsigned char>;
dcl|
template<> class numeric_limits<wchar_t>;
dcl|since=c++20|
template<> class numeric_limits<char8_t>;
dcl|since=c++11|
template<> class numeric_limits<char16_t>;
dcl|since=c++11|
template<> class numeric_limits<char32_t>;
dcl|
template<> class numeric_limits<short>;
dcl|
template<> class numeric_limits<unsigned short>;
dcl|
template<> class numeric_limits<int>;
dcl|
template<> class numeric_limits<unsigned int>;
dcl|
template<> class numeric_limits<long>;
dcl|
template<> class numeric_limits<unsigned long>;
dcl|since=c++11|
template<> class numeric_limits<long long>;
dcl|since=c++11|
template<> class numeric_limits<unsigned long long>;
dcl|
template<> class numeric_limits<float>;
dcl|
template<> class numeric_limits<double>;
dcl|
template<> class numeric_limits<long double>;
```

The value of each member of a specialization of `std::numeric_limits` on a cv-qualified type ''cv'' `T` is equal to the value of the corresponding member of the specialization on the unqualified type `T`. For example, `std::numeric_limits<int>::digits` is equal to `std::numeric_limits<const int>::digits`.
Aliases of arithmetic types (such as `std::size_t` or `std::streamsize`) may also be examined with the `std::numeric_limits` type traits.
Non-arithmetic standard types, such as `std::complex<T>` or `std::nullptr_t`, do not have specializations.
rrev|since=c++20|
If the implementation defines any integer-class types, specializations of `std::numeric_limits` must also be provided for them.
Implementations may provide specializations of `std::numeric_limits` for implementation-specific types: e.g. GCC provides `std::numeric_limits<__int128>`. Non-standard libraries may add specializations for library-provided types, e.g. [http://openexr.com/ OpenEXR] provides `std::numeric_limits<half>` for a 16-bit floating-point type.

## Template parameters


### Parameters

- `T` - a type to retrieve numeric properties for

## Member constants


| cpp/types/numeric_limits/dsc is_specialized | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_signed | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_exact | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_infinity | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_signaling_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm_loss | (see dedicated page) |
| cpp/types/numeric_limits/dsc round_style | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_iec559 | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_bounded | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_modulo | (see dedicated page) |
| cpp/types/numeric_limits/dsc digits | (see dedicated page) |
| cpp/types/numeric_limits/dsc digits10 | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_digits10 | (see dedicated page) |
| cpp/types/numeric_limits/dsc radix | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent10 | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent10 | (see dedicated page) |
| cpp/types/numeric_limits/dsc traps | (see dedicated page) |
| cpp/types/numeric_limits/dsc tinyness_before | (see dedicated page) |


## Member functions


| cpp/types/numeric_limits/dsc min | (see dedicated page) |
| cpp/types/numeric_limits/dsc lowest | (see dedicated page) |
| cpp/types/numeric_limits/dsc max | (see dedicated page) |
| cpp/types/numeric_limits/dsc epsilon | (see dedicated page) |
| cpp/types/numeric_limits/dsc round_error | (see dedicated page) |
| cpp/types/numeric_limits/dsc infinity | (see dedicated page) |
| cpp/types/numeric_limits/dsc quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc signaling_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc denorm_min | (see dedicated page) |


## Helper classes


| cpp/types/numeric_limits/dsc float_round_style | (see dedicated page) |
| cpp/types/numeric_limits/dsc float_denorm_style | (see dedicated page) |


## Relationship with C library macro constants


| - |
| rowspan=2 | Specialization<br>tt | std::numeric_limits<T><br>where tt | T is |
| colspan=11 | Members |
| - |
| tt | min() |
| tt | lowest()<br> |
| tt | max() |
| tt | radix |
| - |
| - |
| c/core | bool |
| c | false |
| c | false |
| c | true |
| c | 2 |
| - |
| c/core | char |
| lc | CHAR_MIN |
| lc | CHAR_MIN |
| lc | CHAR_MAX |
| c | 2 |
| - |
| c/core | signed char |
| lc | SCHAR_MIN |
| lc | SCHAR_MIN |
| lc | SCHAR_MAX |
| c | 2 |
| - |
| c/core | unsigned char |
| c | 0 |
| c | 0 |
| lc | UCHAR_MAX |
| c | 2 |
| - |
| c/core | wchar_t |
| lc | WCHAR_MIN |
| lc | WCHAR_MIN |
| lc | WCHAR_MAX |
| c | 2 |
| - |
| c/core | char8_t |
| c | 0 |
| c | 0 |
| lc | UCHAR_MAX |
| c | 2 |
| - |
| c/core | char16_t |
| c | 0 |
| c | 0 |
| lc | UINT_LEAST16_MAX |
| c | 2 |
| - |
| c/core | char32_t |
| c | 0 |
| c | 0 |
| lc | UINT_LEAST32_MAX |
| c | 2 |
| - |
| c/core | short |
| rowspan=2 | lc | SHRT_MIN |
| rowspan=2 | lc | SHRT_MIN |
| rowspan=2 | lc | SHRT_MAX |
| rowspan=2 | c | 2 |
| - |
| c/core | signed short |
| - |
| c/core | unsigned short |
| c | 0 |
| c | 0 |
| lc | USHRT_MAX |
| c | 2 |
| - |
| c/core | int |
| rowspan=2 | lc | INT_MIN |
| rowspan=2 | lc | INT_MIN |
| rowspan=2 | lc | INT_MAX |
| rowspan=2 | c | 2 |
| - |
| c/core | signed int |
| - |
| c/core | unsigned int |
| c | 0 |
| c | 0 |
| lc | UINT_MAX |
| c | 2 |
| - |
| c/core | long |
| rowspan=2 | lc | LONG_MIN |
| rowspan=2 | lc | LONG_MIN |
| rowspan=2 | lc | LONG_MAX |
| rowspan=2 | c | 2 |
| - |
| c/core | signed long |
| - |
| c/core | unsigned long |
| c | 0 |
| c | 0 |
| lc | ULONG_MAX |
| c | 2 |
| - |
| c/core | long long |
| rowspan=2 | lc | LLONG_MIN |
| rowspan=2 | lc | LLONG_MIN |
| rowspan=2 | lc | LLONG_MAX |
| rowspan=2 | c | 2 |
| - |
| c/core | signed long long |
| - |
| c/core | unsigned long long |
| c | 0 |
| c | 0 |
| lc | ULLONG_MAX |
| c | 2 |


| - |
| rowspan=2 | Specialization<br>tt | std::numeric_limits<T><br>where tt | T is |
| colspan=11 | Members |
| - |
| tt | denorm_min() |
| tt | min() |
| tt | lowest()<br> |
| tt | max() |
| tt | epsilon() |
| tt | digits |
| tt | digits10 |
| - |
| - |
| c/core | float |
| lc | FLT_TRUE_MIN |
| lc | FLT_MIN |
| c | -FLT_MAX |
| lc | FLT_MAX |
| lc | FLT_EPSILON |
| lc | FLT_MANT_DIG |
| lc | FLT_DIG |
| - |
| c/core | double |
| lc | DBL_TRUE_MIN |
| lc | DBL_MIN |
| c | -DBL_MAX |
| lc | DBL_MAX |
| lc | DBL_EPSILON |
| lc | DBL_MANT_DIG |
| lc | DBL_DIG |
| - |
| c/core | long double |
| lc | LDBL_TRUE_MIN |
| lc | LDBL_MIN |
| c | -LDBL_MAX |
| lc | LDBL_MAX |
| lc | LDBL_EPSILON |
| lc | LDBL_MANT_DIG |
| lc | LDBL_DIG |


| - |
| rowspan=2 | Specialization<br>tt | std::numeric_limits<T><br>where tt | T is |
| colspan=11 | Members (continue) |
| - |
| tt | min_exponent |
| tt | min_exponent10 |
| tt | max_exponent |
| tt | max_exponent10 |
| tt | radix |
| - |
| - |
| c/core | float |
| lc | FLT_MIN_EXP |
| lc | FLT_MIN_10_EXP |
| lc | FLT_MAX_EXP |
| lc | FLT_MAX_10_EXP |
| lc | FLT_RADIX |
| - |
| c/core | double |
| lc | DBL_MIN_EXP |
| lc | DBL_MIN_10_EXP |
| lc | DBL_MAX_EXP |
| lc | DBL_MAX_10_EXP |
| lc | FLT_RADIX |
| - |
| c/core | long double |
| lc | LDBL_MIN_EXP |
| lc | LDBL_MIN_10_EXP |
| lc | LDBL_MAX_EXP |
| lc | LDBL_MAX_10_EXP |
| lc | FLT_RADIX |


## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main() 
{
    std::cout << "type\t│ lowest()\t│ min()\t\t│ max()\n"
              << "bool\t│ "
              << std::numeric_limits<bool>::lowest() << "\t\t│ "
              << std::numeric_limits<bool>::min() << "\t\t│ "
              << std::numeric_limits<bool>::max() << '\n'
              << "uchar\t│ "
              << +std::numeric_limits<unsigned char>::lowest() << "\t\t│ "
              << +std::numeric_limits<unsigned char>::min() << "\t\t│ "
              << +std::numeric_limits<unsigned char>::max() << '\n'
              << "int\t│ "
              << std::numeric_limits<int>::lowest() << "\t│ "
              << std::numeric_limits<int>::min() << "\t│ "
              << std::numeric_limits<int>::max() << '\n'
              << "float\t│ "
              << std::numeric_limits<float>::lowest() << "\t│ "
              << std::numeric_limits<float>::min() << "\t│ "
              << std::numeric_limits<float>::max() << '\n'
              << "double\t│ "
              << std::numeric_limits<double>::lowest() << "\t│ "
              << std::numeric_limits<double>::min() << "\t│ "
              << std::numeric_limits<double>::max() << '\n';
}
```


**Output:**
```
<nowiki>
type    │ lowest()      │ min()         │ max()
bool    │ 0             │ 0             │ 1
uchar   │ 0             │ 0             │ 255
int     │ -2147483648   │ -2147483648   │ 2147483647
float   │ -3.40282e+38  │ 1.17549e-38   │ 3.40282e+38
double  │ -1.79769e+308 │ 2.22507e-308  │ 1.79769e+308
</nowiki>
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-201 | C++98 | specializations for all fundamental types need to be provided | excluded non-arithmetic types |


## See also

* `Fixed width integer types`
* Arithmetic types
* C++ type system overview
* `Type support (basic types, RTTI, type traits)`
* `C numeric limits interface`
