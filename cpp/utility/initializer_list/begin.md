---
title: std::initializer_list::begin
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list/begin
---

ddcla|since=c++11|constexpr=c++14|
const T* begin() const noexcept;
Obtains a pointer to the first element in the `initializer_list`. Equivalent to `return data();`.
If the initializer list is empty, the values of `begin()` and `end()` are unspecified, but will be identical.

## Return value

A pointer to the first element in the initializer list

## Complexity

Constant

## Example


### Example

```cpp
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <iterator>

int main()
{
    static constexpr auto il = {42, 24};
    static_assert(*il.begin() == 0x2A);
    static_assert(il.begin()[1] == 030);

    std::initializer_list ϕ = {'1', '.', '6', '1', '8', '0'};

    std::copy(ϕ.begin(),
              ϕ.end(),
              std::ostream_iterator<char>(std::cout, ""));

    std::cout << '\n';
}
```


**Output:**
```
1.6180
```


## See also


| cpp/utility/initializer_list/dsc end | (see dedicated page) |

