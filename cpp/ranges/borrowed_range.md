---
title: std::ranges::enable_borrowed_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/borrowed_range
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< class R >
concept borrowed_range =
ranges::range<R> &&
(std::is_lvalue_reference_v<R>
ranges::enable_borrowed_range<std::remove_cvref_t<R>>);
dcl|num=2|since=c++20|1=
template< class R >
constexpr bool enable_borrowed_range = false;
```

1. The concept `borrowed_range` defines the requirements of a range such that a function can take it by value and return iterators obtained from it without danger of dangling.
2. The `enable_borrowed_range` variable template is used to indicate whether a  is a `borrowed_range`. The primary template is defined as `false`.

## Semantic requirements

Let `U` be `std::remove_reference_t<T>` if `T` is an rvalue reference type, and `T` otherwise. Given a variable `u` of type `U`, `T` models `borrowed_range` only if the validity of iterators obtained from `u` is not tied to the lifetime of that variable.

## Specializations

A program may specialize `enable_borrowed_range` to `true` for cv-unqualified s which model `borrowed_range`, and `false` for types which do not. Such specializations shall be usable in  and have type `const bool`.

### Unconditionally borrowed ranges in the standard library

Specializations of `enable_borrowed_range` for all specializations of the following standard templates are defined as `true`:
* `cpp/string/basic_string_view#Helper templates|std::basic_string_view`
* `cpp/container/span#Helper templates|std::span`
* `cpp/ranges/subrange#Helper templates|std::ranges::subrange`
* `cpp/ranges/ref_view#Helper templates|std::ranges::ref_view`
* `cpp/ranges/empty_view#Helper templates|std::ranges::empty_view`
* `cpp/ranges/iota_view#Helper templates|std::ranges::iota_view`

### Conditionally borrowed ranges in the standard library

Specialization of `enable_borrowed_range` for the following standard range adaptors are defined as `true` if and only if `std::ranges::enable_borrowed_range<V>` is `true`, where `V` is the underlying view type:
rrev|since=c++23|
* `cpp/ranges/adjacent_view#Helper templates|std::ranges::adjacent_view`
* `cpp/ranges/as_const_view#Helper templates|std::ranges::as_const_view`
* `cpp/ranges/as_rvalue_view#Helper templates|std::ranges::as_rvalue_view`
* `cpp/ranges/chunk_view#Helper templates|std::ranges::chunk_view`
* `cpp/ranges/common_view#Helper templates|std::ranges::common_view`
* `cpp/ranges/drop_view#Helper templates|std::ranges::drop_view`
* `cpp/ranges/drop_while_view#Helper templates|std::ranges::drop_while_view`
* `cpp/ranges/elements_view#Helper templates|std::ranges::elements_view`
rrev|since=c++23|
* `cpp/ranges/enumerate_view#Helper templates|std::ranges::enumerate_view`
* `cpp/ranges/owning_view#Helper templates|std::ranges::owning_view`
* `cpp/ranges/reverse_view#Helper templates|std::ranges::reverse_view`
rrev|since=c++23|
* `cpp/ranges/slide_view#Helper templates|std::ranges::slide_view`
* `cpp/ranges/stride_view#Helper templates|std::ranges::stride_view`
* `cpp/ranges/take_view#Helper templates|std::ranges::take_view`
rrev|since=c++26|
* `cpp/ranges/as_input_view#Helper templates|std::ranges::as_input_view`
rrev|since=c++23|
Specialization of `enable_borrowed_range` for the following standard range adaptors are defined as `true` if and only if `(std::ranges::enable_borrowed_range<Vs> && ...)` is `true`, where `Vs...` are all view types it adapts:
* `cpp/ranges/zip_view#Helper templates|std::ranges::zip_view`

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cstddef>
#include <iostream>
#include <ranges>
#include <span>
#include <type_traits>

template<typename T, std::size_t N>
struct MyRange : std::array<T, N> {};

template<typename T, std::size_t N>
constexpr bool std::ranges::enable_borrowed_range<MyRange<T, N>> = false;

template<typename T, std::size_t N>
struct MyBorrowedRange : std::span<T, N> {};

template<typename T, std::size_t N>
constexpr bool std::ranges::enable_borrowed_range<MyBorrowedRange<T, N>> = true;

int main()
{
    static_assert(std::ranges::range<MyRange<int, 8>>);
    static_assert(std::ranges::borrowed_range<MyRange<int, 8>> == false);
    static_assert(std::ranges::range<MyBorrowedRange<int, 8>>);
    static_assert(std::ranges::borrowed_range<MyBorrowedRange<int, 8>> == true);

    auto getMyRangeByValue = []{ return MyRange<int, 4>{<!---->{1, 2, 42, 3}<!---->}; };
    auto dangling_iter = std::ranges::max_element(getMyRangeByValue());
    static_assert(std::is_same_v<std::ranges::dangling, decltype(dangling_iter)>);
    // *dangling_iter; // compilation error (i.e. dangling protection works.)

    auto my = MyRange<int, 4>{<!---->{1, 2, 42, 3}<!---->};
    auto valid_iter = std::ranges::max_element(my);
    std::cout << *valid_iter << ' '; // OK: 42

    auto getMyBorrowedRangeByValue = []
    {
        static int sa[4]{1, 2, 42, 3};
        return MyBorrowedRange<int, std::size(sa)>{sa};
    };
    auto valid_iter2 = std::ranges::max_element(getMyBorrowedRangeByValue());
    std::cout << *valid_iter2 << '\n'; // OK: 42
}
```


**Output:**
```
42 42
```


## See also


| cpp/ranges/dsc dangling | (see dedicated page) |

