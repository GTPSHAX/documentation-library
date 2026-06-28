---
title: std::ranges::views::empty
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/empty_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template<class T>
requires std::is_object_v<T>
class empty_view : public ranges::view_interface<empty_view<T>>
dcl|num=2|since=c++20|1=
namespace views {
template<class T>
constexpr empty_view<T> empty{};
}
```

1. A range factory that produces a  of no elements of a particular type.
2. Variable template for `empty_view`.

## Member functions

member|begin|
ddcl|since=c++20|
static constexpr T* begin() noexcept { return nullptr; }
`empty_view` does not reference any element.
member|end|
ddcl|since=c++20|
static constexpr T* end() noexcept { return nullptr; }
`empty_view` does not reference any element.
member|data|
ddcl|since=c++20|
static constexpr T* data() noexcept { return nullptr; }
`empty_view` does not reference any element.
member|size|
ddcl|since=c++20|
static constexpr std::size_t size() noexcept { return 0; }
`empty_view` is always empty.
member|empty|
ddcl|since=c++20|
static constexpr bool empty() noexcept { return true; }
`empty_view` is always empty.

## Helper templates

ddcl|since=c++20|1=
template<class T>
constexpr bool ranges::enable_borrowed_range<ranges::empty_view<T>> = true;
This specialization of `ranges::enable_borrowed_range` makes `empty_view` satisfy .

## Notes

Although `empty_view` obtains `front`, `back`, and `operator[]` member functions from `view_interface`, calls to them always result in undefined behavior since an `empty_view` is always empty.
The inherited `operator bool` conversion function always returns `false`.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    namespace ranges = std::ranges;

    ranges::empty_view<long> e;
    static_assert(ranges::empty(e)); // uses operator bool
    static_assert(0 == e.size());
    static_assert(nullptr == e.data());
    static_assert(nullptr == e.begin());
    static_assert(nullptr == e.end());
    static_assert(nullptr == e.cbegin());
    static_assert(nullptr == e.cend());
}
```


## See also


| cpp/utility/dsc optional | (see dedicated page) |
| cpp/ranges/dsc single_view | (see dedicated page) |
| cpp/ranges/dsc all_view | (see dedicated page) |
| cpp/ranges/dsc ref_view | (see dedicated page) |

