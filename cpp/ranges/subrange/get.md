---
title: std::ranges::get(std::ranges::subrange)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/get
---


```cpp
**Header:** `<`ranges`>`
dcla|num=1|since=c++20|1=
template< std::size_t N, class I, class S, ranges::subrange_kind K >
requires ((N == 0 && std::copyable<I>)  N == 1)
constexpr auto get( const ranges::subrange<I, S, K>& r );
dcl|num=2|since=c++20|
template< std::size_t N, class I, class S, ranges::subrange_kind K >
requires (N < 2)
constexpr auto get( ranges::subrange<I, S, K>&& r );
dcl|num=3|since=c++20|
namespace std { using ranges::get; }
```

Provides  support.
1. Obtains the iterator or sentinel from a `subrange` lvalue (or a const rvalue) when `1=N == 0` or `1=N == 1`, respectively.
2. Same as , except that it takes a non-const `subrange` rvalue.
3. Overloads  are imported into namespace `std`, which simplifies their usage and makes every `subrange` with a copyable iterator a pair-like type.

## Parameters


### Parameters

- `r` - a `subrange`

## Return value

@1,2@ If `N` is `0`, returns `r.begin()`. Otherwise (`N` is `1`), returns `r.end()`.

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    std::array a{1, -2, 3, -4};

    std::ranges::subrange sub_a{std::next(a.begin()), std::prev(a.end())};
    std::cout << *std::ranges::get<0>(sub_a) << ' '   // == *(begin(a) + 1)
              << *std::ranges::get<1>(sub_a) << '\n'; // == *(end(a) - 1)

    *std::get<0>(sub_a) = 42; // OK
//  *std::get<2>(sub_a) = 13; // Error: index can only be 0 or 1
}
```


**Output:**
```
-2 -4
```


## Defect reports


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |
| cpp/container/array/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |

