---
title: std::optional
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional
---

ddcl|header=optional|since=c++17|
template< class T >
class optional;
The class template `std::optional` manages an optional contained value, i.e. a value that may or may not be present.
A common use case for `optional` is the return value of a function that may fail. As opposed to other approaches, such as `std::pair<T, bool>`, `optional` handles expensive-to-construct objects well and is more readable, as the intent is expressed explicitly.
Any instance of `optional` at any given point in time either ''contains a value'' or ''does not contain a value''.
If an `optional` contains a value, the value is guaranteed to be nested within the `optional` object. Thus, an `optional` object models an object, not a pointer, even though `operator*()` and `operator->()` are defined.
When an object of type `optional<T>` is contextually converted to `bool`, the conversion returns `true` if the object contains a value and `false` if it does not contain a value.
The `optional` object contains a value in the following conditions:
* The object is initialized with/assigned from a value of type `T` or another `optional` that contains a value.
The object does not contain a value in the following conditions:
* The object is default-initialized.
* The object is initialized with/assigned from a value of type `std::nullopt_t` or an  `optional` object that does not contain a value.
* The member function `reset()` is called.
rrev|since=c++26|
The `optional` object is a  that contains either one element if it ''contains a value'', or otherwise zero elements if it does not contain a value. The lifetime of the contained element is bound to the object.
There are no optional references, functions, arrays, or (possibly cv-qualified) `void`; a program is ill-formed if it instantiates an `optional` with such a type. In addition, a program is ill-formed if it instantiates an `optional` with the (possibly cv-qualified) tag types `std::nullopt_t` or `std::in_place_t`.

## Template parameters


### Parameters

- `T` - the type of the value to manage initialization state for. The type must meet the requirements of *Destructible* (in particular, array and reference types are not allowed).

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |

All requirements on the iterator types of a *Container* apply to the `iterator` type of `optional` as well.

## Data members


## Member functions


| cpp/utility/optional/dsc constructor | (see dedicated page) |
| cpp/utility/optional/dsc destructor | (see dedicated page) |
| cpp/utility/optional/dsc operator{{= | (see dedicated page) |

#### Iterators

| cpp/utility/optional/dsc begin | (see dedicated page) |
| cpp/utility/optional/dsc end | (see dedicated page) |

#### Observers

| cpp/utility/optional/dsc operator* | (see dedicated page) |
| cpp/utility/optional/dsc operator bool | (see dedicated page) |
| cpp/utility/optional/dsc value | (see dedicated page) |
| cpp/utility/optional/dsc value_or | (see dedicated page) |

#### Monadic operations

| cpp/utility/optional/dsc and_then | (see dedicated page) |
| cpp/utility/optional/dsc transform | (see dedicated page) |
| cpp/utility/optional/dsc or_else | (see dedicated page) |

#### Modifiers

| cpp/utility/optional/dsc swap | (see dedicated page) |
| cpp/utility/optional/dsc reset | (see dedicated page) |
| cpp/utility/optional/dsc emplace | (see dedicated page) |


## Non-member functions


| cpp/utility/optional/dsc operator_cmp | (see dedicated page) |
| cpp/utility/optional/dsc make_optional | (see dedicated page) |
| cpp/utility/optional/dsc swap2 | (see dedicated page) |


## Helper classes


| cpp/utility/optional/dsc hash | (see dedicated page) |
| cpp/utility/optional/dsc nullopt_t | (see dedicated page) |
| cpp/utility/optional/dsc bad_optional_access | (see dedicated page) |


## Helpers


| cpp/utility/optional/dsc nullopt | (see dedicated page) |
| cpp/utility/optional/dsc in_place | (see dedicated page) |


## Helper specializations

ddcl|since=c++26|1=
template< class T >
constexpr bool ranges::enable_view<std::optional<T>> = true;
This specialization of `ranges::enable_view` makes `optional` satisfy .
ddcl|since=c++26|1=
template< class T >
constexpr auto format_kind<std::optional<T>> = range_format::disabled;
This specialization of `format_kind` disables the range formatting support of `optional`.

## Deduction guides


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <optional>
#include <string>

// optional can be used as the return type of a factory that may fail
std::optional<std::string> create(bool b)
{
    if (b)
        return "Godzilla";
    return {};
}

// std::nullopt can be used to create any (empty) std::optional
auto create2(bool b)
{
    return b ? std::optional<std::string>{"Godzilla"} : std::nullopt;
}

int main()
{
    std::cout << "create(false) returned "
              << create(false).value_or("empty") << '\n';

    // optional-returning factory functions are usable as conditions of while and if
    if (auto str = create2(true))
        std::cout << "create2(true) returned " << *str << '\n';
}
```


**Output:**
```
create(false) returned empty
create2(true) returned Godzilla
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4141 | C++17 | the requirement of storage<br>allocation was confusing | the contained object must be<br>nested within the tt |


## See also


| cpp/utility/dsc variant | (see dedicated page) |
| cpp/utility/dsc any | (see dedicated page) |
| cpp/utility/dsc expected | (see dedicated page) |
| cpp/ranges/dsc single_view | (see dedicated page) |
| cpp/ranges/dsc empty_view | (see dedicated page) |

