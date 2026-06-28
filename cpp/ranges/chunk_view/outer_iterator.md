---
title: std::ranges::chunk_view::outer-iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/outer_iterator
---

ddcl|since=c++23|notes=|
class /*outer-iterator*/
The return type of `chunk_view::begin` if `V` models .

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Non-member functions


| cpp/ranges/chunk_view/outer_iterator/operator_cmp|title=operator==|compares the iterator with | |
| cpp/ranges/chunk_view/outer_iterator/operator-|title=operator-|calculates the number of chunks remaining|notes= | |


## Nested classes


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <ranges>
#include <sstream>

int main()
{
    const std::string source{"ABCDEFGHIJ"};

    auto letters = std::istringstream{source};
    auto chunks = std::ranges::istream_view<char>(letters)
                {{!
```

for (auto outer_iter = chunks.begin(); outer_iter != std::default_sentinel;
++outer_iter)
{
auto chunk = *outer_iter; // chunk is an object of type
// chunk_view::outer_iterator::value_type
std::cout << '[';
for (auto inner_iter = chunk.begin(); inner_iter != std::default_sentinel;
++inner_iter)
std::cout << *inner_iter;
std::cout << "] ";
}
std::cout << '\n';
// The same output using range-for loops
auto letters2 = std::istringstream{source};
auto chunks2 = std::ranges::istream_view<char>(letters2)
| std::views::chunk(4);
for (auto chunk : chunks2)
{
std::cout << '[';
for (auto ch : chunk)
std::cout << ch;
std::cout << "] ";
}
std::cout << '\n';
}
|output=
[ABCD] [EFGH] [IJ]
[ABCD] [EFGH] [IJ]

## References


## See also


| cpp/ranges/chunk_view/dsc iterator | (see dedicated page) |

