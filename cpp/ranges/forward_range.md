---
title: std::ranges::forward_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/forward_range
---

ddcl|header=ranges|since=c++20|1=
template< class T >
concept forward_range =
ranges::input_range<T> && std::forward_iterator<ranges::iterator_t<T>>;
The `forward_range` concept is a refinement of  for which `ranges::begin` returns a model of .

## Example


### Example

```cpp
#include <forward_list>
#include <queue>
#include <ranges>
#include <span>
#include <stack>
#include <tuple>

const char* str{"not a forward range"};
const char str2[] = "a forward range";
static_assert(
    std::ranges::forward_range<decltype("a forward range")> &&
    !std::ranges::forward_range<decltype(str)> &&
    std::ranges::forward_range<decltype(str2)> &&
    !std::ranges::forward_range<std::stack<char>> &&
    std::ranges::forward_range<std::forward_list<char>> &&
    !std::ranges::forward_range<std::tuple<std::forward_list<char>>> &&
    std::ranges::forward_range<std::span<char>> &&
    !std::ranges::forward_range<std::queue<char>> &&
"");

int main() {}
```

