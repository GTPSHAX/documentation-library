---
title: std::ranges::views::repeat
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/repeat_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|1=
template< std::move_constructible W,
std::semiregular Bound = std::unreachable_sentinel_t >
requires (std::is_object_v<W> && std::same_as<W, std::remove_cv_t<W>> &&
(/*integer-like-with-usable-difference-type*/<Bound>
std::same_as<Bound, std::unreachable_sentinel_t>))
class repeat_view : public ranges::view_interface<repeat_view<W, Bound>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ repeat = /* unspecified */;
}
dcl|since=c++23|
template< class W >
requires /* see below */
constexpr /* see below */ repeat( W&& value );
dcl|since=c++23|
template< class W, class Bound >
requires /* see below */
constexpr /* see below */ repeat( W&& value, Bound&& bound );
dcla|num=3|expos=yes|1=
concept /*integer-like-with-usable-difference-type*/ =
/*is-signed-integer-like*/<T>
(/*is-integer-like*/ <T> && std::weakly_incrementable<T>)
```

1. A range factory that generates a sequence of elements by repeatedly producing the same value. Can be either bounded or unbounded (infinite).
2. `views::repeat(e)` and `views::repeat(e, f)` are expression-equivalent to `repeat_view<std::decay_t<decltype((E))>>(e)` and `repeat_view(e, f)` respectively for any suitable subexpressions `e` and `f`.
3. Determines whether a type is integer-like and has a usable difference type.
`repeat_view` models . If `Bound` is not `std::unreachable_sentinel_t`, `repeat_view` also models  and .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions

member|repeat_view|2=

```cpp
dcl|num=1|since=c++23|1=
repeat_view() requires std::default_initializable<W> = default;
dcl|num=2|since=c++23|1=
constexpr explicit repeat_view( const W& value, Bound bound = Bound() );
dcl|num=3|since=c++23|1=
constexpr explicit repeat_view( W&& value, Bound bound = Bound() );
dcl|num=4|since=c++23|1=
template < class... WArgs, class... BoundArgs >
requires std::constructible_from<W, WArgs...>
&& std::constructible_from<Bound, BoundArgs...>
constexpr explicit
repeat( std::piecewise_construct_t, std::tuple<WArgs...> value_args,
std::tuple<BoundArgs...> bound_args = std::tuple<>{} );
```

1. Default-initializes  and value-initializes .
2. Initializes  with `value` and initializes  with `bound`.
@@ If `Bound` is not `std::unreachable_sentinel_t` and `1=bool(bound >= 0)` is `false`, the behavior is undefined.
3. Initializes  with `std::move(value)` and initializes  with `bound`.
@@ If `Bound` is not `std::unreachable_sentinel_t` and `1=bool(bound >= 0)` is `false`, the behavior is undefined.
4. Initializes  with `std::make_from_tuple<T>(std::move(value_args))` and  with `std::make_from_tuple<Bound>(std::move(bound_args))`.
@@ If `Bound` is not `std::unreachable_sentinel_t` and `1=bool(bound >= 0)` is `false`, the behavior is undefined.

## Parameters


### Parameters

- `value` - the value to be repeatedly produced
- `bound` - the bound
- `value_args` - the tuple containing the initializers of 
- `bound_args` - the tuple containing the initializers of 
member|begin|2=
ddcl|since=c++23|
constexpr /*iterator*/ begin() const;
Returns .
member|end|2=

```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/ end() const
requires (!std::same_as<Bound, std::unreachable_sentinel_t>);
dcl|num=2|since=c++23|
constexpr std::unreachable_sentinel_t end() const;
```

1. Returns .
2. Returns `std::unreachable_sentinel`.
member|size|2=
ddcl|since=c++23|
constexpr auto size() const
requires (!std::same_as<Bound, std::unreachable_sentinel_t>);
Returns .

## Deduction guides


```cpp
dcl|since=c++23|1=
template< class W, class Bound = std::unreachable_sentinel_t >
repeat_view( W, Bound = Bound() ) -> repeat_view<W, Bound>;
```


## Nested classes


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>
using namespace std::literals;

int main()
{
    // bounded overload
    for (auto s : std::views::repeat("C++"sv, 3))
        std::cout << s << ' ';
    std::cout << '\n';

    // unbounded overload
    for (auto s : std::views::repeat("I know that you know that"sv)
                {{!
```

std::cout << s << ' ';
std::cout << "...\n";
}
|output=
C++ C++ C++
I know that you know that I know that you know that I know that you know that ...

## Defect reports


## See also


| cpp/ranges/dsc iota_view | (see dedicated page) |
| cpp/ranges/dsc views indices | (see dedicated page) |

