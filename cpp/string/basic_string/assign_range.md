---
title: std::basic_string::assign_range
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/assign_range
---

ddcl|since=c++23|1=
template< container-compatible-range<CharT> R >
constexpr std::basic_string& assign_range( R&& rg );
Replaces the contents of the string with the values in the range `rg`.
Equivalent to

```cpp
return assign(
    std::basic_string(
        std::from_range,
        std​::​forward<R>(rg),
        get_allocator())
);
```


## Parameters


### Parameters

- `rg` - a 

## Return value

`*this`

## Complexity

Linear in size of `rg`.

## Exceptions


## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string>

int main()
{
    const auto source = {'s', 'o', 'u', 'r', 'c', 'e'};
    std::string destination{"destination"};

#ifdef __cpp_lib_containers_ranges
    destination.assign_range(source);
#else
    destination.assign(source.begin(), source.end());
#endif

    assert(destination == "source");
}
```


## See also


| cpp/string/basic_string/dsc assign | (see dedicated page) |
| cpp/string/basic_string/dsc operator{{= | (see dedicated page) |
| cpp/string/basic_string/dsc constructor | (see dedicated page) |

