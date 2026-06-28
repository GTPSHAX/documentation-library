---
title: std::ranges::range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/range
---

ddcl|header=ranges|since=c++20|1=
template< class T >
concept range = requires( T& t ) {
ranges::begin(t); // equality-preserving for forward iterators
ranges::end (t);
};
The `range` concept defines the requirements of a type that allows iteration over its elements by providing an iterator and sentinel that denote the elements of the range.

## Semantic requirements

Given an expression `E` such that `decltype((E))` is `T`, `T` models `range` only if
* [ranges::begin(E), ranges::end(E)) denotes a range, and
* both `ranges::begin(E)` and `ranges::end(E)` are amortized constant time and do not alter the value of `E` in a manner observable to equality-preserving expressions, and
* if the type of `ranges::begin(E)` models , `ranges::begin(E)` is equality-preserving (in other words, forward iterators support multi-pass algorithms).

## Notes

A typical `range` class only needs to provide two functions:
# A member function `begin()` whose return type models .
# A member function `end()` whose return type models `<It>`, where `It` is the return type of `begin()`.
Alternatively, they can be non-member functions, to be found by argument-dependent lookup.

## Example


### Example

```cpp
#include <ranges>

// A minimum range
struct SimpleRange
{
    int* begin();
    int* end();
};
static_assert(std::ranges::range<SimpleRange>);

// Not a range: no begin/end
struct NotRange
{
    int t {};
};
static_assert(!std::ranges::range<NotRange>);

// Not a range: begin does not return an input_or_output_iterator
struct NotRange2
{
    void* begin();
    int* end();
};
static_assert(!std::ranges::range<NotRange2>);

int main() {}
```


## Defect reports

