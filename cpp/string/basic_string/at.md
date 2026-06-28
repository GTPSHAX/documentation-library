---
title: std::basic_string::at
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/at
---


```cpp
dcla|anchor=no|num=1|constexpr=c++20|
CharT& at( size_type pos );
dcla|anchor=no|num=2|constexpr=c++20|
const CharT& at( size_type pos ) const;
```

Returns a reference to the character at specified location `pos`. Bounds checking is performed, exception of type `std::out_of_range` will be thrown on invalid access.

## Parameters


### Parameters

- `pos` - position of the character to return

## Return value

Reference to the requested character.

## Exceptions

Throws `std::out_of_range` if `1=pos >= size()`.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

int main()
{
    std::string s("message"); // for capacity

    s = "abc";
    s.at(2) = 'x'; // OK
    std::cout << s << '\n';

    std::cout << "string size = " << s.size() << '\n';
    std::cout << "string capacity = " << s.capacity() << '\n';

    try
    {
        // This will throw since the requested offset is greater than the current size.
        s.at(3) = 'x';
    }
    catch (std::out_of_range const& exc)
    {
        std::cout << exc.what() << '\n';
    }
}
```


**Output:**
```
abx
string size = 3
string capacity = 7
basic_string::at
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc operator_at | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

