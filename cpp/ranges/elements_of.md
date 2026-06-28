---
title: std::ranges::elements_of
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_of
---

ddcl|header=ranges|since=c++23|1=
template< ranges::range R, class Allocator = std::allocator<std::byte> >
struct elements_of;
Encapsulates a . Specializations of `elements_of` act as a tag in overload sets to disambiguate when a range should be treated as a sequence rather than a single value.

## Template parameters


### Parameters

- `R` - a type that satisfies 
- `Allocator` - an allocator type that meets the requirements of *Allocator*

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |

All these members are declared with  attribute.

## Deduction guide

ddcl|since=c++23|1=
template< class R, class Allocator = std::allocator<std::byte> >
elements_of( R&&, Allocator = Allocator() ) -> elements_of<R&&, Allocator>;

## Example


### Example

```cpp
#include <any>
#include <generator>
#include <iostream>
#include <ranges>
#include <string_view>

template<bool Elementwise>
std::generator<std::any> gen(std::ranges::input_range auto&& r)
{
    if constexpr (Elementwise)
        co_yield std::ranges::elements_of(r); // yield each element of r
    else
        co_yield r;                           // yield r as a single value
}

int main()
{
    auto test = std::string_view{"test"};

    for (std::any a : gen<true>(test))
        std::cout << '[' << std::any_cast<char>(a) << "] ";
    std::cout << '\n';

    for (std::any a : gen<false>(test))
        std::cout << '[' << std::any_cast<std::string_view>(a) << "] ";
    std::cout << '\n';
}
```


**Output:**
```
[t] [e] [s] [t] 
[test]
```


## References

