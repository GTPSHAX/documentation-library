---
title: std::ranges::common_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_range
---

ddcl|header=ranges|since=c++20|1=
template< class T >
concept common_range =
ranges::range<T> && std::same_as<ranges::iterator_t<T>, ranges::sentinel_t<T>>;
The `common_range` concept is a refinement of  for which `std::ranges::begin()` and `std::ranges::end()` return the same type (e.g. all standard library containers).

## Example


### Example

```cpp
#include <ranges>

struct A
{
    char* begin();
    char* end();
};
static_assert( std::ranges::common_range<A> );

struct B
{
    char* begin();
    bool end();
};  // not a common_range: begin/end have different types
static_assert( not std::ranges::common_range<B> );

struct C
{
    char* begin();
};  // not a common_range, not even a range: has no end()
static_assert( not std::ranges::common_range<C> );

int main() {}
```


## See also


| cpp/ranges/dsc common_view | (see dedicated page) |

