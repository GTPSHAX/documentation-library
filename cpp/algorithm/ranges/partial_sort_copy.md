---
title: std::ranges::partial_sort_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/partial_sort_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I1, std::sentinel_for<I1> S1,
std::random_access_iterator I2, std::sentinel_for<I2> S2,
class Comp = ranges::less, class Proj1 = std::identity,
class Proj2 = std::identity >
requires std::indirectly_copyable<I1, I2> &&
std::sortable<I2, Comp, Proj2> &&
std::indirect_strict_weak_order<Comp, std::projected<I1, Proj1>,
std::projected<I2, Proj2>>
constexpr partial_sort_copy_result<I1, I2>
partial_sort_copy( I1 first, S1 last, I2 result_first, S2 result_last,
Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=2|since=c++20|1=
template< ranges::input_range R1, ranges::random_access_range R2,
class Comp = ranges::less, class Proj1 = std::identity,
class Proj2 = std::identity >
requires std::indirectly_copyable<ranges::iterator_t<R1>, ranges::iterator_t<R2>> &&
std::sortable<ranges::iterator_t<R2>, Comp, Proj2> &&
std::indirect_strict_weak_order<Comp, std::projected<ranges::iterator_t<R1>,
Proj1>, std::projected<ranges::iterator_t<R2>, Proj2>>
constexpr partial_sort_copy_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>>
partial_sort_copy( R1&& r, R2&& result_r,
Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {} );
dcl|num=3|since=c++20|1=
template< class I, class O >
using partial_sort_copy_result = ranges::in_out_result<I, O>;
```

Copies the first `N` elements from the source range [first, last), as if it was partially sorted with respect to `comp` and `proj1`, into the destination range [result_first, result_first + N), where },  is equal to `ranges::distance(first, last)`, and  is equal to `ranges::distance(result_first, result_last)`.
The order of equal elements is ''not'' guaranteed to be preserved.
1. The source range elements are projected using the function object `proj1`, and the destination elements are projected using the function object `proj2`.
2. Same as , but uses `r` as the source range and `result_r` as the destination range, as if using `ranges::begin(r)` as `first`, `ranges::end(r)` as `last`, `ranges::begin(result_r)` as `result_first`, and `ranges::end(result_r)` as `result_last`.

## Parameters


### Parameters

- `[3=to copy from, range=source)` - 
- `r` - the source range to copy from
- `[result_first, result_last)` - 
- `result_r` - the destination range
- `comp` - comparison to apply to the projected elements
- `proj1` - projection to apply to the elements of source range
- `proj2` - projection to apply to the elements of destination range

## Return value

An object equal to }.

## Complexity

At most } comparisons and } projections.

## Possible implementation

eq fun|1=
struct partial_sort_copy_fn
{
template<std::input_iterator I1, std::sentinel_for<I1> S1,
std::random_access_iterator I2, std::sentinel_for<I2> S2,
class Comp = ranges::less, class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_copyable<I1, I2> && std::sortable<I2, Comp, Proj2> &&
std::indirect_strict_weak_order<Comp, std::projected<I1, Proj1>,
std::projected<I2, Proj2>>
constexpr ranges::partial_sort_copy_result<I1, I2>
operator()(I1 first, S1 last, I2 result_first, S2 result_last,
Comp comp = {}, Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
if (result_first == result_last)
return {std::move(ranges::next(std::move(first), std::move(last))),
std::move(result_first)};
auto out_last{result_first};
// copy first N elements
for (; !(first == last or out_last == result_last); ++out_last, ++first)
*out_last = *first;
// convert N copied elements into a max-heap
ranges::make_heap(result_first, out_last, comp, proj2);
// process the rest of the input range (if any), preserving the heap property
for (; first != last; ++first)
{
if (std::invoke(comp, std::invoke(proj1, *first),
std::invoke(proj2, *result_first)))
{
// pop out the biggest item and push in a newly found smaller one
ranges::pop_heap(result_first, out_last, comp, proj2);
*(out_last - 1) = *first;
ranges::push_heap(result_first, out_last, comp, proj2);
}
}
// first N elements in the output range is still
// a heap - convert it into a sorted range
ranges::sort_heap(result_first, out_last, comp, proj2);
return {std::move(first), std::move(out_last)};
}
template<ranges::input_range R1, ranges::random_access_range R2,
class Comp = ranges::less, class Proj1 = std::identity,
class Proj2 = std::identity>
requires std::indirectly_copyable<ranges::iterator_t<R1>, ranges::iterator_t<R2>> &&
std::sortable<ranges::iterator_t<R2>, Comp, Proj2> &&
std::indirect_strict_weak_order<Comp, std::projected<ranges::iterator_t<R1>,
Proj1>, std::projected<ranges::iterator_t<R2>, Proj2>>
constexpr ranges::partial_sort_copy_result<ranges::borrowed_iterator_t<R1>,
ranges::borrowed_iterator_t<R2>>
operator()(R1&& r, R2&& result_r, Comp comp = {},
Proj1 proj1 = {}, Proj2 proj2 = {}) const
{
return (*this)(ranges::begin(r), ranges::end(r),
ranges::begin(result_r), ranges::end(result_r),
std::move(comp), std::move(proj1), std::move(proj2));
}
};
inline constexpr partial_sort_copy_fn partial_sort_copy {};

## Example


### Example

```cpp
#include <algorithm>
#include <forward_list>
#include <functional>
#include <iostream>
#include <ranges>
#include <string_view>
#include <vector>

void print(std::string_view rem, std::ranges::input_range auto const& v)
{
    for (std::cout << rem; const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    const std::forward_list source{4, 2, 5, 1, 3};

    print("Write to the smaller vector in ascending order: ", "");

    std::vector dest1{10, 11, 12};
    print("const source list: ", source);
    print("destination range: ", dest1);
    std::ranges::partial_sort_copy(source, dest1);
    print("partial_sort_copy: ", dest1);

    print("Write to the larger vector in descending order:", "");

    std::vector dest2{10, 11, 12, 13, 14, 15, 16};
    print("const source list: ", source);
    print("destination range: ", dest2);
    std::ranges::partial_sort_copy(source, dest2, std::greater{});
    print("partial_sort_copy: ", dest2);
}
```


**Output:**
```
Write to the smaller vector in ascending order:
const source list: 4 2 5 1 3
destination range: 10 11 12
partial_sort_copy: 1 2 3
Write to the larger vector in descending order:
const source list: 4 2 5 1 3
destination range: 10 11 12 13 14 15 16
partial_sort_copy: 5 4 3 2 1 15 16
```


## See also


| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc partial_sort_copy | (see dedicated page) |

