---
title: std::ranges::generate
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/generate
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_or_output_iterator O, std::sentinel_for<O> S,
std::copy_constructible F >
requires std::invocable<F&> && std::indirectly_writable<O, std::invoke_result_t<F&>>
constexpr O
generate( O first, S last, F gen );
dcl|num=2|since=c++20|1=
template< class R, std::copy_constructible F >
requires std::invocable<F&> && ranges::output_range<R, std::invoke_result_t<F&>>
constexpr ranges::borrowed_iterator_t<R>
generate( R&& r, F gen );
```

1. Assigns the result of ''successive'' invocations of the function object `gen` to each element in the range [first, last).
2. Same as , but uses `r` as the range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to modify, sentinel=yes}})` - 
- `r` - the range of elements to modify
- `gen` - the generator function object

## Return value

An output iterator that compares equal to `last`.

## Complexity

Exactly `ranges::distance(first, last)` invocations of `gen()` and assignments.

## Possible implementation

eq fun|1=
struct generate_fn
{
template<std::input_or_output_iterator O, std::sentinel_for<O> S,
std::copy_constructible F>
requires std::invocable<F&> && std::indirectly_writable<O, std::invoke_result_t<F&>>
constexpr O operator()(O first, S last, F gen) const
{
for (; first != last; *first = std::invoke(gen), ++first)
{}
return first;
}
template<class R, std::copy_constructible F>
requires std::invocable<F&> && ranges::output_range<R, std::invoke_result_t<F&>>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r, F gen) const
{
return (*this)(ranges::begin(r), ranges::end(r), std::move(gen));
}
};
inline constexpr generate_fn generate {};

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <random>
#include <string_view>

auto dice()
{
    static std::uniform_int_distribution<int> distr{1, 6};
    static std::random_device device;
    static std::mt19937 engine {device()};
    return distr(engine);
}

void iota(auto& r, int init)
{
    std::ranges::generate(r, [init] mutable { return init++; });
}

void print(std::string_view comment, const auto& v)
{
    for (std::cout << comment; int i : v)
        std::cout << i << ' ';
    std::cout << '\n';
}

int main()
{
    std::array<int, 8> v;

    std::ranges::generate(v.begin(), v.end(), dice);
    print("dice: ", v);
    std::ranges::generate(v, dice);
    print("dice: ", v);

    iota(v, 1);
    print("iota: ", v);
}
```


**Output:**
```
dice: 4 3 1 6 6 4 5 5
dice: 4 2 5 3 6 2 6 2
iota: 1 2 3 4 5 6 7 8
```


## See also


| cpp/algorithm/ranges/dsc generate_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/numeric/random/ranges/dsc generate_random | (see dedicated page) |
| cpp/algorithm/dsc generate | (see dedicated page) |

