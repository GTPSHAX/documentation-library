---
title: std::basic_string_view::remove_prefix
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/remove_prefix
---

ddcl|since=c++17|
constexpr void remove_prefix( size_type n );
Moves the start of the view forward by `n` characters.

## Parameters


### Parameters

- `n` - number of characters to remove from the start of the view

## Complexity

Constant.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string_view>

using namespace std::literals;

[[nodiscard("a pure function")]]
constexpr std::size_t count_substrings(std::string_view hive, const std::string_view bee)
{
    if (hive.empty() {{!!
```

return 0U;
std::size_t buzz{};
while (bee.size() <= hive.size())
{
const auto pos = hive.find(bee);
if (pos == hive.npos)
break;
++buzz;
hive.remove_prefix(pos + bee.size());
}
return buzz;
}
int main()
{
std::string str = "   trim me";
std::string_view v = str;
v.remove_prefix(std::min(v.find_first_not_of(" "), v.size()));
std::cout << "String: '" << str << "'\n"
<< "View  : '" << v << "'\n";
constexpr auto hive{"bee buzz bee buzz bee"};
std::cout << "There are " << count_substrings(hive, "bee") << " bees in this hive.\n";
}
|output=
String: '   trim me'
View  : 'trim me'
There are 3 bees in this hive.

## See also


| cpp/string/basic_string_view/dsc remove_suffix | (see dedicated page) |

