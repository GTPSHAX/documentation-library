---
title: std::swap(std::basic_string)
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/swap2
---


# swapsmall|(std::basic_string)


```cpp
**Header:** `<`string`>`
dcl rev multi
|until1=c++17|dcl1=
template< class CharT, class Traits, class Alloc >
void swap( std::basic_string<CharT, Traits, Alloc>& lhs,
std::basic_string<CharT, Traits, Alloc>& rhs );
|notes2=<sup>(constexpr C++20)</sup>|dcl2=
template< class CharT, class Traits, class Alloc >
void swap( std::basic_string<CharT, Traits, Alloc>& lhs,
std::basic_string<CharT, Traits, Alloc>& rhs ) noexcept(/* see below */);
```

Specializes the `std::swap` algorithm for `std::basic_string`. Swaps the contents of `lhs` and `rhs`.
Equivalent to `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - strings whose contents to swap

## Return value

(none)

## Complexity

Constant.
rrev|since=c++17|

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string a = "AAA";
    std::string b = "BBBB";

    std::cout << "Before swap:\n"
                 "a = " << a << "\n"
                 "b = " << b << "\n\n";

    std::swap(a, b);

    std::cout << "After swap:\n"
                 "a = " << a << "\n"
                 "b = " << b << '\n';
}
```


**Output:**
```
Before swap:
a = AAA
b = BBBB

After swap:
a = BBBB
b = AAA
```


## Defect reports


## See also


| cpp/string/basic_string/dsc swap | (see dedicated page) |

