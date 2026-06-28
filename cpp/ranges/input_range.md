---
title: std::ranges::input_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/input_range
---

ddcl|header = ranges|since=c++20|1=
template< class T >
concept input_range =
ranges::range<T> && std::input_iterator<ranges::iterator_t<T>>;
The `input_range` concept is a refinement of  for which `ranges::begin` returns a model of .
