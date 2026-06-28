---
title: std::basic_string_view::at
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/at
---


```cpp
dcl|since=c++17|
constexpr const_reference at( size_type pos ) const;
```

Returns a `const` reference to the character at specified location `pos`. Bounds checking is performed, exception of type `std::out_of_range` will be thrown on invalid access.

## Parameters


### Parameters

- `pos` - position of the character to return

## Return value

`Const` reference to the requested character.

## Exceptions

Throws `std::out_of_range` if `1=pos >= size()`.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string_view>

int main()
{
    std::string_view str_view("abcdef");

    try
    {
        for (std::size_t i = 0; true; ++i)
            std::cout << i << ": " << str_view.at(i) << '\n';
    }
    catch (const std::out_of_range& e)
    {
        std::cout << "Whooops. Index is out of range.\n";
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
0: a
1: b
2: c
3: d
4: e
5: f
6: Whooops. Index is out of range.
basic_string_view::at: __pos (which is 6) >= this->size() (which is 6)
```


## See also


| cpp/string/basic_string_view/dsc operator_at | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |

