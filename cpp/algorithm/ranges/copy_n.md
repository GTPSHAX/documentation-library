---
title: std::ranges::copy_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/copy_n
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|num=1|
template< std::input_iterator I, std::weakly_incrementable O >
requires std::indirectly_copyable<I, O>
constexpr copy_n_result<I, O>
copy_n( I first, std::iter_difference_t<I> n, O result );
dcl|since=c++20|num=2|1=
template< class I, class O >
using copy_n_result = ranges::in_out_result<I, O>;
```

1. Copies exactly `n` values from the range beginning at `first` to the range beginning at `result` by performing `1=*(result + i) = *(first + i)` for each integer in [0, n). The behavior is undefined if `result` is within the range [first, first + n) (`ranges::copy_backward` might be used instead in this case).

## Parameters


### Parameters

- `first` - the beginning of the range of elements to copy from
- `n` - number of the elements to copy
- `result` - the beginning of the destination range

## Return value

} or more formally, a value of type `ranges::in_out_result` that contains an  iterator equals to `ranges::next(first, n)` and a  iterator equals to `ranges::next(result, n)`.

## Complexity

Exactly `n` assignments.

## Notes

In practice, implementations of `std::ranges::copy_n` may avoid multiple assignments and use bulk copy functions such as `std::memmove` if the value type is *TriviallyCopyable* and the iterator types satisfy . Alternatively, such copy acceleration can be injected during an optimization phase of a compiler.
When copying overlapping ranges, `std::ranges::copy_n` is appropriate when copying to the left (beginning of the destination range is outside the source range) while `std::ranges::copy_backward` is appropriate when copying to the right (end of the destination range is outside the source range).

## Possible implementation

eq fun|1=
struct copy_n_fn
{
template<std::input_iterator I, std::weakly_incrementable O>
requires std::indirectly_copyable<I, O>
constexpr ranges::copy_n_result<I, O>
operator()(I first, std::iter_difference_t<I> n, O result) const
{
for (; n-- > 0; (void)++first, (void)++result)
*result = *first;
return {std::move(first), std::move(result)};
}
};
inline constexpr copy_n_fn copy_n{};

## Example


### Example


**Output:**
```
"ABCD"
in[5] = 'F'
out[5] = 'f'
```


## See also


| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |
| cpp/algorithm/dsc copy_n | (see dedicated page) |

