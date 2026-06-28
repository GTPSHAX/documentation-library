---
title: std::hash
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/hash
---


```cpp
**Header:** `<`bitset`>`
**Header:** `<`coroutine`>`
**Header:** `<`chrono|notes=
**Header:** `<`filesystem`>`
**Header:** `<`functional`>`
**Header:** `<`memory`>`
**Header:** `<`optional`>`
**Header:** `<`stacktrace`>`
**Header:** `<`string`>`
**Header:** `<`string_view`>`
**Header:** `<`system_error`>`
**Header:** `<`text_encoding`>`
**Header:** `<`thread`>`
**Header:** `<`typeindex`>`
**Header:** `<`variant`>`
**Header:** `<`vector`>`
dcl|since=c++11|
template< class Key >
struct hash;
```

The unordered associative containers `std::unordered_set`, `std::unordered_multiset`, `std::unordered_map`, `std::unordered_multimap` use specializations of the template `std::hash` as the default hash function.
Given a type `Key`, each specialization `std::hash<Key>` is either ''enabled'' or :
* If `std::hash<Key>` is not provided by the program or the user, it is disabled.
* Otherwise, `std::hash<Key>` is enabled if all following conditions are satisfied:
:* All following requirements are satisfied:
::* *Hash* (with `Key` as the function call argument type)
::* *DefaultConstructible*
::* *CopyAssignable*
::* *Swappable*
:* Given the following values:
::* `h`, an object of type `std::hash<Key>`.
::* `k1` and `k2`, objects of type `Key`.
:: All following requirements are satisfied:
::* If `1=k1 == k2` is `true`, `1=h(k1) == h(k2)` is also `true`.
::* Unless `std::hash<Key>` is a program-defined specialization, `h(k1)` will never throw an exception.
* Otherwise, `std::hash<Key>` is disabled.
Disabled specializations do not satisfy *Hash*, do not satisfy *FunctionObject*, and following values are all `false`:
* `std::is_default_constructible<std::hash<Key>>::value`
* `std::is_copy_constructible<std::hash<Key>>::value`
* `std::is_move_constructible<std::hash<Key>>::value`
* `std::is_copy_assignable<std::hash<Key>>::value`
* `std::is_move_assignable<std::hash<Key>>::value`
In other words, they exist, but cannot be used.
rrev|until=c++20|

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


## Standard library specializations

Each header that declares the template `std::hash` also provides enabled specializations of `std::hash` for the following types:
* all cv-unqualified arithmetic types
* all cv-unqualified enumeration types
* all cv-unqualified pointer types
* `std::nullptr_t`
On top of that, some headers also provide other enabled `std::hash` specializations for library types (see below).
rrev|since=c++17|
For all `std::hash` specializations provided by the standard library except the following, all their member functions are `noexcept`:
* `cpp/utility/optional/hash|std::hash<std::optional>`
* `cpp/utility/variant/hash|std::hash<std::variant>`
* `cpp/memory/unique_ptr/hash|std::hash<std::unique_ptr>`
rrev|since=c++26|
* `cpp/memory/indirect/hash|std::hash<std::indirect>`
* `cpp/chrono/duration/hash|std::hash<std::chrono::duration>`
* `cpp/chrono/time_point/hash|std::hash<std::chrono::time_point>`
* `cpp/chrono/zoned_time/hash|std::hash<std::chrono::zoned_time>`

## Specializations for library types


#### Language support library

| cpp/coroutine/coroutine_handle/dsc hash | (see dedicated page) |

#### Dianostics library

| cpp/error/error_code/dsc hash | (see dedicated page) |
| cpp/error/error_condition/dsc hash | (see dedicated page) |
| cpp/types/type_index/dsc hash | (see dedicated page) |
| cpp/utility/stacktrace_entry/dsc hash | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc hash | (see dedicated page) |

#### Memory management library

| cpp/memory/unique_ptr/dsc hash | (see dedicated page) |
| cpp/memory/shared_ptr/dsc hash | (see dedicated page) |
| cpp/memory/indirect/dsc hash | (see dedicated page) |

#### General utilities library

| cpp/utility/optional/dsc hash | (see dedicated page) |
| cpp/utility/variant/dsc hash | (see dedicated page) |
| cpp/utility/variant/monostate#Helper classes|title=std::hash | |
| cpp/utility/bitset/dsc hash | (see dedicated page) |

#### Containers library

| cpp/container/vector bool/hash|title=std::hash | |

#### Strings library

| cpp/string/basic_string/dsc hash | (see dedicated page) |
| cpp/string/basic_string_view/dsc hash | (see dedicated page) |

#### Text processing library

| cpp/text/text_encoding/dsc hash | (see dedicated page) |

#### Time library

