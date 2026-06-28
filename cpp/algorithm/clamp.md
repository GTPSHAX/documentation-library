---
title: std::clamp
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/clamp
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++17|
template< class T >
constexpr const T& clamp( const T& v, const T& lo, const T& hi );
dcla|num=2|since=c++17|
template< class T, class Compare >
constexpr const T& clamp( const T& v, const T& lo, const T& hi,
Compare comp );
```

If the value of `v` is within , returns `v`; otherwise returns the nearest boundary.
1. Uses <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|} to compare the values.
@@ If `T` is not *LessThanComparable*, the behavior is undefined.
2. Uses the comparison function `comp` to compare the values.
If `lo` is greater than `hi`, the behavior is undefined.

## Parameters


### Parameters

- `v` - the value to clamp
- `lo, hi` - the boundaries to clamp `v` to

## Return value

Reference to `lo` if `v` is less than `lo`, reference to `hi` if `hi` is less than `v`, otherwise reference to `v`.

## Complexity

1. At most two comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
2. At most two applications of the comparison function `comp`.

## Possible implementation

eq impl
|title1=clamp (1)|ver1=1|1=
template<class T>
constexpr const T& clamp(const T& v, const T& lo, const T& hi)
{
return clamp(v, lo, hi, less{});
}
|title2=clamp (2)|ver2=2|2=
template<class T, class Compare>
constexpr const T& clamp(const T& v, const T& lo, const T& hi, Compare comp)
{
return comp(v, lo) ? lo : comp(hi, v) ? hi : v;
}

## Notes

If `v` compares equivalent to either bound, returns a reference to `v`, not the bound.

## Example


### Example

```cpp
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>

int main()
{
    std::cout << "[raw] "
                 "[" << INT8_MIN << ',' << INT8_MAX << "] "
                 "[0," << UINT8_MAX << "]\n";

    for (const int v : {-129, -128, -1, 0, 42, 127, 128, 255, 256})
        std::cout << std::setw(4) << v
                  << std::setw(11) << std::clamp(v, INT8_MIN, INT8_MAX)
                  << std::setw(8) << std::clamp(v, 0, UINT8_MAX) << '\n';
}
```


**Output:**
```
[raw] [-128,127] [0,255]
-129       -128       0
-128       -128       0
  -1         -1       0
   0          0       0
  42         42      42
 127        127     127
 128        127     128
 255        127     255
 256        127     255
```


## See also


| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/dsc max | (see dedicated page) |
| cpp/utility/dsc in_range | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |

