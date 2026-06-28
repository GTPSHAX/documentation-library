---
title: std::ranges::viewable_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/viewable_range
---

ddcl|header=ranges|since=c++20|1=
template< class T >
concept viewable_range =
ranges::range<T> &&
((ranges::view<std::remove_cvref_t<T>> &&
std::constructible_from<std::remove_cvref_t<T>, T>)
(!ranges::view<std::remove_cvref_t<T>> &&
(std::is_lvalue_reference_v<T>
(std::movable<std::remove_reference_t<T>> && !/*is-initializer-list*/<T>))));
The `viewable_range` concept is a refinement of  that describes a range that can be converted into a  through `cpp/ranges/all_view|views::all`.
The constant `/*is-initializer-list*/<T>` is `true` if and only if `std::remove_cvref_t<T>` is a specialization of `std::initializer_list`.

## Example


### Example

```cpp
#include <ranges>
#include <string>
#include <vector>

struct valid_result {};
struct invalid_result {};

template <typename T>
concept valid_viewable_range = std::same_as<T, valid_result>;

template <typename T>
concept invalid_viewable_range = std::same_as<T, invalid_result>;

auto test_viewable_range(std::ranges::viewable_range auto &&) -> valid_result;
auto test_viewable_range(auto&&) -> invalid_result;

int main()
{
    auto il = {1, 2, 3};
    int arr []{1, 2, 3};
    std::vector vec{1, 2, 3};
    std::ranges::ref_view r{arr};
    std::ranges::owning_view o{std::string("Hello")};

    static_assert(requires {
        { test_viewable_range(il) } -> valid_viewable_range;
        { test_viewable_range(std::move(il)) } -> invalid_viewable_range;
        { test_viewable_range(arr) } -> valid_viewable_range;
        { test_viewable_range(std::move(arr)) } -> invalid_viewable_range;
        { test_viewable_range(vec) } -> valid_viewable_range;
        { test_viewable_range(std::move(vec)) } -> valid_viewable_range;
        { test_viewable_range(r) } -> valid_viewable_range;
        { test_viewable_range(std::move(r)) } -> valid_viewable_range;
        { test_viewable_range(o) } -> invalid_viewable_range;
        { test_viewable_range(std::move(o)) } -> valid_viewable_range;
        { test_viewable_range(std::ranges::ref_view(o)) } -> valid_viewable_range;
    });
}
```


## Defect reports


## See also


| cpp/ranges/dsc all_view | (see dedicated page) |