| cpp/chrono/duration|nested=true|notes= | |
| cpp/chrono/time_point|nested=true|notes= | |
| cpp/chrono/day|nested=true|notes= | |
| cpp/chrono/month|nested=true|notes= | |
| cpp/chrono/year|nested=true|notes= | |
| cpp/chrono/weekday|nested=true|notes= | |
| cpp/chrono/weekday_indexed|nested=true|notes= | |
| cpp/chrono/weekday_last|nested=true|notes= | |
| cpp/chrono/month_day|nested=true|notes= | |
| cpp/chrono/month_day_last|nested=true|notes= | |
| cpp/chrono/month_weekday|nested=true|notes= | |
| cpp/chrono/month_weekday_last|nested=true|notes= | |
| cpp/chrono/year_month|nested=true|notes= | |
| cpp/chrono/year_month_day|nested=true|notes= | |
| cpp/chrono/year_month_day_last|nested=true|notes= | |
| cpp/chrono/year_month_weekday|nested=true|notes= | |
| cpp/chrono/year_month_weekday_last|nested=true|notes= | |
| cpp/chrono/zoned_time|nested=true|notes= | |
| cpp/chrono/leap_second|nested=true|notes= | |

#### Input/output library

| cpp/filesystem/path/dsc hash | (see dedicated page) |

#### Concurrency support library

| cpp/thread/thread/id/dsc hash | (see dedicated page) |


## Notes

The actual hash functions are implementation-dependent and are not required to fulfill any other quality criteria except those specified above. Notably, some implementations use trivial (identity) hash functions which map an integer to itself. In other words, these hash functions are designed to work with unordered associative containers, but not as cryptographic hashes, for example.
Hash functions are only required to produce the same result for the same input within a single execution of a program; this allows salted hashes that prevent collision denial-of-service attacks.
There is no specialization for C strings. `std::hash<const char*>` produces a hash of the value of the pointer (the memory address), it does not examine the contents of any character array.
Additional specializations for `std::pair` and the standard container types, as well as utility functions to compose hashes are available in [https://www.boost.org/doc/libs/release/libs/container_hash/doc/html/hash.html#ref `boost::hash`].

## Example


### Example

```cpp
#include <cstddef>
#include <functional>
#include <iomanip>
#include <iostream>
#include <string>
#include <unordered_set>

struct S
{
    std::string first_name;
    std::string last_name;
    bool operator==(const S&) const = default; // since C++20
};

// Before C++20.
// bool operator==(const S& lhs, const S& rhs)
// {
//     return lhs.first_name == rhs.first_name && lhs.last_name == rhs.last_name;
// }

// Custom hash can be a standalone function object.
struct MyHash
{
    std::size_t operator()(const S& s) const noexcept
    {
        std::size_t h1 = std::hash<std::string>{}(s.first_name);
        std::size_t h2 = std::hash<std::string>{}(s.last_name);
        return h1 ^ (h2 << 1); // or use boost::hash_combine
    }
};

// Custom specialization of std::hash can be injected in namespace std.
template<>
struct std::hash<S>
{
    std::size_t operator()(const S& s) const noexcept
    {
        std::size_t h1 = std::hash<std::string>{}(s.first_name);
        std::size_t h2 = std::hash<std::string>{}(s.last_name);
        return h1 ^ (h2 << 1); // or use boost::hash_combine
    }
};

int main()
{
    std::string str = "Meet the new boss...";
    std::size_t str_hash = std::hash<std::string>{}(str);
    std::cout << "hash(" << std::quoted(str) << ") =\t" << str_hash << '\n';

    S obj = {"Hubert", "Farnsworth"};
    // Using the standalone function object.
    std::cout << "hash(" << std::quoted(obj.first_name) << ", "
              << std::quoted(obj.last_name) << ") =\t"
              << MyHash{}(obj) << " (using MyHash) or\n\t\t\t\t"
              << std::hash<S>{}(obj) << " (using injected specialization)\n";

    // Custom hash makes it possible to use custom types in unordered containers.
    // The example will use the injected std::hash<S> specialization above,
    // to use MyHash instead, pass it as a second template argument.
    std::unordered_set<S> names = {obj, {"Bender", "Rodriguez"}, {"Turanga", "Leela"}<!---->};
    for (auto const& s: names)
        std::cout << std::quoted(s.first_name) << ' '
                  << std::quoted(s.last_name) << '\n';
}
```


**Output:**
```
hash("Meet the new boss...") =  10656026664466977650
hash("Hubert", "Farnsworth") =  12922914235676820612 (using MyHash) or
                                12922914235676820612 (using injected specialization)
"Bender" "Rodriguez"
"Turanga" "Leela"
"Hubert" "Farnsworth"
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2119 | C++11 | specializations for extended integer types were missing | provided |
| lwg-2148 | C++11 | specializations for enumerations were missing | provided |

