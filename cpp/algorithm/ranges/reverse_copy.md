---
title: std::ranges::reverse_copy
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/reverse_copy
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::bidirectional_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O >
requires std::indirectly_copyable<I, O>
constexpr reverse_copy_result<I, O>
reverse_copy( I first, S last, O result );
dcl|num=2|since=c++20|1=
template< ranges::bidirectional_range R, std::weakly_incrementable O >
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr reverse_copy_result<ranges::borrowed_iterator_t<R>, O>
reverse_copy( R&& r, O result );
dcl|num=3|since=c++20|1=
template< class I, class O >
using reverse_copy_result = ranges::in_out_result<I, O>;
```

1. Copies the elements from the source range [first, last) to the destination range [result, result + N), where `N` is `ranges::distance(first, last)`, in such a way that the elements in the new range are in reverse order. Behaves as if by executing the assignment `1=*(result + N - 1 - i) = *(first + i)` once for each integer `i` in [0, N). The behavior is undefined if the source and destination ranges overlap.
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to copy, range=source)` - 
- `r` - the source range of elements to copy
- `result` - the beginning of the destination range.

## Return value

}.

## Complexity

Exactly `N` assignments.

## Notes

Implementations (e.g. [https://github.com/microsoft/STL/blob/main/stl/src/vector_algorithms.cpp MSVC STL]) may enable vectorization when the both iterator types model  and have the same value type, and the value type is *TriviallyCopyable*.

## Possible implementation

See also the implementations in [https://github.com/microsoft/STL/blob/472161105d596192194d4715ccad307c6c163b4a/stl/inc/algorithm#L4245-L4323 MSVC STL] and [https://github.com/gcc-mirror/gcc/blob/14d8a5ae472ca5743016f37da2dd4770d83dea21/libstdc%2B%2B-v3/include/bits/ranges_algo.h#L1330-L1359 libstdc++].
eq fun|1=
struct reverse_copy_fn
{
template<std::bidirectional_iterator I, std::sentinel_for<I> S,
std::weakly_incrementable O>
requires std::indirectly_copyable<I, O>
constexpr ranges::reverse_copy_result<I, O>
operator()(I first, S last, O result) const
{
auto ret = ranges::next(first, last);
for (; last != first; *result = *--last, ++result);
return {std::move(ret), std::move(result)};
}
template<ranges::bidirectional_range R, std::weakly_incrementable O>
requires std::indirectly_copyable<ranges::iterator_t<R>, O>
constexpr ranges::reverse_copy_result<ranges::borrowed_iterator_t<R>, O>
operator()(R&& r, O result) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(result));
}
};
inline constexpr reverse_copy_fn reverse_copy {};

## Example


### Example


**Output:**
```
12345 → 54321 → 12345
```


## See also


| cpp/algorithm/ranges/dsc reverse | (see dedicated page) |
| cpp/algorithm/dsc reverse_copy | (see dedicated page) |

