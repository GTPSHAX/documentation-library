---
title: std::any
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any
---

ddcl|header=any|since=c++17|
class any;
The class `any` describes a type-safe container for single values of any copy constructible type.
1. An object of class `any` stores an instance of any type that satisfies the constructor requirements or is empty, and this is referred to as the ''state'' of the class `any` object. The stored instance is called the contained object. Two states are equivalent if they are either both empty or if both are not empty and if the contained objects are equivalent.
2. The non-member `any_cast` functions provide type-safe access to the contained object.
Implementations are encouraged to avoid dynamic allocations for small objects, but such an optimization may only be applied to types for which `std::is_nothrow_move_constructible` returns `true`.

## Member functions


| cpp/utility/any/dsc constructor | (see dedicated page) |
| cpp/utility/any/dsc operator{{= | (see dedicated page) |
| cpp/utility/any/dsc destructor | (see dedicated page) |

#### Modifiers

| cpp/utility/any/dsc emplace | (see dedicated page) |
| cpp/utility/any/dsc reset | (see dedicated page) |
| cpp/utility/any/dsc swap | (see dedicated page) |

#### Observers

| cpp/utility/any/dsc has_value | (see dedicated page) |
| cpp/utility/any/dsc type | (see dedicated page) |


## Non-member functions


| cpp/utility/any/dsc swap2 | (see dedicated page) |
| cpp/utility/any/dsc any_cast | (see dedicated page) |
| cpp/utility/any/dsc make_any | (see dedicated page) |


## Helper classes


| cpp/utility/any/dsc bad_any_cast | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <any>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    // any type
    std::any a = 1;
    std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
    a = 3.14;
    std::cout << a.type().name() << ": " << std::any_cast<double>(a) << '\n';
    a = true;
    std::cout << a.type().name() << ": " << std::any_cast<bool>(a) << '\n';

    // bad cast
    try
    {
        a = 1;
        std::cout << std::any_cast<float>(a) << '\n';
    }
    catch (const std::bad_any_cast& e)
    {
        std::cout << e.what() << '\n';
    }

    // has value
    a = 2;
    if (a.has_value())
        std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';

    // reset
    a.reset();
    if (!a.has_value())
        std::cout << "no value\n";

    // pointer to contained data
    a = 3;
    int* i = std::any_cast<int>(&a);
    std::cout << *i << '\n';
}
```


**Output:**
```
int: 1
double: 3.14
bool: true
bad any_cast
int: 2
no value
3
```


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/dsc variant | (see dedicated page) |
| cpp/utility/dsc optional | (see dedicated page) |
| cpp/memory/dsc unique_ptr | (see dedicated page) |
| cpp/memory/dsc indirect | (see dedicated page) |
| cpp/memory/dsc polymorphic | (see dedicated page) |

