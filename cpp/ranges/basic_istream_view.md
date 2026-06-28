---
title: std::ranges::wistream_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/basic_istream_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< std::movable Val, class CharT,
class Traits = std::char_traits<CharT> >
requires std::default_initializable<Val> &&
/*stream-extractable*/<Val, CharT, Traits>
class basic_istream_view
: public ranges::view_interface<basic_istream_view<Val, CharT, Traits>>
dcl|num=2|since=c++20|1=
template< class Val >
using istream_view = ranges::basic_istream_view<Val, char>;
dcl|num=3|since=c++20|1=
template< class Val >
using wistream_view = ranges::basic_istream_view<Val, wchar_t>;
dcl|num=4|since=c++20|1=
namespace views {
template< class T >
constexpr /* unspecified */ istream = /* unspecified */;
}
dcla|num=5|expos=yes|1=
template< class Val, class CharT, class Traits >
concept /*stream-extractable*/ =
requires(std::basic_istream<CharT, Traits>& is, Val& t) {
is >> t;
};
```

1. A range factory that generates a sequence of elements by repeatedly calling `operator>>`.
@2,3@ Convenience alias templates for character types `char` and `wchar_t`.
4. `views::istream<T>(e)` is expression-equivalent to `ranges::basic_istream_view<T, typename U::char_type, typename U::traits_type>(e)` for any suitable subexpressions `e`, where `U` is `std::remove_reference_t<decltype(e)>`.
@@ The program is ill-formed if `U` is not both publicly and unambiguously derived from `std::basic_istream<typename U::char_type, typename U::traits_type>`, which may result in a substitution failure.
5. The exposition-only concept `/*stream-extractable*/<Val, CharT, Traits>` is satisfied when lvalue of type `Val` can be extracted from lvalue of type `std::basic_istream<CharT, Traits>`.
The iterator type of `basic_istream_view` is move-only: it does not meet the *Iterator* requirements, and thus does not work with pre-C++20 s.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| rrev|until=c++23| | |
| Although  is derived from `ranges::view_interface|std::ranges::view_interface`, it cannot use any of inherited member functions. | |
| member|basic_istream_view| | |
| ddcl|since=c++20|1= | |
| constexpr explicit | |
| basic_istream_view( std::basic_istream<CharT, Traits>& stream ); | |
| Initializes  with `std::addressof(stream)`, and value-initializes . | |
| member|begin| | |
| ddcl|since=c++20| | |
| constexpr auto begin(); | |
| Equivalent to box|`*``>>``; return`}. | |
| member|end| | |
| ddcl|since=c++20| | |
| constexpr std::default_sentinel_t end() const noexcept; | |
| Returns `std::default_sentinel`. | |
| ===Nested classes=== | |


## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <ranges>
#include <sstream>
#include <string>

int main()
{
    auto words = std::istringstream{"today is yesterday’s tomorrow"};
    for (const auto& s : std::views::istream<std::string>(words))
        std::cout << std::quoted(s, '/') << ' ';
    std::cout << '\n';

    auto floats = std::istringstream{"1.1  2.2\t3.3\v4.4\f55\n66\r7.7  8.8"};
    std::ranges::copy
    (
        std::views::istream<float>(floats),
        std::ostream_iterator<float>{std::cout, ", "}
    );
    std::cout << '\n';
}
```


**Output:**
```
/today/ /is/ /yesterday’s/ /tomorrow/
1.1, 2.2, 3.3, 4.4, 55, 66, 7.7, 8.8,
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3568 | C++20 | P2325R3 accidentally made the stored value default-initialized | restored to value-initialization |


## See also


| cpp/iterator/dsc istream_iterator | (see dedicated page) |

