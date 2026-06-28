---
title: std::ranges::generate_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/generate_n
---


```cpp
**Header:** `<`algorithm`>`
dcl|since=c++20|1=
template< std::input_or_output_iterator O, std::copy_constructible F >
requires std::invocable<F&> && std::indirectly_writable<O, std::invoke_result_t<F&>>
constexpr O
generate_n( O first, std::iter_difference_t<O> n, F gen );
```

Assigns the result of ''successive'' invocations of the function object `gen` to each element in the range [first, first + n), if `0 < n`. Does nothing otherwise.

## Parameters


### Parameters

- `first` - the beginning of the range of elements to modify
- `n` - number of elements to modify
- `gen` - the generator function object.

## Return value

Iterator one past the last element assigned if `0 < count`, `first` otherwise.

## Complexity

Exactly `n` invocations of `gen()` and assignments.

## Possible implementation

eq fun|1=
struct generate_n_fn
{
template<std::input_or_output_iterator O, std::copy_constructible F>
requires std::invocable<F&> && std::indirectly_writable<O, std::invoke_result_t<F&>>
constexpr O operator()(O first, std::iter_difference_t<O> n, F gen) const
{
for (; n-- > 0; *first = std::invoke(gen), ++first)
{}
return first;
}
};
inline constexpr generate_n_fn generate_n {};

## Example


### Example


**Output:**
```
5 5 2 2 6 6 3 5 (dice)
0 1 2 3 4 5 6 7 (iota)
```


## See also


| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/numeric/random/ranges/dsc generate_random | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/algorithm/dsc generate_n | (see dedicated page) |

