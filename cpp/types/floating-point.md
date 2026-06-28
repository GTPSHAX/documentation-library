---
title: Fixed width floating-point types
type: Utilities
source: https://en.cppreference.com/w/cpp/types/floating-point
---


# Fixed width floating-point types mark since c++23

If the implementation supports any of the following [IEEE 754|ISO 60559](https://en.wikipedia.org/wiki/IEEE 754|ISO 60559) types as an extended floating-point type, then:
* the corresponding macro is defined as `1` to indicate support,
* the corresponding floating-point literal suffix is available, and
* the corresponding type alias name is provided:


| - |
| rowspan=2 | '''Types'''<br>Defined in header<br>header | stdfloat |
| rowspan=2 style="width: 15%;" | Literal suffix |
| rowspan=2 | Predefined macro |
| rowspan=2 | C language type |
| colspan=4 | Type properties |
| - |
| bits of storage |
| bits of precision |
| bits of exponent |
| max exponent |
| - |
| lc | float16_t |
| c | f16 or c | F16 |
| c | __STDCPP_FLOAT16_T__ |
| tt | _Float16 |
| 16 |
| 11 |
| 5 |
| 15 |
| - |
| lc | float32_t |
| c | f32 or c | F32 |
| c | __STDCPP_FLOAT32_T__ |
| tt | _Float32 |
| 32 |
| 24 |
| 8 |
| 127 |
| - |
| lc | float64_t |
| c | f64 or c | F64 |
| c | __STDCPP_FLOAT64_T__ |
| tt | _Float64 |
| 64 |
| 53 |
| 11 |
| 1023 |
| - |
| lc | float128_t |
| c | f128 or c | F128 |
| c | __STDCPP_FLOAT128_T__ |
| tt | _Float128 |
| 128 |
| 113 |
| 15 |
| 16383 |
| - |
| lc | bfloat16_t |
| c | bf16 or c | BF16 |
| c | __STDCPP_BFLOAT16_T__ |
| (N/A) |
| 16 |
| 8 |
| 8 |
| 127 |


## Notes

The type `std::bfloat16_t` is known as [Bfloat16 floating-point format|Brain Floating-Point](https://en.wikipedia.org/wiki/Bfloat16 floating-point format|Brain Floating-Point).
Unlike the fixed width integer types, which may be aliases to standard integer types, the fixed width floating-point types must be aliases to extended floating-point types (not `float` / `double` / `long double`), therefore not drop-in replacements for standard floating-point types.

## Example


### Example

```cpp
#include <stdfloat>

#if __STDCPP_FLOAT64_T__ != 1
    #error "64-bit float type required"
#endif

int main()
{
    std::float64_t f = 0.1f64;
}
```


## References


## See also

* Fundamental types
