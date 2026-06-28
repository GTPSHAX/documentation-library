---
title: std::basic_string::crend
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/rend
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|
reverse_iterator rend();
dcla|anchor=no|num=2|noexcept=c++11|constexpr=c++20|
const_reverse_iterator rend() const;
dcla|anchor=no|num=3|since=c++11|constexpr=c++20|
const_reverse_iterator crend() const noexcept;
```

Returns a reverse iterator to the character following the last character of the reversed string. It corresponds to the character preceding the first character of the non-reversed string. This character acts as a placeholder, attempting to access it results in undefined behavior.

## Parameters

(none)

## Return value

Reverse iterator to the character following the last character.

## Complexity

Constant.

## Notes

libc++ backports `crend()` to C++98 mode.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string p("[A man, a plan, a canal: Panama]");
    std::string q;

    std::copy(p.crbegin(), p.crend(), std::back_inserter(q));
    std::cout << "q = " << q << '\n';

    std::copy(q.crbegin(), q.crend(), p.rbegin());
    std::cout << "p = " << p << '\n';
}
```


**Output:**
```
q = ]amanaP :lanac a ,nalp a ,nam A[
p = ]amanaP :lanac a ,nalp a ,nam A[
```


## See also


| cpp/string/basic_string/dsc rbegin | (see dedicated page) |
| cpp/string/basic_string_view/dsc rend | (see dedicated page) |

