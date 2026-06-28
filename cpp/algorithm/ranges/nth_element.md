---
title: std::ranges::nth_element
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/nth_element
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::random_access_iterator I, std::sentinel_for<I> S,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<I, Comp, Proj>
constexpr I
nth_element( I first, I nth, S last, Comp comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::random_access_range R,
class Comp = ranges::less, class Proj = std::identity >
requires std::sortable<iterator_t<R>, Comp, Proj>
constexpr ranges::borrowed_iterator_t<R>
nth_element( R&& r, iterator_t<R> nth, Comp comp = {}, Proj proj = {} );
```

Reorders the elements in [first, last) such that:
* The element pointed at by `nth` is changed to whatever element would occur in that position if [first, last) were sorted with respect to `comp` and `proj`.
* All of the elements before this new **`nth`** element are ''less than or equal to'' the elements after the new `nth` element. That is, for every iterator ''i'', ''j'' in the ranges [first, nth), [nth, last) respectively, the expression `std::invoke(comp, std::invoke(proj, *j), std::invoke(proj, *i))` evaluates to `false`.
* If `1=nth == last` then the function has no effect.
1. Elements are compared using the given binary comparison function object `comp` and projection object `proj`.
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to reorder, sentinel=yes}})` - 
- `r` - the range of elements to reorder
- `nth` - the iterator defining the partition point
- `comp` - comparator used to compare the projected elements
- `proj` - projection to apply to the elements

## Return value

1. An iterator equal to `last`.
2. Same as  if `r` is an lvalue or of a  type. Otherwise returns `std::ranges::dangling`.

## Complexity

Linear in `ranges::distance(first, last)` on average.

## Notes

The algorithm used is typically introselect although other selection algorithms with suitable average-case complexity are allowed.

## Possible implementation

See also the implementation in [https://github.com/microsoft/STL/blob/e97bb2b50a12816ce68cc5147b7a3a21fb68bfa3/stl/inc/algorithm#L8896-L8969 msvc stl], [https://github.com/gcc-mirror/gcc/blob/a87819b8f1b890d36a3f05bd9de80be20e9525dd/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L2016-L2044 libstdc++], and libc++: [https://github.com/llvm/llvm-project/blob/ed2d3644abee9535eb07333beb1562a651001281/libcxx/include/__algorithm/ranges_nth_element.h (1)] / [https://github.com/llvm/llvm-project/blob/ed2d364/libcxx/include/__algorithm/nth_element.h (2)].

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <ranges>
#include <string_view>

void print(std::string_view rem, std::ranges::input_range auto const& a)
{
    for (std::cout << rem; const auto e : a)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::array v{5, 6, 4, 3, 2, 6, 7, 9, 3};
    print("Before nth_element: ", v);

    std::ranges::nth_element(v, v.begin() + v.size() / 2);
    print("After nth_element:  ", v);
    std::cout << "The median is: " << v[v.size() / 2] << '\n';

    std::ranges::nth_element(v, v.begin() + 1, std::greater<int>());
    print("After nth_element:  ", v);
    std::cout << "The second largest element is: " << v[1] << '\n';
    std::cout << "The largest element is: " << v[0] << "\n\n";

    using namespace std::literals;
    std::array names
    {
        "Diva"sv, "Cornelius"sv, "Munro"sv, "Rhod"sv,
        "Zorg"sv, "Korben"sv, "Bender"sv, "Leeloo"sv,
    };
    print("Before nth_element: ", names);
    auto fifth_element{std::ranges::next(names.begin(), 4)};
    std::ranges::nth_element(names, fifth_element);
    print("After nth_element:  ", names);
    std::cout << "The 5th element is: " << *fifth_element << '\n';
}
```


**Output:**
```
Before nth_element: 5 6 4 3 2 6 7 9 3 
After nth_element:  2 3 3 4 5 6 6 7 9 
The median is: 5
After nth_element:  9 7 6 6 5 4 3 3 2 
The second largest element is: 7
The largest element is: 9

Before nth_element: Diva Cornelius Munro Rhod Zorg Korben Bender Leeloo 
After nth_element:  Diva Cornelius Bender Korben Leeloo Rhod Munro Zorg 
The 5th element is: Leeloo
```


## See also


| cpp/algorithm/ranges/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/dsc nth_element | (see dedicated page) |

