---
title: std::complex
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex
---


```cpp
**Header:** `<`complex`>`
dcl|num=1|1=
template< class T >
class complex;
dcl|num=2|until=c++23|
template<> class complex<float>;
dcl|num=3|until=c++23|
template<> class complex<double>;
dcl|num=4|until=c++23|
template<> class complex<long double>;
```

Specializations of `std::complex` for cv-unqualified <sup>(until C++23)</sup> standard  are <sup>(since C++23)</sup> *TriviallyCopyable* *LiteralType*s for representing and manipulating [complex number](https://en.wikipedia.org/wiki/complex number).

## Template parameters


### Parameters

- `T` - the type of the real and imaginary parts. The behavior is unspecified (and may fail to compile) if `T` is not a cv-unqualified <sup>(until C++23)</sup> standard floating-point type and undefined if `T` is not *NumericType*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/complex/dsc complex | (see dedicated page) |
| cpp/numeric/complex/dsc operator{{= | (see dedicated page) |
| cpp/numeric/complex/dsc real | (see dedicated page) |
| cpp/numeric/complex/dsc imag | (see dedicated page) |
| cpp/numeric/complex/dsc operator_arith | (see dedicated page) |


## Non-member functions


| cpp/numeric/complex/dsc operator_arith2 | (see dedicated page) |
| cpp/numeric/complex/dsc operator_arith3 | (see dedicated page) |
| cpp/numeric/complex/dsc operator_cmp | (see dedicated page) |
| cpp/numeric/complex/dsc operator_ltltgtgt | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc real2 | (see dedicated page) |
| cpp/numeric/complex/dsc imag2 | (see dedicated page) |
| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/complex/dsc arg | (see dedicated page) |
| cpp/numeric/complex/dsc norm | (see dedicated page) |
| cpp/numeric/complex/dsc conj | (see dedicated page) |
| cpp/numeric/complex/dsc proj | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |

#### Exponential functions

| cpp/numeric/complex/dsc exp | (see dedicated page) |
| cpp/numeric/complex/dsc log | (see dedicated page) |
| cpp/numeric/complex/dsc log10 | (see dedicated page) |

#### Power functions

| cpp/numeric/complex/dsc pow | (see dedicated page) |
| cpp/numeric/complex/dsc sqrt | (see dedicated page) |

#### Trigonometric functions

| cpp/numeric/complex/dsc sin | (see dedicated page) |
| cpp/numeric/complex/dsc cos | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |
| cpp/numeric/complex/dsc asin | (see dedicated page) |
| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc atan | (see dedicated page) |

#### Hyperbolic functions

| cpp/numeric/complex/dsc sinh | (see dedicated page) |
| cpp/numeric/complex/dsc cosh | (see dedicated page) |
| cpp/numeric/complex/dsc tanh | (see dedicated page) |
| cpp/numeric/complex/dsc asinh | (see dedicated page) |
| cpp/numeric/complex/dsc acosh | (see dedicated page) |
| cpp/numeric/complex/dsc atanh | (see dedicated page) |


## Helper types


| cpp/numeric/complex/dsc tuple_size | (see dedicated page) |
| cpp/numeric/complex/dsc tuple_element | (see dedicated page) |


## Array-oriented access

For any object `z` of type `std::complex<T>`, `reinterpret_cast<T(&)[2]>(z)[0]` is the real part of `z` and `reinterpret_cast<T(&)[2]>(z)[1]` is the imaginary part of `z`.
For any pointer to an element of an array of `std::complex<T>` named `p` and any valid array index `i`, `reinterpret_cast<T*>(p)[2 * i]` is the real part of the complex number `p[i]`, and `reinterpret_cast<T*>(p)[2 * i + 1]` is the imaginary part of the complex number `p[i]`.
The intent of this requirement is to preserve binary compatibility between the C++ library complex number types and the C language complex number types (and arrays thereof), which have an identical object representation requirement.

## Implementation notes

In order to satisfy the requirements of array-oriented access, an implementation is constrained to store the real and imaginary parts of a `std::complex` specialization in separate and adjacent memory locations. Possible declarations for its non-static data members include:
* an array of type `value_type[2]`, with the first element holding the real part and the second element holding the imaginary part (e.g. Microsoft Visual Studio);
* a single member of type `value_type _Complex` (encapsulating the corresponding C language complex number type) (e.g. GNU libstdc++);
* two members of type `value_type`, with the same member access, holding the real and the imaginary parts respectively (e.g. LLVM libc++).
An implementation cannot declare additional non-static data members that would occupy storage disjoint from the real and imaginary parts, and must ensure that the class template specialization does not contain any padding bit. The implementation must also ensure that optimizations to array access account for the possibility that a pointer to `value_type` may be aliasing a `std::complex` specialization or array thereof.

## Literals


| std::literals::complex_literals|inline=true | |
| cpp/numeric/dsc operator""i | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iomanip>
#include <iostream>
#include <ranges>

int main()
{
    using namespace std::complex_literals;
    std::cout << std::fixed << std::setprecision(1);

    std::complex<double> z1 = 1i * 1i; // imaginary unit squared
    std::cout << "i * i = " << z1 << '\n';

    std::complex<double> z2 = std::pow(1i, 2); // imaginary unit squared
    std::cout << "pow(i, 2) = " << z2 << '\n';

    const double PI = std::acos(-1); // or std::numbers::pi in C++20
    std::complex<double> z3 = std::exp(1i * PI); // Euler's formula
    std::cout << "exp(i * pi) = " << z3 << '\n';

    std::complex<double> z4 = 1.0 + 2i, z5 = 1.0 - 2i; // conjugates
    std::cout << "(1 + 2i) * (1 - 2i) = " << z4 * z5 << '\n';

    const auto zz = {0.0 + 1i, 2.0 + 3i, 4.0 + 5i};
#if __cpp_lib_tuple_like >= 202311L
    for (double re : zz {{!
```

std::cout << re << ' ';
std::cout << '\n';
for (double im : zz | std::views::values)
std::cout << im << ' ';
std::cout << '\n';
#else
for (double re : zz | std::views::transform([](auto z){ return z.real(); }))
std::cout << re << ' ';
std::cout << '\n';
for (double im : zz | std::views::transform([](auto z){ return z.imag(); }))
std::cout << im << ' ';
std::cout << '\n';
#endif
}
|output=
i * i = (-1.0,0.0)
pow(i, 2) = (-1.0,0.0)
exp(i * pi) = (-1.0,0.0)
(1 + 2i) * (1 - 2i) = (5.0,0.0)
0.0 2.0 4.0
1.0 3.0 5.0

## Defect reports


## See also

