---
title: std::ranges::join_with_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/ operator++( int )
requires std::is_reference_v</*InnerBase*/> &&
ranges::forward_range</*Base*/> &&
ranges::forward_range</*InnerBase*/>;
dcl|num=4|since=c++23|
constexpr /*iterator*/& operator--()
requires std::is_reference_v</*InnerBase*/> &&
ranges::bidirectional_range</*Base*/> &&
ranges::bidirectional_range</*InnerBase*/> &&
ranges::common_range</*InnerBase*/> &&
ranges::bidirectional_range</*PatternBase*/> &&
ranges::common_range</*PatternBase*/>;
dcl|num=5|since=c++23|
constexpr /*iterator*/ operator--( int )
requires std::is_reference_v</*InnerBase*/> &&
ranges::bidirectional_range</*Base*/> &&
ranges::bidirectional_range</*InnerBase*/> &&
ranges::common_range</*InnerBase*/> &&
ranges::bidirectional_range</*PatternBase*/> &&
ranges::common_range</*PatternBase*/>;
```

Increments or decrements the iterator.
1. Increments the `inner iterator` as if by box|}`);`.
@@ After that, adjusts the inner and outer iterators as follows:
* If the incremented inner iterator is the past-the-end iterator of the pattern range, it is set to an iterator to the beginning of the next inner range.
* If the incremented inner iterator is the past-the-end iterator of an inner range, the outer iterator is incremented. Then:
:* If the incremented outer iterator is not the past-the-end iterator of the outer range, the inner iterator is set to an iterator to the beginning of the pattern range.
:* Otherwise, if  is `true`, the inner iterator is set to a pattern iterator holding a singular value.
* Repeats the operations above until either the inner iterator is not a past-the-end iterator, or the outer iterator is a past-the-end iterator.
2. Equivalent to `++*this;`.
3. Equivalent to .
4. If the outer iterator is the past-the-end iterator of the outer range, decrements it and sets the inner iterator to the past-the-end iterator of the last inner range, otherwise do nothing.
@@ After that, adjusts the inner and outer iterators as follows:
* If the inner iterator refers to the beginning of an inner range, it is set to the past-the-end iterator of the pattern range.
* If the inner iterator refers to the beginning of the pattern range, the outer iterator is decremented, and the inner iterator is set to the past-the-end iterator of the previous inner range.
* Repeats the operations above until the inner iterator does not refer to the beginning of any range.
@@ Finally, decrements the inner iterator as if by box|}`);`.
5. Equivalent to .

## Return value

@1,4@ `*this`
@3,5@ A copy of `*this` that was made before the change.
