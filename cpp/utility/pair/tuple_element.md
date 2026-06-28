---
title: std::tuple_element<std::pair>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/tuple_element
---


```cpp
**Header:** `<`utility`>`
dcl|since=c++11|
template< std::size_t I, class T1, class T2 >
struct tuple_element<I, std::pair<T1, T2>>;
```

The partial specializations of `std::tuple_element` for pairs provide compile-time access to the types of the pair's elements, using tuple-like syntax. The program is ill-formed if `1=I >= 2`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Possible implementation

eq fun
|1=
template<std::size_t I, typename T>
struct tuple_element;
template<std::size_t I, typename T1, typename T2>
struct tuple_element<I, std::pair<T1, T2>>
{
static_assert(I < 2, "std::pair has only 2 elements!");
};
template<typename T1, typename T2>
struct tuple_element<0, std::pair<T1, T2>>
{
using type = T1;
};
template<typename T1, typename T2>
struct tuple_element<1, std::pair<T1, T2>>
{
using type = T2;
};

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <tuple>

namespace detail
{
    template<std::size_t>
    struct index_tag { constexpr explicit index_tag() = default; };

    template<class T, class U>
    constexpr T get_val_dispatch(std::pair<T, U> const& pair, index_tag<0>)
    {
        return pair.first;
    }

    template<class T, class U>
    constexpr U get_val_dispatch(std::pair<T, U> const& pair, index_tag<1>)
    {
        return pair.second;
    }
} // namespace detail

template<std::size_t N, class T, class U>
auto constexpr get_val(std::pair<T, U> const& pair)
    -> typename std::tuple_element<N, std::pair<T, U>>::type
{
    return detail::get_val_dispatch(pair, detail::index_tag<N>{});
}

int main()
{
    auto var = std::make_pair(1, std::string{"one"});

    std::cout << get_val<0>(var) << " = " << get_val<1>(var);
}
```


**Output:**
```
1 = one
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2974 | c++11 | out-of-bounds index referred the undefined primary template | made ill-formed (hard error) |


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_element | (see dedicated page) |
| cpp/container/array/dsc tuple_element | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_element | (see dedicated page) |
| cpp/utility/pair/dsc tuple_size | (see dedicated page) |

