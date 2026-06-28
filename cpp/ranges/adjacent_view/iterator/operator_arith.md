---
title: std::ranges::adjacent_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr /*iterator*/ operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<Base>;
dcl|num=4|since=c++23|
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<Base>;
dcl|num=5|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires ranges::random_access_range<Base>;
```

Increments or decrements the iterator.
Let  be an underlying array of iterators.
1. Equivalent to:

```cpp
for (auto& i : current_)
    i = std::ranges::next(i);
return *this;
```

The behavior is undefined if before the call the `current_.back()` is not incrementable.
2. Equivalent to:

```cpp
auto tmp = *this;
++*this;
return tmp;
```

3. Equivalent to:

```cpp
for (auto& i : current_)
    i = std::ranges::prev(i);
return *this;
```

The behavior is undefined if before the call the `current_.front()` is not decrementable.
4. Equivalent to:

```cpp
auto tmp = *this;
--*this;
return tmp;
```

5. Equivalent to:

```cpp
for (auto& i : current_)
    i = i + n;
return *this;
```

The behavior is undefined if before the call the `current_.back() + n` does not have well-defined behavior.
6. Equivalent to:

```cpp
for (auto& i : current_)
    i = i - n;
return *this;
```

The behavior is undefined if before the call the `current_.front() - n` does not have well-defined behavior.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,3,5,6@ `*this`
@2,4@ A copy of `*this` that was made before the change.

## Example


### Example

```cpp
#include <cassert>
#include <list>
#include <ranges>
#include <utility>
#include <vector>

int main()
{
    {
        auto v = std::vector{0, 1, 2, 3, 4, 5};
        auto i = (v {{!
```

assert((*i == std::pair{0, 1}));
++i;                            // overload (1)
assert((*i == std::pair{1, 2}));
--i;                            // overload (3)
assert((*i == std::pair{0, 1}));
i += 2;                         // overload (5)
assert((*i == std::pair{2, 3}));
i -= 2;                         // overload (6)
assert((*i == std::pair{0, 1}));
}
{
auto v = std::list{0, 1, 2, 3, 4, 5};
auto i = (v | std::views::pairwise).begin();
assert((*i == std::pair{0, 1}));
++i;                            // overload (1)
assert((*i == std::pair{1, 2}));
--i;                            // overload (3)
assert((*i == std::pair{0, 1}));
//      i += 2; // Error: v is not a random_access_range; overload (5)
//      i -= 2; // Error: v is not a random_access_range; overload (6)
}
}

## See also

