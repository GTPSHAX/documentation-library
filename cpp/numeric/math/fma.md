---
title: std::fma
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fma
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
float       fma ( float x, float y, float z );
double      fma ( double x, double y, double z );
long double fma ( long double x, long double y, long double z );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
fma ( /* floating-point-type */ x,
/* floating-point-type */ y,
/* floating-point-type */ z );
dcla|anchor=no|num=2|since=c++11|constexpr=c++23|
float       fmaf( float x, float y, float z );
dcla|anchor=no|num=3|since=c++11|constexpr=c++23|
long double fmal( long double x, long double y, long double z );
dcl|num=4|since=c++11|
#define FP_FAST_FMA  /* implementation-defined */
dcl|num=5|since=c++11|
#define FP_FAST_FMAF /* implementation-defined */
dcl|num=6|since=c++11|
#define FP_FAST_FMAL /* implementation-defined */
**Header:** `<`cmath`>`
dcla|anchor=no|num=A|since=c++11|constexpr=c++23|
template< class Arithmetic1, class Arithmetic2, class Arithmetic3 >
/* common-floating-point-type */
fma( Arithmetic1 x, Arithmetic2 y, Arithmetic3 z );
```

@1-3@ Computes `x * y + z` as if to infinite precision and rounded only once to fit the result type.<sup>(since C++23)</sup>  The library provides overloads of `std::fma` for all cv-unqualified floating-point types as the type of the parameters `x`, `y` and `z`.
@4-6@ If the macro constants `FP_FAST_FMA`, `FP_FAST_FMAF`, or `FP_FAST_FMAL` are defined, the function `std::fma` evaluates faster (in addition to being more precise) than the expression `x * y + z` for `double`, `float`, and `long double` arguments, respectively. If defined, these macros evaluate to integer `1`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `x, y, z` - floating-point or integer values

## Return value

If successful, returns the value of `x * y + z` as if calculated to infinite precision and rounded once to fit the result type (or, alternatively, calculated as a single ternary floating-point operation).
If a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error due to underflow occurs, the correct value (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If `x` is zero and `y` is infinite or if `x` is infinite and `y` is zero, and
** if `z` is not a NaN, then NaN is returned and `FE_INVALID` is raised,
** if `z` is a NaN, then NaN is returned and `FE_INVALID` may be raised.
* If `x * y` is an exact infinity and `z` is an infinity with the opposite sign, NaN is returned and `FE_INVALID` is raised.
* If `x` or `y` are NaN, NaN is returned.
* If `z` is NaN, and `x * y` is not `0 * Inf` or `Inf * 0`, then NaN is returned (without `FE_INVALID`).

## Notes

This operation is commonly implemented in hardware as [Multiply%E2%80%93accumulate operation|fused multiply-add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate operation|fused multiply-add) CPU instruction. If supported by hardware, the appropriate `FP_FAST_FMA?` macros are expected to be defined, but many implementations make use of the CPU instruction even when the macros are not defined.
POSIX [https://pubs.opengroup.org/onlinepubs/9699919799/functions/fma.html (`fma`, `fmaf`, `fmal`)] additionally specifies that the situations specified to return `FE_INVALID` are domain errors.
Due to its infinite intermediate precision, `std::fma` is a common building block of other correctly-rounded mathematical operations, such as `std::sqrt` or even the division (where not provided by the CPU, e.g. [Itanium](https://en.wikipedia.org/wiki/Itanium)).
As with all floating-point expressions, the expression `x * y + z` may be compiled as a fused multiply-add unless the `cpp/preprocessor/impl|#pragma` `STDC FP_CONTRACT` is off.

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iomanip>
#include <iostream>

#ifndef __GNUC__
#pragma STDC FENV_ACCESS ON
#endif

int main()
{
    // demo the difference between fma and built-in operators
    const double in = 0.1;
    std::cout << "0.1 double is " << std::setprecision(23) << in
              << " (" << std::hexfloat << in << std::defaultfloat << ")\n"
              << "0.1*10 is 1.0000000000000000555112 (0x8.0000000000002p-3), "
              << "or 1.0 if rounded to double\n";

    const double expr_result = 0.1 * 10 - 1;
    const double fma_result = std::fma(0.1, 10, -1);
    std::cout << "0.1 * 10 - 1 = " << expr_result
              << " : 1 subtracted after intermediate rounding\n"
              << "fma(0.1, 10, -1) = " << std::setprecision(6) << fma_result << " ("
              << std::hexfloat << fma_result << std::defaultfloat << ")\n\n";

    // fma is used in double-double arithmetic
    const double high = 0.1 * 10;
    const double low = std::fma(0.1, 10, -high);
    std::cout << "in double-double arithmetic, 0.1 * 10 is representable as "
              << high << " + " << low << "\n\n";

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout << "fma(+Inf, 10, -Inf) = " << std::fma(INFINITY, 10, -INFINITY) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
0.1 double is 0.10000000000000000555112 (0x1.999999999999ap-4)
0.1*10 is 1.0000000000000000555112 (0x8.0000000000002p-3), or 1.0 if rounded to double
0.1 * 10 - 1 = 0 : 1 subtracted after intermediate rounding
fma(0.1, 10, -1) = 5.55112e-17 (0x1p-54)

in double-double arithmetic, 0.1 * 10 is representable as 1 + 5.55112e-17

fma(+Inf, 10, -Inf) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc remainder | (see dedicated page) |
| cpp/numeric/math/dsc remquo | (see dedicated page) |

