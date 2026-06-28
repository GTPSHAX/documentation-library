---
title: std::ranges::unique_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/unique_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<I, Proj>>
C = ranges::equal_to >
requires std::indirectly_copyable<I, O> && (std::forward_iterator<I>
(std::input_iterator<O> && std::same_as<std::iter_value_t<I>,
std::iter_value_t<O>>)  std::indirectly_copyable_storable<I, O>)
constexpr unique_copy_result<I, O>
unique_copy( I first, S last, O result, C comp = {}, Proj proj = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<ranges::iterator_t<R>,
Proj>> C = ranges::equal_to >
requires std::indirectly_copyable<ranges::iterator_t<R>, O> &&
(std::forward_iterator<ranges::iterator_t<R>>
(std::input_iterator<O> && std::same_as<ranges::range_value_t<R>,
std::iter_value_t<O>>)
std::indirectly_copyable_storable<ranges::iterator_t<R>, O>)
constexpr unique_copy_result<ranges::borrowed_iterator_t<R>, O>
unique_copy( R&& r, O result, C comp = {}, Proj proj = {} );
dcl|num=3|since=c++20|1=
template< class I, class O >
using unique_copy_result = ranges::in_out_result<I, O>;
```

1. Copies the elements from the source range [first, last), to the destination range beginning at `result` in such a way that there are no consecutive equal elements. Only the first element of each group of equal elements is copied.
@@ The ranges [first, last) and [result, result + N) must not overlap. `1= N = ranges::distance(first, last)`.
@@ Two consecutive elements `*(i - 1)` and `*i` are considered equivalent if `1=std::invoke(comp, std::invoke(proj, *(i - 1)), std::invoke(proj, *i)) == true`, where `i` is an iterator in the range [first + 1, last).
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to process, range=source)` - 
- `r` - the source range of elements
- `result` - the destination range of elements
- `comp` - the binary predicate to compare the projected elements
- `proj` - the projection to apply to the elements

## Return value

}

## Complexity

Exactly `N - 1` applications of the corresponding predicate `comp` and no more than twice as many applications of any projection `proj`.

## Possible implementation

See also the implementations in [https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1198-L1276 libstdc++] and [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4022-L4113 MSVC STL] (and third-party libraries: [https://github.com/CaseyCarter/cmcstl2/blob/master/include/stl2/detail/algorithm/unique_copy.hpp cmcstl2], [https://github.com/tcbrindle/NanoRange/blob/master/include/nanorange/algorithm/unique_copy.hpp NanoRange], and [https://github.com/ericniebler/range-v3/blob/master/include/range/v3/algorithm/unique_copy.hpp range-v3]).
eq fun|1=
struct unique_copy_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<I,
Proj>> C = ranges::equal_to>
requires std::indirectly_copyable<I, O> && (std::forward_iterator<I>
(std::input_iterator<O> && std::same_as<std::iter_value_t<I>,
std::iter_value_t<O>>)  std::indirectly_copyable_storable<I, O>)
constexpr ranges::unique_copy_result<I, O>
operator()(I first, S last, O result, C comp = {}, Proj proj = {}) const
{
if (!(first == last))
{
std::iter_value_t<I> value = *first;
*result = value;
++result;
while (!(++first == last))
{
auto&& value2 = *first;
if (!std::invoke(comp, std::invoke(proj, value2),
std::invoke(proj, value)))
{
value = std::forward<decltype(value2)>(value2);
*result = value;
++result;
}
}
}
return {std::move(first), std::move(result)};
}
template<ranges::input_range R, std::weakly_incrementable O,
class Proj = std::identity,
std::indirect_equivalence_relation<std::projected<ranges::iterator_t<R>,
Proj>> C = ranges::equal_to>
requires std::indirectly_copyable<ranges::iterator_t<R>, O> &&
(std::forward_iterator<ranges::iterator_t<R>>
(std::input_iterator<O> && std::same_as<ranges::range_value_t<R>,
std::iter_value_t<O>>)
std::indirectly_copyable_storable<ranges::iterator_t<R>, O>)
constexpr ranges::unique_copy_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result, C comp = {}, Proj proj = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result),
std::move(comp), std::move(proj));
}
};
inline constexpr unique_copy_fn unique_copy {};

## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <list>
#include <string>
#include <type_traits>

void print(const auto& rem, const auto& v)
{
    using V = std::remove_cvref_t<decltype(v)>;
    constexpr bool sep{std::is_same_v<typename V::value_type, int>};
    std::cout << rem << std::showpos;
    for (const auto& e : v)
        std::cout << e << (sep ? " " : "");
    std::cout << '\n';
}

int main()
{
    std::string s1{"The      string    with many       spaces!"};
    print("s1: ", s1);

    std::string s2;
    std::ranges::unique_copy(
        s1.begin(), s1.end(), std::back_inserter(s2),
        [](char c1, char c2) { return c1 == ' ' && c2 == ' '; }
    );
    print("s2: ", s2);

    const auto v1 = {-1, +1, +2, -2, -3, +3, -3};
    print("v1: ", v1);
    std::list<int> v2;
    std::ranges::unique_copy(
        v1, std::back_inserter(v2),
        {}, // default comparator std::ranges::equal_to
        [](int x) { return std::abs(x); } // projection
    );
    print("v2: ", v2);
}
```


**Output:**
```
s1: The      string    with many       spaces!
s2: The string with many spaces!
v1: -1 +1 +2 -2 -3 +3 -3 
v2: -1 +2 -3
```


## See also


| cpp/algorithm/ranges/dsc unique | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc unique_copy | (see dedicated page) |

