---
title: std::ranges::views::single
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/single_view
---


```cpp
**Header:** `<`ranges`>`
dcl rev multi|num=1|since1=c++20|dcl1=
template< std::copy_constructible T >
requires std::is_object_v<T>
class single_view
: public ranges::view_interface<single_view<T>>
|since2=c++23|dcl2=
template< std::move_constructible T >
requires std::is_object_v<T>
class single_view
: public ranges::view_interface<single_view<T>>
dcl|num=2|since=c++20|1=
namespace views {
inline constexpr /* unspecified */ single = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ single( T&& t );
```

1. Produces a  that contains exactly one element of a specified value.
2. The expression `views::single(e)` is expression-equivalent to `single_view<std::decay_t<decltype((e))>>(e)` for any suitable subexpression `e`.
The lifetime of the element is bound to the parent `single_view`. Copying `single_view` makes a copy of the element.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|spec=rrev multi|until1=c++23 | |
| |rev1=`<T>` | |
| |rev2=`<T>`|value_|the single element of the view | |


## Member functions

member|single_view|

```cpp
dcl|num=1|since=c++20|1=
single_view() requires std::default_initializable<T> = default;
dcl rev multi|num=2|since1=c++20|dcl1=
constexpr explicit single_view( const T& t );
|since2=c++23|dcl2=
constexpr explicit single_view( const T& t )
requires std::copy_constructible<T>;
dcl|num=3|since=c++20|1=
constexpr explicit single_view( T&& t );
dcl|num=4|since=c++20|1=
template< class... Args >
requires std::constructible_from<T, Args...>
constexpr explicit single_view( std::in_place_t, Args&&... args );
```

Constructs a `single_view`.
1. Default initializes , which value-initializes its contained value.
2. Initializes  with `t`.
3. Initializes  with `std::move(t)`.
4. Initializes  as if by box|}.
member|begin|
ddcl|since=c++20|
constexpr T* begin() noexcept;
constexpr const T* begin() const noexcept;
Equivalent to `return data();`.
member|end|
ddcl|since=c++20|
constexpr T* end() noexcept;
constexpr const T* end() const noexcept;
Equivalent to `return data() + 1;`.
member|empty|
ddcl|since=c++20|
static constexpr bool empty() noexcept;
Equivalent to `return false;`.
member|size|
ddcl|since=c++20|
static constexpr std::size_t size() noexcept;
Equivalent to `return 1;`.
Makes `single_view` model `/*tiny-range*/` as required by `split_view`.
member|data|
ddcl|since=c++20|
constexpr T* data() noexcept;
constexpr const T* data() const noexcept;
Returns a pointer to the contained value of . The behavior is undefined if  does not contains a value.

## Deduction guides

ddcl|since=c++20|1=
template< class T >
single_view( T ) -> single_view<T>;

## Notes

For a , the inherited `empty` member function always returns `false`, and the inherited `operator bool` conversion function always returns `true`.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <ranges>
#include <string>
#include <tuple>

int main()
{
    constexpr std::ranges::single_view sv1{3.1415}; // uses (const T&) constructor
    static_assert(sv1);
    static_assert(not sv1.empty());

    std::cout << "1) *sv1.data(): " << *sv1.data() << '\n'
              << "2) *sv1.begin(): " << *sv1.begin() << '\n'
              << "3)  sv1.size(): " << sv1.size() << '\n'
              << "4)  distance: " << std::distance(sv1.begin(), sv1.end()) << '\n';

    std::string str{"C++20"};
    std::cout << "5)  str = " << std::quoted(str) << '\n';
    std::ranges::single_view sv2{std::move(str)}; // uses (T&&) constructor
    std::cout << "6) *sv2.data(): " << std::quoted(*sv2.data()) << '\n'
              << "7)  str = " << std::quoted(str) << '\n';

    std::ranges::single_view<std::tuple<int, double, std::string>>
        sv3{std::in_place, 42, 3.14, "😄"}; // uses (std::in_place_t, Args&&... args)

    std::cout << "8)  sv3 holds a tuple: { "
              << std::get<0>(sv3[0]) << ", "
              << std::get<1>(sv3[0]) << ", "
              << std::get<2>(sv3[0]) << " }\n";
}
```


**Output:**
```
1) *sv1.data(): 3.1415
2) *sv1.begin(): 3.1415
3)  sv1.size(): 1
4)  distance: 1
5)  str = "C++20"
6) *sv2.data(): "C++20"
7)  str = ""
8)  sv3 holds a tuple: { 42, 3.14, 😄 }
```


## Defect reports


## See also


| cpp/utility/dsc optional | (see dedicated page) |
| cpp/ranges/dsc empty_view | (see dedicated page) |
| cpp/ranges/dsc split_view | (see dedicated page) |

