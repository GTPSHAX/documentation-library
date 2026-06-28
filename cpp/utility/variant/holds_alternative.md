---
title: std::holds_alternative
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/holds_alternative
---


```cpp
**Header:** `<`variant`>`
dcl|since=c++17|
template< class T, class... Types >
constexpr bool holds_alternative( const std::variant<Types...>& v ) noexcept;
```

Checks if the variant `v` holds the alternative `T`. The call is ill-formed if `T` does not appear exactly once in `Types...`

## Parameters


### Parameters

- `v` - variant to examine

## Return value

`true` if the variant currently holds the alternative `T`, `false` otherwise.

## Example


### Example

```cpp
#include <cassert>
#include <string>
#include <variant>

int main()
{
    std::variant<int, std::string> v = "abc";
    assert(not std::holds_alternative<int>(v));
    assert(std::holds_alternative<std::string>(v));
}
```


## See also


| cpp/utility/variant/dsc index | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |

