---
title: std::basic_string::begin
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/begin
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|
iterator begin();
dcla|anchor=no|num=2|noexcept=c++11|constexpr=c++20|
const_iterator begin() const;
dcla|anchor=no|num=3|constexpr=c++20|since=c++11|
const_iterator cbegin() const noexcept;
```

Returns an iterator to the first character of the string.
`begin()` returns a mutable or constant iterator, depending on the constness of `*this`.
`cbegin()` always returns a constant iterator. It is equivalent to `const_cast<const basic_string&>(*this).begin()`.

## Parameters

(none)

## Return value

Iterator to the first character.

## Complexity

Constant.

## Notes

libc++ backports `cbegin()` to C++98 mode.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string s("Exemplar");
    *s.begin() = 'e';
    std::cout << s << '\n';

    auto i = s.cbegin();
    std::cout << *i << '\n';
//  *i = 'E'; // error: i is a constant iterator
}
```


**Output:**
```
exemplar
e
```


## See also


| cpp/string/basic_string/dsc end | (see dedicated page) |
| cpp/string/basic_string_view/dsc begin | (see dedicated page) |

