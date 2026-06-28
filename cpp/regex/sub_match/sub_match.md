---
title: std::sub_match::sub_match
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/sub_match/sub_match
---

ddcl|since=c++11|
constexpr sub_match();
Default constructs a `std::sub_match`. The `matched` member is set to `false` and the inherited members `first` and `second` are value-initialized.
This is the only publicly accessible and defined constructor.

## Example


### Example

```cpp
#include <cassert>
#include <regex>

int main()
{
    std::sub_match<const char*> s;
    assert(!s.matched);
}
```

