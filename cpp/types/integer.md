---
title: Fixed width integer types
type: Utilities
source: https://en.cppreference.com/w/cpp/types/integer
---


# Fixed width integer types mark since c++11


## Types

For each of the following typedef names marked , an implementation defines it if and only if the implementation provides a corresponding type.


| cstdint | |
| cpp/types/dsc intN_t | (see dedicated page) |
| cpp/types/dsc int_fastN_t | (see dedicated page) |
| cpp/types/dsc int_leastN_t | (see dedicated page) |
| cpp/types/dsc intmax_t | (see dedicated page) |
| cpp/types/dsc intptr_t | (see dedicated page) |
| cpp/types/dsc uintN_t | (see dedicated page) |
| cpp/types/dsc uint_fastN_t | (see dedicated page) |
| cpp/types/dsc uint_leastN_t | (see dedicated page) |
| cpp/types/dsc uintmax_t | (see dedicated page) |
| cpp/types/dsc uintptr_t | (see dedicated page) |


## Macro constants

For each of the following macros marked , an implementation defines it if and only if the implementation defines the corresponding typedef name.


| cstdint | |

#### Signed integers : bit width

| cpp/types/dsc INTn_WIDTH | (see dedicated page) |
| cpp/types/dsc INT_FASTn_WIDTH | (see dedicated page) |
| cpp/types/dsc INT_LEASTn_WIDTH | (see dedicated page) |
| cpp/types/dsc INTMAX_WIDTH | (see dedicated page) |
| cpp/types/dsc INTPTR_WIDTH | (see dedicated page) |

#### Signed integers : minimum value

| cpp/types/dsc INTn_MIN | (see dedicated page) |
| cpp/types/dsc INT_FASTn_MIN | (see dedicated page) |
| cpp/types/dsc INT_LEASTn_MIN | (see dedicated page) |
| cpp/types/dsc INTMAX_MIN | (see dedicated page) |
| cpp/types/dsc INTPTR_MIN | (see dedicated page) |

#### Signed integers : maximum value

| cpp/types/dsc INTn_MAX | (see dedicated page) |
| cpp/types/dsc INT_FASTn_MAX | (see dedicated page) |
| cpp/types/dsc INT_LEAST8_MAX | (see dedicated page) |
| cpp/types/dsc INTMAX_MAX | (see dedicated page) |
| cpp/types/dsc INTPTR_MAX | (see dedicated page) |

#### Unsigned integers : bit width

| cpp/types/dsc UINTn_WIDTH | (see dedicated page) |
| cpp/types/dsc UINT_FASTn_WIDTH | (see dedicated page) |
| cpp/types/dsc UINT_LEASTn_WIDTH | (see dedicated page) |
| cpp/types/dsc UINTMAX_WIDTH | (see dedicated page) |
| cpp/types/dsc UINTPTR_WIDTH | (see dedicated page) |

#### Unsigned integers : maximum value

| cpp/types/dsc UINTn_MAX | (see dedicated page) |
| cpp/types/dsc UINT_FASTn_MAX | (see dedicated page) |
| cpp/types/dsc UINT_LEASTn_MAX | (see dedicated page) |
| cpp/types/dsc UINTMAX_MAX | (see dedicated page) |
| cpp/types/dsc UINTPTR_MAX | (see dedicated page) |


## Function macros

For each of the following macros marked , an implementation defines it if and only if the implementation defines the corresponding typedef name.


| cstdint | |
| cpp/types/dsc INTn_C | (see dedicated page) |
| cpp/types/dsc INTMAX_C | (see dedicated page) |
| cpp/types/dsc UINTn_C | (see dedicated page) |
| cpp/types/dsc UINTMAX_C | (see dedicated page) |


```cpp
#include <cstdint>
UINT64_C(0x123) // expands to a literal of type uint_least64_t and value 0x123
```


## Format macro constants


| cinttypes | |


### Format constants for the `std::fprintf` family of functions

Each of the `PRI` macros listed here is defined if and only if the implementation defines the corresponding typedef name.


