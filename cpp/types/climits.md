---
title: C numeric limits interface
type: Utilities
source: https://en.cppreference.com/w/cpp/types/climits
---


# C numeric limits interface

See also `std::numeric_limits` interface.

## Characteristics of integer types


#### Characteristics of core language integer types

| climits | |
| cpp/types/dsc BOOL_WIDTH | (see dedicated page) |
| cpp/types/dsc CHAR_BIT | (see dedicated page) |
| cpp/types/dsc MB_LEN_MAX | (see dedicated page) |
| cpp/types/dsc CHAR_WIDTH | (see dedicated page) |
| cpp/types/dsc CHAR_MIN | (see dedicated page) |
| cpp/types/dsc CHAR_MAX | (see dedicated page) |
| cpp/types/dsc signed_WIDTH | (see dedicated page) |
| cpp/types/dsc signed_MIN | (see dedicated page) |
| cpp/types/dsc signed_MAX | (see dedicated page) |
| cpp/types/dsc unsigned_WIDTH | (see dedicated page) |
| cpp/types/dsc unsigned_MAX | (see dedicated page) |
| cwchar | |
| cstdint | |
| cpp/types/dsc WCHAR_WIDTH | (see dedicated page) |
| cpp/types/dsc WCHAR_MIN | (see dedicated page) |
| cpp/types/dsc WCHAR_MAX | (see dedicated page) |

#### Characteristics of library type aliases

| cstdint | |
| cpp/types/dsc PTRDIFF_WIDTH | (see dedicated page) |
| cpp/types/dsc PTRDIFF_MIN | (see dedicated page) |
| cpp/types/dsc PTRDIFF_MAX | (see dedicated page) |
| cpp/types/dsc SIZE_WIDTH | (see dedicated page) |
| cpp/types/dsc SIZE_MAX | (see dedicated page) |
| cpp/types/dsc SIG_ATOMIC_WIDTH | (see dedicated page) |
| cpp/types/dsc SIG_ATOMIC_MIN | (see dedicated page) |
| cpp/types/dsc SIG_ATOMIC_MAX | (see dedicated page) |
| cpp/types/dsc WINT_WIDTH | (see dedicated page) |
| cpp/types/dsc WINT_MIN | (see dedicated page) |
| cpp/types/dsc WINT_MAX | (see dedicated page) |


## Value requirements

rrev|since=c++26|
`BOOL_WIDTH` always expands to `1`.
Each of<sup>(since C++26)</sup>  the `*_WIDTH` macros (other than `BOOL_WIDTH`), `CHAR_BIT` and `MB_LEN_MAX` expands to an implementation-defined value. The allowed minimum values are listed below, where each group of macros separated by / always expand to the same value:
* at least `1`: `MB_LEN_MAX`
* at least `8`: `CHAR_BIT` / `CHAR_WIDTH` / `SCHAR_WIDTH` / `UCHAR_WIDTH`, `WCHAR_WIDTH`, `SIG_ATOMIC_WIDTH`
* at least `16`: `SHRT_WIDTH` / `USHRT_WIDTH`, `INT_WIDTH` / `UINT_WIDTH`, `PTRDIFF_WIDTH`, `SIZE_WIDTH`, `WINT_WIDTH`
* at least `32`: `LONG_WIDTH` / `ULONG_WIDTH`
* at least `64`: `LLONG_WIDTH` / `ULLONG_WIDTH`

### Notes

The types of these constants, other than<sup>(since C++26)</sup>  the `*_WIDTH` macros, `CHAR_BIT` and `MB_LEN_MAX`, are required to match the results of the s as applied to objects of the types they describe: `CHAR_MAX` may have type `int` or `unsigned int`, but never `char`. Similarly `USHRT_MAX` may not be of an unsigned type: its type may be `int`.
A  implementation may lack `std::sig_atomic_t` and/or `std::wint_t` typedef names, in which case the `SIG_ATOMIC_*` and/or `WINT_*` macros are correspondingly absent.

### Example


### Example

