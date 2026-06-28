---
title: std::swap(std::optional)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/swap2
---


# swapsmall|(std::optional)

ddcl|header=optional|since=c++17|notes=<sup>(constexpr C++20)</sup>|
template< class T >
void swap( std::optional<T>& lhs,
std::optional<T>& rhs ) noexcept(/* see below */);
Overloads the `std::swap` algorithm for `std::optional`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.
.

## Parameters


### Parameters

- `lhs, rhs` - `optional` objects whose states to swap

## Return value

(none)

## Exceptions


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <optional>
#include <string>

int main()
{
    std::optional<std::string> a{"██████"}, b{"▒▒▒▒▒▒"};

    auto print = [&](auto const& s)
    {
        std::cout << s << "\t"
                     "a = " << a.value_or("(null)") << "  "
                     "b = " << b.value_or("(null)") << '\n';
    };

    print("Initially:");
    std::swap(a, b);
    print("swap(a, b):");
    a.reset();
    print("\n""a.reset():");
    std::swap(a, b);
    print("swap(a, b):");
}
```


**Output:**
```
Initially:   a = ██████  b = ▒▒▒▒▒▒
swap(a, b):  a = ▒▒▒▒▒▒  b = ██████

a.reset():   a = (null)  b = ██████
swap(a, b):  a = ██████  b = (null)
```


## Defect reports


## See also


| cpp/utility/optional/dsc swap | (see dedicated page) |

