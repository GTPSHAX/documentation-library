---
title: std::basic_string_view::npos
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/npos
---

ddcl|since=c++17|1=
static constexpr size_type npos = size_type(-1);
This is a special value equal to the maximum value representable by the type `size_type`. The exact meaning depends on context, but it is generally used either as end of view indicator by the functions that expect a view index or as the error indicator by the functions that return a view index.

## Example


### Example

```cpp
#include <string_view>

constexpr bool
contains(std::string_view const what, std::string_view const where) noexcept
{
    return std::string_view::npos != where.find(what);
}

int main()
{
    using namespace std::literals;

    static_assert(contains("water", "in a bottle of water"));
    static_assert(!contains("wine", "in a bottle of champagne"));
    static_assert(""sv.npos == "haystack"sv.find("needle"));
}
```


## See also


| cpp/string/basic_string/dsc npos | (see dedicated page) |

