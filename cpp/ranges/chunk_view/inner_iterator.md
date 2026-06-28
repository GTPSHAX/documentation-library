---
title: std::ranges::chunk_view::inner-iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator
---

ddcl|since=c++23|notes=|
class /*inner-iterator*/
The return type of `chunk_view::''outer-iterator''::value_type::begin` if `V` models .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Non-member functions


| cpp/ranges/chunk_view/inner_iterator/operator_cmp|title=operator==|compares the iterator with | |
| cpp/ranges/chunk_view/inner_iterator/operator-|title=operator-|calculates the remained number of elements|notes= | |
| cpp/ranges/chunk_view/inner_iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/chunk_view/inner_iterator/iter_swap|swaps the objects pointed to by two underlying iterators|notes= | |


## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <ranges>
#include <sstream>

int main()
{
    auto letters = std::istringstream{"ABCDEFGHIJK"};

    auto chunks = std::ranges::istream_view<char>(letters)
                {{!
```

for (auto chunk : chunks)
{
// chunk is an object of type chunk_view::outer_iterator::value_type
std::cout << '[';
for (auto inner_iter = chunk.begin(); inner_iter != std::default_sentinel;
++inner_iter)
std::cout << *inner_iter;
std::cout << "] ";
}
std::cout << '\n';
}
|output=
[ABCD] [EFGH] [IJK]

## References


## See also


| cpp/ranges/chunk_view/dsc outer_iterator | (see dedicated page) |
| cpp/ranges/chunk_view/dsc iterator | (see dedicated page) |

