---
title: std::ranges::output_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/output_range
---

ddcl|header = ranges|since=c++20|1=
template<class R, class T>
concept output_range =
ranges::range<R> && std::output_iterator<ranges::iterator_t<R>, T>;
The `output_range` concept is a refinement of  for which `ranges::begin` returns a model of .
