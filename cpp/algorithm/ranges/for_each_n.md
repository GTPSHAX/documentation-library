---
title: std::ranges::for_each_n
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges/for_each_n
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< std::input_iterator I, class Proj = std::identity,
std::indirectly_unary_invocable<std::projected<I, Proj>> Fun >
constexpr for_each_n_result<I, Fun>
for_each_n( I first, std::iter_difference_t<I> count,
Fun f, Proj proj = {} );
dcl|num=2|since=c++26|1=
template< /*execution-policy*/ Ep,
std::random_access_iterator I, class Proj = identity,
std::indirectly_unary_invocable<std::projected<I, Proj>> Fun >
I for_each_n( Ep&& policy, I first, iter_difference_t<I> count,
Fun f, Proj proj = {} );
dcl|num=3|since=c++20|1=
template< class I, class F >
using for_each_n_result = ranges::in_fun_result<I, F>;
```

For the definition of `/*execution-policy*/`, see this page.
Applies the given invocable object `f` to each element (projected by `proj`) in the target range [first, ranges::next(first, count)). If `f` returns a result, the result is ignored.
1. `f` is applied in order from `first`.
2. `f` might not be applied in order. The algorithm is executed according to `policy`.
@@ Unlike other , `for_each_n` is not allowed to make arbitrary copies of elements from the target range.
.

## Parameters


### Parameters

- `first` - the beginning of the target range
- `count` - the number of elements in the target range
- `f` - the invocable object to be applied to the (projected) elements
- `proj` - the projection to be applied to the elements
- `policy` - execution policy

## Return value

1. }
2. `ranges::next(first, count)`

## Complexity

Exactly `count` applications of `f` and `proj`.

## Exceptions

2.

## Notes

If the projection returns a mutable reference, `f` may modify the elements in the target range.

## Possible implementation


```cpp
struct for_each_n_fn
{
    template<std::input_iterator I, class Proj = std::identity,
             std::indirectly_unary_invocable<std::projected<I, Proj>> Fun>
    constexpr for_each_n_result<I, Fun>
        operator()(I first, std::iter_difference_t<I> count,
                   Fun fun, Proj proj = Proj{}) const
    {
        for (; count-- > 0; ++first)
            std::invoke(fun, std::invoke(proj, *first));
        return {std::move(first), std::move(fun)};
    }
};

inline constexpr for_each_n_fn for_each_n{};
```


## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <ranges>
#include <string_view>

struct P
{
    int first;
    char second;
    friend std::ostream& operator<<(std::ostream& os, const P& p)
    {
        return os << '{' << p.first << ",'" << p.second << "'}";
    }
};

auto print = [](std::string_view name, const auto& v)
{
    std::cout << name << ": ";
    for (auto n = v.size(); const auto& e : v)
        std::cout << e << (--n ? ", " : "\n");
};

int main()
{
    std::array a {1, 2, 3, 4, 5};
    print("a", a);
    // Negate first three numbers:
    std::ranges::for_each_n(a.begin(), 3, [](auto& n) { n *= -1; });
    print("a", a);

    std::array s { P{1,'a'}, P{2, 'b'}, P{3, 'c'}, P{4, 'd'} };
    print("s", s);
    // Negate data members “P::first” using projection:
    std::ranges::for_each_n(s.begin(), 2, [](auto& x) { x *= -1; }, &P::first);
    print("s", s);
    // Capitalize data members “P::second” using projection:
    std::ranges::for_each_n(s.begin(), 3, [](auto& c) { c -= 'a' - 'A'; }, &P::second);
    print("s", s);
}
```


**Output:**
```
a: 1, 2, 3, 4, 5
a: -1, -2, -3, 4, 5
s: {1,'a'}, {2,'b'}, {3,'c'}, {4,'d'}
s: {-1,'a'}, {-2,'b'}, {3,'c'}, {4,'d'}
s: {-1,'A'}, {-2,'B'}, {3,'C'}, {4,'d'}
```


## See also


| cpp/algorithm/dsc for_each_n | (see dedicated page) |
| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/language/dsc range-for | (see dedicated page) |

