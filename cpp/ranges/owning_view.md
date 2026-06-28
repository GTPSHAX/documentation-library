---
title: std::ranges::owning_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/owning_view
---

ddcl|header=ranges|since=c++20|
template< ranges::range R >
requires std::movable<R> && (!/*is-initializer-list*/<R>)
class owning_view
: public ranges::view_interface<owning_view<R>>
`owning_view` is a  that has unique ownership of a . It is move-only and stores that `range` within it.
The constant `/*is-initializer-list*/<R>` in the `requires` clause is `true` if and only if `std::remove_cvref_t<R>` is a specialization of `std::initializer_list`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|owning_view|2=

```cpp
dcl|num=1|since=c++20|1=
owning_view() requires std::default_initializable<R> = default;
dcl|num=2|since=c++20|1=
owning_view( owning_view&& other ) = default;
dcl|num=3|since=c++20|
constexpr owning_view( R&& t );
```

1. Default constructor. Value-initializes  by its default member initializer (`1== R()`).
2. Move constructor. Move constructs  from that of `other`.
3. Move constructs  from `t`.

## Parameters


### Parameters

- `other` - another `owning_view` to move from
- `t` - range to move from

## Notes

`owning_view` does not explicitly define a copy constructor. `owning_view` is move-only.
member|operator|
ddcl|since=c++20|1=
owning_view& operator=( owning_view&& other ) = default;
Move assignment operator. Move assigns  from that of `other`.

## Parameters


### Parameters

- `other` - another `owning_view` to move from

## Return value

`*this`

## Notes

`owning_view` does not explicitly define a copy assignment operator. `owning_view` is move-only.
member|base|

```cpp
dcl|num=1|since=c++20|
constexpr R& base() & noexcept;
dcl|num=2|since=c++20|
constexpr const R& base() const & noexcept;
dcl|num=3|since=c++20|
constexpr R&& base() && noexcept;
dcl|num=4|since=c++20|
constexpr const R&& base() const && noexcept;
```

Returns a reference to the stored range, keeping value category and const-qualification.

## Return value

@1,2@
@3,4@
member|begin|

```cpp
dcl|num=1|since=c++20|
constexpr ranges::iterator_t<R> begin();
dcl|num=2|since=c++20|
constexpr auto begin() const requires ranges::range<const R>;
```

Returns .
member|end|

```cpp
dcl|num=1|since=c++20|
constexpr ranges::sentinel_t<R> end();
dcl|num=2|since=c++20|
constexpr auto end() const requires ranges::range<const R>;
```

Returns .
member|empty|

```cpp
dcl|num=1|since=c++20|
constexpr bool empty() requires requires { ranges::empty(r_); };
dcl|num=2|since=c++20|
constexpr bool empty() const requires requires { ranges::empty(r_); };
```

Returns .
member|size|

```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<R>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const R>;
```

Returns .
member|reserve_hint|

```cpp
dcl|num=1|since=c++26|
constexpr auto reserve_hint()
requires ranges::approximately_sized_range<R>;
dcl|num=2|since=c++26|
constexpr auto reserve_hint() const
requires ranges::approximately_sized_range<const R>;
```

Returns .
member|data|

```cpp
dcl|num=1|since=c++20|
constexpr auto data() requires ranges::contiguous_range<R>;
dcl|num=2|since=c++20|
constexpr auto data() const requires ranges::contiguous_range<const R>;
```

Returns .

## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<std::ranges::owning_view<T>> =
ranges::enable_borrowed_range<T>;
This specialization of `ranges::enable_borrowed_range` makes `owning_view` satisfy  when the underlying range satisfies it.

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <ranges>
#include <string>

int main()
{
    using namespace std::literals;
    std::ranges::owning_view ov{"cosmos"s}; // the deduced type of R is std::string;
                                            // “ov” is the only owner of this string
    assert(
        ov.empty() == false &&
        ov.size() == 6 &&
        ov.size() == ov.base().size() &&
        ov.front() == 'c' &&
        ov.front() == *ov.begin() &&
        ov.back() == 's' &&
        ov.back() == *(ov.end() - 1) &&
        ov.data() == ov.base()
    );

    std::cout << "sizeof(ov): " << sizeof ov << '\n' // typically equal to sizeof(R)
              << "range-for: ";
    for (const char ch : ov)
        std::cout << ch;
    std::cout << '\n';

    std::ranges::owning_view<std::string> ov2;
    assert(ov2.empty());
//  ov2 = ov; // compile-time error: copy assignment operator is deleted
    ov2 = std::move(ov); // OK
    assert(ov2.size() == 6);
}
```


**Output:**
```
sizeof(ov): 32
range-for: cosmos
```


## See also


| cpp/ranges/dsc ref_view | (see dedicated page) |
| cpp/ranges/dsc all_view | (see dedicated page) |

