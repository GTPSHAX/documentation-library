---
title: std::swap(std::match_results)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/swap2
---


# swapsmall|(std::match_results)

ddcl|header=regex|since=c++11|
template< class BidirIt, class Alloc >
void swap( match_results<BidirIt,Alloc>& x1,
match_results<BidirIt,Alloc>& x2 ) noexcept;
Specializes the `std::swap` algorithm for `std::match_results`. Exchanges the contents of `x1` with those of `x2`. Effectively calls `x1.swap(x2)`.

## Parameters


### Parameters

- `x1, x2` - the match_results objects whose contents will be swapped

**Type requirements:**

- `BidirIt`
- `Alloc`

## Return value

(none)

## Example

