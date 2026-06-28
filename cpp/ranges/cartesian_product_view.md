---
title: std::ranges::views::cartesian_product
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< ranges::input_range First, ranges::forward_range... Vs >
requires (ranges::view<First> && ... && ranges::view<Vs>)
class cartesian_product_view
: public ranges::view_interface<cartesian_product_view<First, Vs...>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /*unspecified*/ cartesian_product = /*unspecified*/;
}
dcl|since=c++23|1=
template< ranges::viewable_range... Rs >
requires /* see below */
constexpr ranges::view auto cartesian_product( Rs&&... rs );
|1=
template< bool Const, class First, class... Vs >
concept /*cartesian-product-is-random-access*/ =
(ranges::random_access_range</*maybe-const*/<Const, First>> && ... &&
(ranges::random_access_range</*maybe-const*/<Const, Vs>> &&
ranges::sized_range</*maybe-const*/<Const, Vs>>));
|1=
template< class R >
concept /*cartesian-product-common-arg*/ =
ranges::common_range<R>
(ranges::sized_range<R> && ranges::random_access_range<R>);
|1=
template< bool Const, class First, class... Vs >
concept /*cartesian-product-is-bidirectional*/ =
(ranges::bidirectional_range</*maybe-const*/<Const, First>> && ... &&
(ranges::bidirectional_range</*maybe-const*/<Const, Vs>> &&
/*cartesian-product-common-arg*/</*maybe-const*/<Const, Vs>>));
|1=
template< class First, class... Vs >
concept /*cartesian-product-is-common*/ =
/*cartesian-product-common-arg*/<First>;
|1=
template< class... Vs >
concept /*cartesian-product-is-sized*/ =
(ranges::sized_range<Vs> && ...);
|1=
template< bool Const, template<class> class FirstSent, class First, class... Vs >
concept /*cartesian-is-sized-sentinel*/ =
(std::sized_sentinel_for<FirstSent</*maybe-const*/<Const, First>>,
ranges::iterator_t</*maybe-const*/<Const, First>>> && ... &&
(ranges::sized_range</*maybe-const*/<Const, Vs>> &&
std::sized_sentinel_for<ranges::iterator_t<
/*maybe-const*/<Const, Vs>>,
ranges::iterator_t</*maybe-const*/<Const, Vs>>>));
|1=
template< /*cartesian-product-common-arg*/ R >
constexpr auto /*cartesian-common-arg-end*/( R& r )
{
if constexpr (ranges::common_range<R>)
return ranges::end(r);
else
return ranges::begin(r) + ranges::distance(r);
}
```

1. `cartesian_product_view` is a range adaptor that takes ''n'' s, where ''n > 0'', and produces a  of tuples calculated by the [Cartesian product#n-ary Cartesian product|n-ary cartesian product](https://en.wikipedia.org/wiki/Cartesian product#n-ary Cartesian product|n-ary cartesian product) of the provided ranges. The size of produced view is a multiple of sizes of provided ranges, while each element is a tuple (of references) of the size ''n''.
2. `views::cartesian_product` is a customization point object.
* When calling with no argument, `views::cartesian_product()` is expression-equivalent to `views::single(std::tuple())`.
* Otherwise, `views::cartesian_product(rs...)` is expression-equivalent to `ranges::cartesian_product_view<views::all_t<decltype((rs))>...>(rs...)`.
3. Determines if `cartesian_product` is a random access range (see also ).
4. Determines if `cartesian_product` is a common range (see also ).
5. Determines if `cartesian_product` is a bidirectional range (see also ).
6. Determines if `cartesian_product` satisfies the helper concept `/*cartesian-product-is-common*/` (see also ).
7. Determines if `cartesian_product` is a sized range (see also ).
8. Determines if `cartesian_product` uses sized sentinel.
9. Returns the end of the produced . Participates in overload resolution only if `cartesian_product` satisfies the helper concept `/*cartesian-product-common-arg*/`.
The `First`  passed to `cartesian_product_view` is treated specially, since it is only passed through a single time. As a result, several constrains are relaxed on it:
* `First` is an  instead of ;
* `First` does not have to be a  in order for the `cartesian_product_view` to be  or ;
* `First` does not have to be  in order for the `cartesian_product_view` to be .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|cartesian_product_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|cartesian_product_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|cartesian_product_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc size|cartesian_product_view | (see dedicated page) |


## 


## Nested classes


## Notes


## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <list>
#include <ranges>
#include <string>
#include <vector>

void print(std::tuple<char const&, int const&, std::string const&> t, int pos)
{
    const auto& [a, b, c] = t;
    std::cout << '(' << a << ' ' << b << ' ' << c << ')' << (pos % 4 ? " " : "\n");
}

int main()
{
    const auto x = std::array{'A', 'B'};
    const auto y = std::vector{1, 2, 3};
    const auto z = std::list<std::string>{"α", "β", "γ", "δ"};

    for (int i{1}; auto const& tuple : std::views::cartesian_product(x, y, z))
        print(tuple, i++);
}
```


**Output:**
```
(A 1 α) (A 1 β) (A 1 γ) (A 1 δ)
(A 2 α) (A 2 β) (A 2 γ) (A 2 δ)
(A 3 α) (A 3 β) (A 3 γ) (A 3 δ)
(B 1 α) (B 1 β) (B 1 γ) (B 1 δ)
(B 2 α) (B 2 β) (B 2 γ) (B 2 δ)
(B 3 α) (B 3 β) (B 3 γ) (B 3 δ)
```


## References


## See also


| cpp/ranges/dsc zip_view | (see dedicated page) |

