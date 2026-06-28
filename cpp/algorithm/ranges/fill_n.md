---
title: std::ranges::fill_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fill_n
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|since1=c++20|until1=c++26|dcl1=
template< class T, std::output_iterator<const T&> O >
constexpr O fill_n( O first, std::iter_difference_t<O> n, const T& value );
|dcl2=
template< class O, class T = std::iter_value_t<O> >
requires std::output_iterator<O, const T&>
constexpr O fill_n( O first, std::iter_difference_t<O> n, const T& value );
```

Assigns the given `value` to all elements in the range [first, first + n).

## Parameters


### Parameters

- `first` - the beginning of the range of elements to modify
- `n` - number of elements to modify
- `value` - the value to be assigned

## Return value

An output iterator that compares equal to `first + n`.

## Complexity

Exactly `n` assignments.

## Possible implementation

eq fun|1=
struct fill_n_fn
{
template<class O, class T = std::iter_value_t<O>>
requires std::output_iterator<O, const T&>
constexpr O operator()(O first, std::iter_difference_t<O> n, const T& value) const
{
for (std::iter_difference_t<O> i {}; i != n; ++first, ++i)
*first = value;
return first;
}
};
inline constexpr fill_n_fn fill_n {};

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iostream>
#include <string>
#include <vector>

void println(const auto& v)
{
    for (const auto& elem : v)
        std::cout << ' ' << elem;
    std::cout << '\n';
}

int main()
{
    constexpr auto n{8};

    std::vector<std::string> v(n, "▓▓░░");
    println(v);

    std::ranges::fill_n(v.begin(), n, "░░▓▓");
    println(v);

    std::vector<std::complex<double>> nums{<!---->{1, 3}, {2, 2}, {4, 8}<!---->};
    println(nums);
    #ifdef __cpp_lib_algorithm_default_value_type
        std::ranges::fill_n(nums.begin(), 2, {4, 2});
    #else
        std::ranges::fill_n(nums.begin(), 2, std::complex<double>{4, 2});
    #endif
    println(nums);
}
```


**Output:**
```
<nowiki/>
 ▓▓░░ ▓▓░░ ▓▓░░ ▓▓░░ ▓▓░░ ▓▓░░ ▓▓░░ ▓▓░░
 ░░▓▓ ░░▓▓ ░░▓▓ ░░▓▓ ░░▓▓ ░░▓▓ ░░▓▓ ░░▓▓
 (1,3) (2,2) (4,8)
 (4,2) (4,2) (4,8)
```


## See also


| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/numeric/random/ranges/dsc generate_random | (see dedicated page) |
| cpp/algorithm/dsc fill_n | (see dedicated page) |