```cpp
#include <climits>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <locale>

int main()
{
    constexpr int w = 14;
    (std::cout << std::left).imbue(std::locale("en_US.UTF-8"));
#   define COUT(x) std::cout << std::setw(w) << #x << " = " << x << '\n'

    COUT( BOOL_WIDTH     );
    COUT( CHAR_BIT       );
    COUT( CHAR_MAX       );
    COUT( CHAR_MIN       );
    COUT( CHAR_WIDTH     );
    COUT( INT_MAX        );
    COUT( INT_MIN        );
    COUT( INT_WIDTH      );
    COUT( LLONG_MAX      );
    COUT( LLONG_MIN      );
    COUT( LLONG_WIDTH    );
    COUT( LONG_MAX       );
    COUT( LONG_MIN       );
    COUT( LONG_WIDTH     );
    COUT( MB_LEN_MAX     );
    COUT( PTRDIFF_MAX    );
    COUT( PTRDIFF_MIN    );
    COUT( SCHAR_MAX      );
    COUT( SCHAR_MIN      );
    COUT( SCHAR_WIDTH    );
    COUT( SHRT_MAX       );
    COUT( SHRT_MIN       );
    COUT( SHRT_WIDTH     );
    COUT( SIG_ATOMIC_MAX );
    COUT( SIG_ATOMIC_MIN );
    COUT( SIZE_MAX       );
    COUT( UCHAR_MAX      );
    COUT( UCHAR_WIDTH    );
    COUT( UINT_MAX       );
    COUT( UINT_WIDTH     );
    COUT( ULLONG_MAX     );
    COUT( ULLONG_WIDTH   );
    COUT( ULONG_MAX      );
    COUT( ULONG_WIDTH    );
    COUT( USHRT_MAX      );
    COUT( USHRT_WIDTH    );
    COUT( WCHAR_MAX      );
    COUT( WCHAR_MIN      );
    COUT( WINT_MAX       );
    COUT( WINT_MIN       );
}
```


**Output:**
```
BOOL_WIDTH     = 1
CHAR_BIT       = 8
CHAR_MAX       = 127
CHAR_MIN       = -128
CHAR_WIDTH     = 8
INT_MAX        = 2,147,483,647
INT_MIN        = -2,147,483,648
INT_WIDTH      = 32
LLONG_MAX      = 9,223,372,036,854,775,807
LLONG_MIN      = -9,223,372,036,854,775,808
LLONG_WIDTH    = 64
LONG_MAX       = 9,223,372,036,854,775,807
LONG_MIN       = -9,223,372,036,854,775,808
LONG_WIDTH     = 64
MB_LEN_MAX     = 16
PTRDIFF_MAX    = 9,223,372,036,854,775,807
PTRDIFF_MIN    = -9,223,372,036,854,775,808
SCHAR_MAX      = 127
SCHAR_MIN      = -128
SCHAR_WIDTH    = 8
SHRT_MAX       = 32,767
SHRT_MIN       = -32,768
SHRT_WIDTH     = 16
SIG_ATOMIC_MAX = 2,147,483,647
SIG_ATOMIC_MIN = -2,147,483,648
SIZE_MAX       = 18,446,744,073,709,551,615
UCHAR_MAX      = 255
UCHAR_WIDTH    = 8
UINT_MAX       = 4,294,967,295
UINT_WIDTH     = 32
ULLONG_MAX     = 18,446,744,073,709,551,615
ULLONG_WIDTH   = 64
ULONG_MAX      = 18,446,744,073,709,551,615
ULONG_WIDTH    = 64
USHRT_MAX      = 65,535
USHRT_WIDTH    = 16
WCHAR_MAX      = 2,147,483,647
WCHAR_MIN      = -2,147,483,648
WINT_MAX       = 4,294,967,295
WINT_MIN       = 0
```


## Characteristics and special values of floating-point types


#### Characteristics of floating-point types

| cfloat | |
| cpp/types/dsc FLT_ROUNDS | (see dedicated page) |
| cpp/types/dsc FLT_EVAL_METHOD | (see dedicated page) |
| cpp/types/dsc fp_HAS_SUBNORM | (see dedicated page) |
| cpp/types/dsc FLT_RADIX | (see dedicated page) |
| cpp/types/dsc fp_MANT_DIG | (see dedicated page) |
| cpp/types/dsc fp_DECIMAL_DIG | (see dedicated page) |
| cpp/types/dsc DECIMAL_DIG | (see dedicated page) |
| cpp/types/dsc fp_DIG | (see dedicated page) |
| cpp/types/dsc fp_MIN_EXP | (see dedicated page) |
| cpp/types/dsc fp_MIN_10_EXP | (see dedicated page) |
| cpp/types/dsc fp_MAX_EXP | (see dedicated page) |
| cpp/types/dsc fp_MAX_10_EXP | (see dedicated page) |
| cpp/types/dsc fp_MAX | (see dedicated page) |
| cpp/types/dsc fp_EPSILON | (see dedicated page) |
| cpp/types/dsc fp_MIN | (see dedicated page) |
| cpp/types/dsc fp_TRUE_MIN | (see dedicated page) |

