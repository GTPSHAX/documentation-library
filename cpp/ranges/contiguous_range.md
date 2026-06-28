---
title: std::ranges::contiguous_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/contiguous_range
---

ddcl|header = ranges|since=c++20|1=
template< class T >
concept contiguous_range =
ranges::random_access_range<T> &&
std::contiguous_iterator<ranges::iterator_t<T>> &&
requires(T& t) {
{ ranges::data(t) } ->
std::same_as<std::add_pointer_t<ranges::range_reference_t<T>>>;
};
The `contiguous_range` concept is a refinement of  for which `ranges::begin` returns a model of  and the customization point `ranges::data` is usable.

## Semantic requirements

`T` models `contiguous_range` only if given an expression `e` such that `decltype((e))` is `T&`, `1=std::to_address(ranges::begin(e)) == ranges::data(e)`.

## Example


### Example

```cpp
#include <array>
#include <deque>
#include <list>
#include <mdspan>
#include <ranges>
#include <set>
#include <span>
#include <string_view>
#include <valarray>
#include <vector>

template<typename T>
concept CR = std::ranges::contiguous_range<T>;

// zstring being a ranges::contiguous_range doesn't have to be a ranges::sized_range
struct zstring
{
    struct sentinel
    {
        friend constexpr bool operator==(const char* str, sentinel) noexcept
        { return *str == '\0'; }
    };

    const char* str;

    const char* begin() const noexcept { return str; }
    sentinel end() const noexcept { return {}; }
};

int main()
{
    int a[4];
    static_assert(
            CR<std::vector<int>> and
        not CR<std::vector<bool>> and
        not CR<std::deque<int>> and
            CR<std::valarray<int>> and
            CR<decltype(a)> and
        not CR<std::list<int>> and
        not CR<std::set<int>> and
            CR<std::array<std::list<int>,42>> and
            CR<std::string_view> and
            CR<zstring> and
            CR<std::span<const int>> and
        not CR<std::mdspan<int, std::dims<1>>>
    );
}
```


## See also


| cpp/ranges/dsc sized_range | (see dedicated page) |
| cpp/ranges/dsc random_access_range | (see dedicated page) |

