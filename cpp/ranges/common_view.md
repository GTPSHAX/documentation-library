---
title: std::ranges::views::common
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< ranges::view V >
requires (not ranges::common_range<V> and
std::copyable<ranges::iterator_t<V>>)
class common_view
: public ranges::view_interface<common_view<V>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ common = /* unspecified */;
}
dcl|since=c++20|1=
template< ranges::viewable_range R >
requires /* see below */
constexpr ranges::view auto common( R&& r );
```

1. Adapts a given  with different types for iterator/sentinel pair into a  that is also a . A `common_view` always has the same iterator/sentinel type.
2. *RangeAdaptorObject*. Let `e` be a subexpression. Then the expression `views::common(e)` is expression-equivalent to:
* `views::all(e)`, if it is a well-formed expression and `decltype((e))` models ;
* } otherwise.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|common_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|common_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|common_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|common_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|common_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc reserve_hint|common_view | (see dedicated page) |


## 


## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::common_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `common_view` satisfy  when the underlying view satisfies it.

## Notes

`common_view` can be useful for working with legacy algorithms that expect the iterator and sentinel are of the same type.

## Example


### Example

```cpp
#include <initializer_list>
#include <iostream>
#include <iterator>
#include <list>
#include <numeric>
#include <ranges>

int main()
{
    auto v1 = {1, 2, 3, 4, 5};
    auto i1 = std::counted_iterator{v1.begin(), std::ssize(v1)};
    auto r1 = std::ranges::subrange{i1, std::default_sentinel};
//  auto e1 = std::accumulate(r1.begin(), r1.end(), 0); // error: "common range" required
    auto c1 = std::ranges::common_view{r1};
    std::cout << "accumulate: " << std::accumulate(c1.begin(), c1.end(), 0) << '\n';

    // inherited from ranges::view_interface:
    std::cout << "c1.front(): " << c1.front() << '\n';
    std::cout << "c1.back(): " << c1.back() << '\n';
    std::cout << "c1.data(): " << c1.data() << '\n';
    std::cout << "c1[0]: " << c1[0] << '\n';

    auto v2 = std::list{1, 2, 3, 4, 5};
    auto i2 = std::counted_iterator{v2.begin(), std::ssize(v2)};
    auto r2 = std::ranges::subrange{i2, std::default_sentinel};
//  auto e2 = std::accumulate(r2.begin(), r2.end(), 0); // error: "common range" required
    auto c2 = std::ranges::common_view{ r2 };
    std::cout << "accumulate: " << std::accumulate(c2.begin(), c2.end(), 0) << '\n';

    // inherited from ranges::view_interface:
    std::cout << "c2.front(): " << c2.front() << '\n';
//  auto e3 = c2.back(); // error: "bidirectional range" required
//  auto e4 = c2.data(); // error: "contiguous range" required
//  auto e5 = c2[0];     // error: "random access range" required
}
```


**Output:**
```
accumulate: 15
c1.front(): 1
c1.back(): 5
c1.data(): 0x7f19937f00d0
c1[0]: 1
accumulate: 15
c2.front(): 1
```


## Defect reports


## See also


| cpp/ranges/dsc common_range | (see dedicated page) |
| cpp/iterator/dsc common_iterator | (see dedicated page) |

