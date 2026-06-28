---
title: std::ranges::adjacent_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator
---

ddcla|since=c++23|expos=yes|
template< bool Const >
class /*iterator*/
The return type of `adjacent_view::begin`, and of `adjacent_view::end` when the underlying view `V` is a .
The type `/*iterator*/<true>` is returned by the const-qualified overloads. The type `/*iterator*/<false>` is returned by the non-const-qualified overloads.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::random_access_iterator_tag`, if  models . Otherwise, | |
| * `std::bidirectional_iterator_tag`, if  models . Otherwise, | |
| * `std::forward_iterator_tag`. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|adjacent_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/adjacent_view/iterator/operator_cmp|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares the underlying iterators|notes= | |
| cpp/ranges/adjacent_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |
| cpp/ranges/adjacent_view/iterator/iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| cpp/ranges/adjacent_view/iterator/iter_swap|swaps the objects pointed to by two underlying iterators|notes= | |


## Example


### Example

```cpp
#include <cassert>
#include <concepts>
#include <list>
#include <ranges>
#include <tuple>
#include <utility>
#include <vector>

int main()
{
    auto v = std::vector{0, 1, 2, 3, 4, 5};
    auto i = (v {{!
```

using I = decltype(i);
static_assert(std::same_as<I::value_type, std::tuple<int, int, int>>);
static_assert(std::same_as<I::iterator_concept, std::random_access_iterator_tag>);
// some of available operators:
++i; i++; --i; i--; i += 2; i -= 2;
assert(i[2] == std::tuple(2, 3, 4));
using DI = decltype(*i);
static_assert(std::same_as<DI, std::tuple<int&, int&, int&>>);
std::get<1>(*i) = 42; // modifies v[1] via iterator i
assert(v[1] == 42);
auto l = std::list{0, 1, 2, 3, 4, 5};
auto j = (l | std::views::adjacent<3>).begin();
using J = decltype(j);
static_assert(std::same_as<J::value_type, std::tuple<int, int, int>>);
static_assert(std::same_as<J::iterator_concept, std::bidirectional_iterator_tag>);
++j; --j; j++; j--; // some of available operators
// j += 2; j -= 2;       // error: these operator are not available
// std::ignore() = j[1]; //        for bidirectional iterator
}

## References


## See also


| <!-- | |
| cpp/ranges/adjacent_transform_view/dsc iterator | (see dedicated page) |
| --> | |

