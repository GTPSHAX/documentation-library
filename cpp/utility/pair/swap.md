---
title: std::pair::swap
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/swap
---


```cpp
dcla|num=1
|since=c++11|constexpr=c++20|
void swap( pair& other ) noexcept(/* see below */);
dcl|num=2
|since=c++23|
constexpr void swap( const pair& other ) const noexcept(/* see below */);
```

Swaps `first` with `other.first` and `second` with `other.second`, as if by `using std::swap; swap(first, other.first); swap(second, other.second);`.
rrev multi
|rev1=
If either selected `swap` function call is ill-formed or does not swap the value of the member, the behavior is undefined.
|since2=c++23|rev2=
1. The program is ill-formed if either `std::is_swappable_v<T1>` or `std::is_swappable_v<T2>` is not `true`.
2. The program is ill-formed if either `std::is_swappable_v<const T1>` or `std::is_swappable_v<const T2>` is not `true`.
If either selected `swap` function call does not swap the value of the member, the behavior is undefined.

## Parameters


### Parameters

- `other` - pair of values to swap

## Exceptions

rrev multi|until1=c++17
|rev1=
noexcept|
noexcept(swap(first, other.first)) &&
noexcept(swap(second, other.second))
In the expression above, the identifier `swap` is looked up in the same manner as the one used by the C++17 `std::is_nothrow_swappable` trait.
|rev2=
1. noexcept|
std::is_nothrow_swappable_v<first_type> &&
std::is_nothrow_swappable_v<second_type>
2. noexcept|
std::is_nothrow_swappable_v<const first_type> &&
std::is_nothrow_swappable_v<const second_type>

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <utility>

int main()
{
    std::pair<int, std::string> p1(10, "test"), p2;
    p2.swap(p1);
    std::cout << "(" << p2.first << ", " << p2.second << ")\n";

#if __cpp_lib_ranges_zip >= 202110L
    // Using the C++23 const qualified swap overload
    // (swap is no longer propagating pair constness)
    int i1 = 10, i2{};
    std::string s1("test"), s2;
    const std::pair<int&, std::string&> r1(i1, s1), r2(i2, s2);
    r2.swap(r1);
    std::cout << "(" << i2 << ", " << s2 << ")\n";
#endif
}
```


**Output:**
```
(10, test)
(10, test)
```


## Defect reports


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/utility/tuple/dsc swap | (see dedicated page) |

