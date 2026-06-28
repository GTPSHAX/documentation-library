---
title: std::make_pair
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/make_pair
---


```cpp
**Header:** `<`utility`>`
dcl rev multi|until1=c++11|dcl1=
template< class T1, class T2 >
std::pair<T1, T2> make_pair( T1 x, T2 y );
|until2=c++20|notes2=<sup>(constexpr C++14)</sup>|dcl2=
template< class T1, class T2 >
std::pair</*V1*/, /*V2*/> make_pair( T1&& x, T2&& y );
|dcl3=
template< class T1, class T2 >
constexpr std::pair<std::unwrap_ref_decay_t<T1>,
std::unwrap_ref_decay_t<T2>>
make_pair( T1&& x, T2&& y );
```

Creates a `std::pair` object, deducing the target type from the types of arguments.
rrev|since=c++11|until=c++20|
Given types `std::decay<T1>::type` as `U1` and `std::decay<T2>::type` as `U2`, the types `/*V1*/` and `/*V2*/` are defined as follows:
* If `U1` is `std::reference_wrapper<X>`, `/*V1*/` is `X&`; otherwise `/*V1*/` is `U1`.
* If `U2` is `std::reference_wrapper<Y>`, `/*V2*/` is `Y&`; otherwise `/*V2*/` is `U2`.

## Parameters


### Parameters

- `x, y` - the values to construct the pair from

## Return value

rev|until=c++11|
`std::pair<T1, T2>(x, y)`
rev|since=c++11|until=c++20|
`std::pair</*V1*/, /*V2*/>(std::forward<T1>(x), std::forward<T2>(y))`
rev|since=c++20|

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <utility>

int main()
{
    int n = 1;
    int a[5] = {1, 2, 3, 4, 5};

    // build a pair from two ints
    auto p1 = std::make_pair(n, a[1]);
    std::cout << "The value of p1 is "
              << '(' << p1.first << ", " << p1.second << ")\n";

    // build a pair from a reference to int and an array (decayed to pointer)
    auto p2 = std::make_pair(std::ref(n), a);
    n = 7;
    std::cout << "The value of p2 is "
              << '(' << p2.first << ", " << *(p2.second + 2) << ")\n";
}
```


**Output:**
```
The value of p1 is (1, 2)
The value of p2 is (7, 3)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-181 | C++98 | the parameter types were const-reference<br>types, which made passing arrays impossible | changed these<br>types to value types |

