---
title: std::ranges::empty
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/empty
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /*unspecified*/ {
inline constexpr auto empty = /*unspecified*/;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr bool empty( T&& t );
```

Determines whether or not `t` has any elements.
A call to `ranges::empty` is expression-equivalent to:
# `bool(t.empty())`, if that expression is valid.
# Otherwise, `1=(ranges::size(t) == 0)`, if that expression is valid.
# Otherwise, `1=bool(ranges::begin(t) == ranges::end(t))`, if that expression is valid and `decltype(ranges::begin(t))` models `std::forward_iterator`.
In all other cases, a call to `ranges::empty` is ill-formed, which can result in substitution failure when `ranges::empty(t)` appears in the immediate context of a template instantiation.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <vector>

template<std::ranges::input_range R>
void print(char id, R&& r)
{
    if (std::ranges::empty(r))
    {
        std::cout << '\t' << id << ") Empty\n";
        return;
    }

    std::cout << '\t' << id << ") Elements:";
    for (const auto& element : r)
        std::cout << ' ' << element;
    std::cout << '\n';
}

int main()
{
    {
        auto v = std::vector<int>{1, 2, 3};
        std::cout << "(1) ranges::empty uses std::vector::empty:\n";
        print('a', v);

        v.clear();
        print('b', v);
    }
    {
        std::cout << "(2) ranges::empty uses ranges::size(initializer_list):\n";
        auto il = {7, 8, 9};
        print('a', il);

        print('b', std::initializer_list<int>{});
    }
    {
        std::cout << "(2) ranges::empty on a raw array uses ranges::size:\n";
        int array[] = {4, 5, 6}; // array has a known bound
        print('a', array);
    }
    {
        struct Scanty : private std::vector<int>
        {
            using std::vector<int>::begin;
            using std::vector<int>::end;
            using std::vector<int>::push_back;
            // Note: both empty() and size() are hidden
        };

        std::cout << "(3) calling ranges::empty on an object w/o empty() or size():\n";
        Scanty y;
        print('a', y);
        y.push_back(42);
        print('b', y);
    }
}
```


**Output:**
```
(1) ranges::empty uses std::vector::empty:
        a) Elements: 1 2 3
        b) Empty
(2) ranges::empty uses ranges::size(initializer_list):
        a) Elements: 7 8 9
        b) Empty
(2) ranges::empty on a raw array uses ranges::size:
        a) Elements: 4 5 6
(3) calling ranges::empty on an object w/o empty() or size():
        a) Empty
        b) Elements: 42
```


## See also


| cpp/iterator/dsc empty | (see dedicated page) |

