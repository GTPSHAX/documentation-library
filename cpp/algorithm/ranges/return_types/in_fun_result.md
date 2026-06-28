---
title: std::ranges::in_fun_result
type: Constrained algorithms
source: https://en.cppreference.com/w/cpp/algorithm/ranges/return_types/in_fun_result
---

ddcl|header=algorithm|since=c++20|
template< class I, class F >
struct in_fun_result;
`ranges::in_fun_result` is a class template that provides a way to store an iterator and a function object as a single unit.

## Template parameters


### Parameters

- `I` - the type of the iterator that the `ranges::in_fun_result` stores.
- `F` - the type of the function object that the `ranges::in_fun_result` stores.

## Data members


| Item | Description |
|------|-------------|
| **Object** | Description |

All these members are declared with  attribute.

## Member functions

member|operator in_fun_result<I2, F2>|2=

```cpp
dcl|num=1|1=
template<class I2, class F2>
requires std::convertible_to<const I&, I2> && std::convertible_to<const F&, F2>
constexpr operator in_fun_result<I2, F2>() const &;
dcl|num=2|1=
template<class I2, class F2>
requires std::convertible_to<I, I2> && std::convertible_to<F, F2>
constexpr operator in_fun_result<I2, F2>() &&;
```

Converts `*this` to the result by constructing every data member of the result from the corresponding member of `*this`.
1. Equivalent to }.
2. Equivalent to }.

## Standard library

The following standard library functions use `ranges::in_fun_result` as the return type:


#### Algorithm functions

| cpp/algorithm/ranges/dsc for_each | (see dedicated page) |
| cpp/algorithm/ranges/dsc for_each_n | (see dedicated page) |


## Synopsis


```cpp
namespace std::ranges
{
    template<class I, class F>
    struct in_fun_result
    {
        [[no_unique_address]] I in;
        [[no_unique_address]] F fun;

        template<class I2, class F2>
        requires std::convertible_to<const I&, I2> && std::convertible_to<const F&, F2>
        constexpr operator in_fun_result<I2, F2>() const &
        {
            return {in, fun};
        }

        template<class I2, class F2>
        requires std::convertible_to<I, I2> && std::convertible_to<F, F2>
        constexpr operator in_fun_result<I2, F2>() &&
        {
            return {std::move(in), std::move(fun)};
        }
    };
}
```


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    int v[]{1, 2, 3};

    const std::ranges::in_fun_result res1 = std::ranges::for_each_n(
        v, std::size(v),
        [](int& x) { return x = -x; } // negating lambda
    );
    assert(res1.in == std::end(v));

    const std::ranges::in_fun_result res2 = std::ranges::for_each(
        std::begin(v),
        res1.in,
        [](int x) { std::cout << x << ' '; } // printing lambda
    );

    std::cout << "│ ";

    std::ranges::for_each(v, res1.fun); // uses negating lambda
    std::ranges::for_each(v, res2.fun); // uses printing lambda
    std::cout << '\n';
}
```


**Output:**
```
-1 -2 -3 │ 1 2 3
```


## See also


| cpp/utility/dsc pair | (see dedicated page) |
| cpp/utility/dsc tuple | (see dedicated page) |

