---
title: std::basic_string::append_range
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/append_range
---

ddcl|since=c++23|1=
template< container-compatible-range<CharT> R >
constexpr std::basic_string& append_range( R&& rg );
Appends all characters from the range `rg`.
Equivalent to

```cpp
return append(std::basic_string( std::from_range, std​::​forward<R>(rg), get_allocator()));
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
    std::string head{"long long"};
    const auto tail = {' ', 'i', 'n', 't'};

#ifdef __cpp_lib_containers_ranges
    head.append_range(tail);
#else
    head.append(tail.begin(), tail.end());
#endif

    assert(head == "long long int");
}
```


## See also


| cpp/string/basic_string/dsc append | (see dedicated page) |

