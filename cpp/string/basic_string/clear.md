---
title: std::basic_string::clear
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/clear
---

ddcla|noexcept=c++11|constexpr=c++20|
void clear();
Removes all characters from the string as if by executing `erase(begin(), end())`.
All pointers, references, and iterators are invalidated.

## Parameters

(none)

## Return value

(none)

## Notes

Unlike for `std::vector::clear`, the C++ standard does not explicitly require that `capacity` is unchanged by this function, but existing implementations do not change capacity. This means that they do not release the allocated memory (see also `shrink_to_fit`).

## Complexity

Linear in the size of the string, although existing implementations operate in constant time.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>

int main()
{
    std::string s{"Exemplar"};
    std::string::size_type const capacity = s.capacity();

    s.clear();
    assert(s.empty());
    assert(s.size() == 0);
    std::cout << std::boolalpha << (s.capacity() == capacity) << '\n';
}
```


**Output:**
```
true
```


## See also


| cpp/string/basic_string/dsc erase | (see dedicated page) |