#### Special values of floating-point types

| cmath| | |
| cfloat| | |
| cpp/numeric/math/dsc INFINITY | (see dedicated page) |
| cpp/numeric/math/dsc NAN | (see dedicated page) |
| cfloat | |
| cpp/types/dsc fp_SNAN | (see dedicated page) |


### Example


### Example

```cpp
#include <cfloat>
#include <iomanip>
#include <iostream>

int main()
{
    int w = 16;
    std::cout << std::left; // std::cout << std::setprecision(53);
#   define COUT(x) std::cout << std::setw(w) << #x << " = " << x << '\n'

    COUT( FLT_RADIX        );
    COUT( DECIMAL_DIG      );
    COUT( FLT_DECIMAL_DIG  );
    COUT( DBL_DECIMAL_DIG  );
    COUT( LDBL_DECIMAL_DIG );
    COUT( FLT_MIN          );
    COUT( DBL_MIN          );
    COUT( LDBL_MIN         );
    COUT( FLT_TRUE_MIN     );
    COUT( DBL_TRUE_MIN     );
    COUT( LDBL_TRUE_MIN    );
    COUT( FLT_MAX          );
    COUT( DBL_MAX          );
    COUT( LDBL_MAX         );
    COUT( FLT_EPSILON      );
    COUT( DBL_EPSILON      );
    COUT( LDBL_EPSILON     );
    COUT( FLT_DIG          );
    COUT( DBL_DIG          );
    COUT( LDBL_DIG         );
    COUT( FLT_MANT_DIG     );
    COUT( DBL_MANT_DIG     );
    COUT( LDBL_MANT_DIG    );
    COUT( FLT_MIN_EXP      );
    COUT( DBL_MIN_EXP      );
    COUT( LDBL_MIN_EXP     );
    COUT( FLT_MIN_10_EXP   );
    COUT( DBL_MIN_10_EXP   );
    COUT( LDBL_MIN_10_EXP  );
    COUT( FLT_MAX_EXP      );
    COUT( DBL_MAX_EXP      );
    COUT( LDBL_MAX_EXP     );
    COUT( FLT_MAX_10_EXP   );
    COUT( DBL_MAX_10_EXP   );
    COUT( LDBL_MAX_10_EXP  );
    COUT( FLT_ROUNDS       );
    COUT( FLT_EVAL_METHOD  );
    COUT( FLT_HAS_SUBNORM  );
    COUT( DBL_HAS_SUBNORM  );
    COUT( LDBL_HAS_SUBNORM );
}
```


**Output:**
```
FLT_RADIX        = 2
DECIMAL_DIG      = 21
FLT_DECIMAL_DIG  = 9
DBL_DECIMAL_DIG  = 17
LDBL_DECIMAL_DIG = 21
FLT_MIN          = 1.17549e-38
DBL_MIN          = 2.22507e-308
LDBL_MIN         = 3.3621e-4932
FLT_TRUE_MIN     = 1.4013e-45
DBL_TRUE_MIN     = 4.94066e-324
LDBL_TRUE_MIN    = 3.6452e-4951
FLT_MAX          = 3.40282e+38
DBL_MAX          = 1.79769e+308
LDBL_MAX         = 1.18973e+4932
FLT_EPSILON      = 1.19209e-07
DBL_EPSILON      = 2.22045e-16
LDBL_EPSILON     = 1.0842e-19
FLT_DIG          = 6
DBL_DIG          = 15
LDBL_DIG         = 18
FLT_MANT_DIG     = 24
DBL_MANT_DIG     = 53
LDBL_MANT_DIG    = 64
FLT_MIN_EXP      = -125
DBL_MIN_EXP      = -1021
LDBL_MIN_EXP     = -16381
FLT_MIN_10_EXP   = -37
DBL_MIN_10_EXP   = -307
LDBL_MIN_10_EXP  = -4931
FLT_MAX_EXP      = 128
DBL_MAX_EXP      = 1024
LDBL_MAX_EXP     = 16384
FLT_MAX_10_EXP   = 38
DBL_MAX_10_EXP   = 308
LDBL_MAX_10_EXP  = 4932
FLT_ROUNDS       = 1
FLT_EVAL_METHOD  = 0
FLT_HAS_SUBNORM  = 1
DBL_HAS_SUBNORM  = 1
LDBL_HAS_SUBNORM = 1
```


## Defect reports


## See also

* Fixed width integer types
* Arithmetic types
* C++ type system overview
* Type support (basic types, RTTI, type traits)
