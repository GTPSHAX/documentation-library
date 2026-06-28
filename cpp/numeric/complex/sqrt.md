---
title: std::sqrt(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/sqrt
---


```cpp
**Header:** `<`complex`>`
dcl|1=
template< class T >
std::complex<T> sqrt( const std::complex<T>& z );
```

Computes the square root of the complex number `z` with a branch cut along the negative real axis.

## Parameters


### Parameters

- `z` - complex number to take the square root of

## Return value

If no errors occur, returns the square root of `z`, in the range of the right half-plane, including the imaginary axis ($[0; +∞)$ along the real axis and $(−∞; +∞)$ along the imaginary axis).

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* The function is continuous onto the branch cut taking into account the sign of imaginary part
* `std::sqrt(std::conj(z))
* If `z` is `(±0,+0)`, the result is `(+0,+0)`
* If `z` is `(x,+∞)`, the result is `(+∞,+∞)` even if x is NaN
* If `z` is `(x,NaN)`, the result is `(NaN,NaN)` (unless x is ±∞) and  `FE_INVALID` may be raised
* If `z` is `(-∞,y)`, the result is `(+0,+∞)` for finite positive y
* If `z` is `(+∞,y)`, the result is `(+∞,+0)` for finite positive y
* If `z` is `(-∞,NaN)`, the result is `(NaN,∞)` (sign of imaginary part unspecified)
* If `z` is `(+∞,NaN)`, the result is `(+∞,NaN)`
* If `z` is `(NaN,y)`, the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`

## Notes

The semantics of this function are intended to be consistent with the C function `c/numeric/complex/csqrt`.

## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::cout << "Square root of -4 is "
              << std::sqrt(std::complex<double>(-4.0, 0.0)) << '\n'
              << "Square root of (-4,-0) is "
              << std::sqrt(std::complex<double>(-4.0, -0.0))
              << " (the other side of the cut)\n";
}
```


**Output:**
```
Square root of -4 is (0,2)
Square root of (-4,-0) is (0,-2) (the other side of the cut)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2597 | C++98 | specification mishandles signed zero imaginary parts | erroneous requirement removed |


## See also


| cpp/numeric/complex/dsc pow | (see dedicated page) |
| cpp/numeric/math/dsc sqrt | (see dedicated page) |
| cpp/numeric/valarray/dsc sqrt | (see dedicated page) |

