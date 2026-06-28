---
title: std::hash<std::variant>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/hash
---


# hashpetty|<std::variant>

ddcl|header=variant|since=c++17|1=
template< class... Types >
struct hash<std::variant<Types...>>;
The template specialization of `std::hash` for the `std::variant` template allows users to obtain hashes of `variant` objects.
The specialization  is enabled (see `std::hash`) if every specialization in  is enabled, and is disabled otherwise.
The member functions of this specialization are not guaranteed to be noexcept.

## Template parameters


### Parameters

- `Types` - the types of the alternatives supported by the `variant` object

## Notes

Unlike `cpp/utility/optional/hash|std::hash<std::optional>`, hash of a variant does not typically equal the hash of the contained value; this makes it possible to distinguish `std::variant<int, int>` holding the same value as different alternatives.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <variant>

using Var = std::variant<int, int, int, std::string>;

template<unsigned I>
void print(Var const& var)
{
    std::cout << "get<" << var.index() << "> = "
              << std::get<I>(var)
              << "\t" "# = "
              << std::hash<Var>{}(var) << '\n';
}

int main()
{
    Var var;
    std::get<0>(var) = 2020;
    print<0>(var);
    var.emplace<1>(2023);
    print<1>(var);
    var.emplace<2>(2026);
    print<2>(var);
    var = "C++";
    print<3>(var);
}
```


**Output:**
```
get<0> = 2020   # = 2020
get<1> = 2023   # = 2024
get<2> = 2026   # = 2028
get<3> = C++    # = 15518724754199266859
```


## See also


| cpp/utility/dsc hash | (see dedicated page) |

