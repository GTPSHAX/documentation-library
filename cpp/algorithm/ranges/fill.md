---
title: std::ranges::fill
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/fill
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|anchor=Version_1|since1=c++20|until1=c++26
|dcl1=
template< class T, std::output_iterator<const T&> O, std::sentinel_for<O> S >
constexpr O fill( O first, S last, const T& value );
|dcl2=
template< class O, std::sentinel_for<O> S, class T = std::iter_value_t<O> >
requires std::output_iterator<O, const T&>
constexpr O fill( O first, S last, const T& value );
dcl rev multi|num=2|since1=c++20|until1=c++26
|dcl1=
template< class T, ranges::output_range<const T&> R >
constexpr ranges::borrowed_iterator_t<R> fill( R&& r, const T& value );
|dcl2=
template< class R, class T = ranges::range_value_t<R> >
requires ranges::output_range<R, const T&>
constexpr ranges::borrowed_iterator_t<R> fill( R&& r, const T& value );
```

1. Assigns the given `value` to the elements in the range [first, last).
2. Same as , but uses `r` as the source range, as if using `ranges::begin(r)` as `first` and `ranges::end(r)` as `last`.

## Parameters


### Parameters

- `[3=to modify, sentinel=yes}})` - 
- `r` - the range of elements to modify
- `value` - the value to be assigned

## Return value

An output iterator that compares equal to `last`.

## Complexity

Exactly `last - first` assignments.

## Possible implementation

eq fun|1=
struct fill_fn
{
template<class O, std::sentinel_for<O> S, class T = std::iter_value_t<O>>
requires std::output_iterator<O, const T&>
constexpr O operator()(O first, S last, const T& value) const
{
while (first != last)
*first++ = value;
return first;
}
template<class R, class T = ranges::range_value_t<R>>
requires ranges::output_range<R, const T&>
constexpr ranges::borrowed_iterator_t<R> operator()(R&& r, const T& value) const
{
return (*this)(ranges::begin(r), ranges::end(r), value);
}
};
inline constexpr fill_fn fill;

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <complex>
#include <iostream>
#include <vector>

void println(const auto& seq)
{
    for (const auto& e : seq)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{0, 1, 2, 3, 4, 5};

    // set all elements to -1 using overload (1)
    std::ranges::fill(v.begin(), v.end(), -1);
    println(v);

    // set all element to 10 using overload (2)
    std::ranges::fill(v, 10);
    println(v);

    std::vector<std::complex<double>> nums{<!---->{1, 3}, {2, 2}, {4, 8}<!---->};
    println(nums);
    #ifdef __cpp_lib_algorithm_default_value_type
        std::ranges::fill(nums, {4, 2}); // T gets deduced
    #else
        std::ranges::fill(nums, std::complex<double>{4, 2});
    #endif
    println(nums);
}
```


**Output:**
```
-1 -1 -1 -1 -1 -1
10 10 10 10 10 10
(1,3) (2,2) (4,8)
(4,2) (4,2) (4,2)
```


## See also


| cpp/algorithm/ranges/dsc fill_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/numeric/random/ranges/dsc generate_random | (see dedicated page) |
| cpp/algorithm/dsc fill | (see dedicated page) |