| - |
| rowspan=2 | Equivalent<br>for c/core | int or<br>c/core | unsigned int |
| rowspan=2 | Description |
| colspan=5 | Macros for data types |
| - |
| <br><br><br><br>vertical | tt | std::int'''x'''tt | _t<br><br><br><br> |
| vertical | tt | std::int_least'''x'''lc | _t |
| vertical | tt | std::int_fast'''x'''lc | _t |
| vertical | tt | std::intmax_t |
| vertical | tt | std::intptr_t |
| - |
| tt | d |
| rowspan=2 style="text-align:left;" | output of a signed decimal integer value |
| PRId'''x''' |
| PRIdLEAST'''x''' |
| PRIdFAST'''x''' |
| PRIdMAX |
| PRIdPTR |
| - |
| tt | i |
| PRIi'''x''' |
| PRIiLEAST'''x''' |
| PRIiFAST'''x''' |
| PRIiMAX |
| PRIiPTR |
| - |
| tt | u |
| style="text-align:left;" | output of an unsigned decimal integer value |
| PRIu'''x''' |
| PRIuLEAST'''x''' |
| PRIuFAST'''x''' |
| PRIuMAX |
| PRIuPTR |
| - |
| tt | o |
| style="text-align:left;" | output of an unsigned octal integer value |
| PRIo'''x''' |
| PRIoLEAST'''x''' |
| PRIoFAST'''x''' |
| PRIoMAX |
| PRIoPTR |
| - |
| tt | x |
| style="text-align:left;" | output of an unsigned lowercase hexadecimal integer value |
| PRIx'''x''' |
| PRIxLEAST'''x''' |
| PRIxFAST'''x''' |
| PRIxMAX |
| PRIxPTR |
| - |
| tt | X |
| style="text-align:left;" | output of an unsigned uppercase hexadecimal integer value |
| PRIX'''x''' |
| PRIXLEAST'''x''' |
| PRIXFAST'''x''' |
| PRIXMAX |
| PRIXPTR |


### Format constants for the `std::fscanf` family of functions

Each of the `SCN` macros listed in here is defined if and only if the implementation defines the corresponding typedef name and has a suitable `std::fscanf` length modifier for the type.


| - |
| rowspan=2 | Equivalent<br>for c/core | int or<br>c/core | unsigned int |
| rowspan=2 | Description |
| colspan=5 | Macros for data types |
| - |
| <br><br><br><br>vertical | tt | std::int'''x'''tt | _t<br><br><br><br> |
| vertical | tt | std::int_least'''x'''lc | _t |
| vertical | tt | std::int_fast'''x'''lc | _t |
| vertical | tt | std::intmax_t |
| vertical | tt | std::intptr_t |
| - |
| tt | d |
| style="text-align:left;" | input of a signed decimal integer value |
| SCNd'''x''' |
| SCNdLEAST'''x''' |
| SCNdFAST'''x''' |
| SCNdMAX |
| SCNdPTR |
| - |
| tt | i |
| style="text-align:left;" | input of a signed integer value |
| SCNi'''x''' |
| SCNiLEAST'''x''' |
| SCNiFAST'''x''' |
| SCNiMAX |
| SCNiPTR |
| - |
| tt | u |
| style="text-align:left;" | input of an unsigned decimal integer value |
| SCNu'''x''' |
| SCNuLEAST'''x''' |
| SCNuFAST'''x''' |
| SCNuMAX |
| SCNuPTR |
| - |
| tt | o |
| style="text-align:left;" | input of an unsigned octal integer value |
| SCNo'''x''' |
| SCNoLEAST'''x''' |
| SCNoFAST'''x''' |
| SCNoMAX |
| SCNoPTR |
| - |
| tt | x |
| style="text-align:left;" | input of an unsigned hexadecimal integer value |
| SCNx'''x''' |
| SCNxLEAST'''x''' |
| SCNxFAST'''x''' |
| SCNxMAX |
| SCNxPTR |


## Notes

Because C++ interprets a character immediately following a string literal as a user-defined string literal, C code such as `printf("%"PRId64"\n",n);` is invalid C++ and requires a space before `PRId64`.
The C99 standard suggests that C++ implementations should not define the above limit, constant, or format macros unless the macros `__STDC_LIMIT_MACROS`, `__STDC_CONSTANT_MACROS` or `__STDC_FORMAT_MACROS` (respectively) are defined before including the relevant C header (`stdint.h` or `inttypes.h`). This recommendation was not adopted by any C++ standard and was removed in C11. However, some implementations (such as glibc 2.17) try to apply this rule, and it may be necessary to define the `__STDC` macros; C++ compilers may try to work around this by automatically defining them in some circumstances.
`std::int8_t` may be `signed char` and `std::uint8_t` may be `unsigned char`, but neither can be `char` regardless of its signedness (because `char` is not considered a "signed integer type" or "unsigned integer type").

## Example


### Example

```cpp
#include <cinttypes>
#include <cstdio>

int main()
{
    std::printf("%zu\n", sizeof(std::int64_t));
    std::printf("%s\n", PRId64);
    std::printf("%+" PRId64 "\n", INT64_MIN);
    std::printf("%+" PRId64 "\n", INT64_MAX);

    std::int64_t n = 7;
    std::printf("%+" PRId64 "\n", n);
}
```


**Output:**
```
8
lld
-9223372036854775808
+9223372036854775807
+7
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2820 | C++11 | the requirements for optional typedef names and macros were inconsistent with C | made consistent |


## References


## See also

* Fundamental types
