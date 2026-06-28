---
title: std::ranges::move
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/move
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|1=
template< std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O >
requires std::indirectly_movable<I, O>
constexpr move_result<I, O>
move( I first, S last, O result );
dcl|since=c++20|num=2|1=
template< ranges::input_range R, std::weakly_incrementable O >
requires std::indirectly_movable<ranges::iterator_t<R>, O>
constexpr move_result<ranges::borrowed_iterator_t<R>, O>
move( R&& r, O result );
dcl|since=c++20|num=3|1=
template< class I, class O >
using move_result = ranges::in_out_result<I, O>;
```

1. Moves the elements in the range, defined by [first, last), to another range beginning at `result`.
The behavior is undefined if `result` is within the range [first, last). In such a case, `ranges::move_backward` may be used instead.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first`, and `ranges::end(r)` as `last`.
The elements in the ''moved-from'' range will still contain valid values of the appropriate type, but not necessarily the same values as before the move.

## Parameters


### Parameters

- `[3=to move, sentinel=yes}})` - 
- `r` - the range of the elements to move
- `result` - the beginning of the destination range

## Return value

}, where
1. `1=N = ranges::distance(first, last)`.
2. `1=N = ranges::distance(r)`.

## Complexity

Exactly `N` move assignments.

## Notes

When moving overlapping ranges, `ranges::move` is appropriate when moving to the left (beginning of the destination range is outside the source range) while `ranges::move_backward` is appropriate when moving to the right (end of the destination range is outside the source range).

## Possible implementation

eq fun|1=
struct move_fn
{
template<std::input_iterator I, std::sentinel_for<I> S, std::weakly_incrementable O>
requires std::indirectly_movable<I, O>
constexpr ranges::move_result<I, O>
operator()(I first, S last, O result) const
{
for (; first != last; ++first, ++result)
*result = ranges::iter_move(first);
return {std::move(first), std::move(result)};
}
template<ranges::input_range R, std::weakly_incrementable O>
requires std::indirectly_movable<ranges::iterator_t<R>, O>
constexpr ranges::move_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result));
}
};
inline constexpr move_fn move {};

## Example


### Example

```cpp
#include <algorithm>
#include <chrono>
#include <iostream>
#include <iterator>
#include <list>
#include <thread>
#include <vector>
using namespace std::literals::chrono_literals;

void f(std::chrono::milliseconds n)
{
    std::this_thread::sleep_for(n);
    std::cout << "thread with n=" << n.count() << "ms ended" << std::endl;
}

int main()
{
    std::vector<std::jthread> v;
    v.emplace_back(f, 400ms);
    v.emplace_back(f, 600ms);
    v.emplace_back(f, 800ms);

    std::list<std::jthread> l;

    // std::ranges::copy() would not compile, because std::jthread is non-copyable
    std::ranges::move(v, std::back_inserter(l));
}
```


**Output:**
```
thread with n=400ms ended
thread with n=600ms ended
thread with n=800ms ended
```


## See also


| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/dsc move | (see dedicated page) |
| cpp/utility/dsc move | (see dedicated page) |

