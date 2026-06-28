---
title: std::variant
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant
---

ddcl|header=variant|since=c++17|
template< class... Types >
class variant;
The class template `std::variant` represents a type-safe .
An instance of `variant` at any given time either holds a value of one of its alternative types, or in the case of error - no value (this state is hard to achieve, see `cpp/utility/variant/valueless_by_exception`).
As with unions, if a variant holds a value of some object type `T`, the `T` object is nested within the `variant` object.
A variant is not permitted to hold references, arrays, or the type `void`.
A variant is permitted to hold the same type more than once, and to hold differently cv-qualified versions of the same type.
Consistent with the behavior of unions during , a default-constructed variant holds a value of its first alternative, unless that alternative is not default-constructible (in which case the variant is not default-constructible either). The helper class  can be used to make such variants default-constructible.
A program that instantiates the definition of `std::variant` with no template arguments is ill-formed. `std::variant<std::monostate>` can be used instead.
If a program declares an explicit or partial specialization of `std::variant`, the program is ill-formed, no diagnostic required.

## Template parameters


### Parameters

- `Types` - the types that may be stored in this variant. All types must meet the *Destructible* requirements (in particular, array types and non-object types are not allowed).

## Member functions


| cpp/utility/variant/dsc constructor | (see dedicated page) |
| cpp/utility/variant/dsc destructor | (see dedicated page) |
| cpp/utility/variant/dsc operator{{= | (see dedicated page) |

#### Observers

| cpp/utility/variant/dsc index | (see dedicated page) |
| cpp/utility/variant/dsc valueless_by_exception | (see dedicated page) |

#### Modifiers

| cpp/utility/variant/dsc emplace | (see dedicated page) |
| cpp/utility/variant/dsc swap | (see dedicated page) |

#### Visitation

| cpp/utility/variant/dsc visit | (see dedicated page) |


## Non-member functions


| cpp/utility/variant/dsc visit2 | (see dedicated page) |
| cpp/utility/variant/dsc holds_alternative | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc get_if | (see dedicated page) |
| cpp/utility/variant/dsc operator_cmp | (see dedicated page) |
| cpp/utility/variant/dsc swap2 | (see dedicated page) |


## Helper classes


| cpp/utility/variant/dsc monostate | (see dedicated page) |
| cpp/utility/variant/dsc bad_variant_access | (see dedicated page) |
| cpp/utility/variant/dsc variant_size | (see dedicated page) |
| cpp/utility/variant/dsc variant_alternative | (see dedicated page) |
| cpp/utility/variant/dsc hash | (see dedicated page) |


## Helper objects


| cpp/utility/variant/dsc variant_npos | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <variant>

int main()
{
    std::variant<int, float> v, w;
    v = 42; // v contains int
    int i = std::get<int>(v);
    assert(42 == i); // succeeds
    w = std::get<int>(v);
    w = std::get<0>(v); // same effect as the previous line
    w = v; // same effect as the previous line

//  std::get<double>(v); // error: no double in [int, float]
//  std::get<3>(v);      // error: valid index values are 0 and 1

    try
    {
        std::get<float>(w); // w contains int, not float: will throw
    }
    catch (const std::bad_variant_access& ex)
    {
        std::cout << ex.what() << '\n';
    }

    using namespace std::literals;

    std::variant<std::string> x("abc");
    // converting constructors work when unambiguous
    x = "def"; // converting assignment also works when unambiguous

    std::variant<std::string, void const*> y("abc");
    // casts to void const* when passed a char const*
    assert(std::holds_alternative<void const*>(y)); // succeeds
    y = "xyz"s;
    assert(std::holds_alternative<std::string>(y)); // succeeds
}
```


**Output:**
```
std::get: wrong index for variant
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4141 | C++17 | the requirement for storage<br>allocation was confusing | the contained object must be<br>nested within the tt |


## See also


| cpp/utility/dsc in_place | (see dedicated page) |
| cpp/utility/dsc optional | (see dedicated page) |
| cpp/utility/dsc any | (see dedicated page) |

