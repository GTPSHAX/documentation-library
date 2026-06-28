---
title: std::regex_token_iterator::regex_token_iterator
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_token_iterator/regex_token_iterator
---


```cpp
dcl|num=1|since=c++11|1=
regex_token_iterator();
dcl|num=2|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type& re,
int submatch = 0,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default );
dcl|num=3|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type& re,
const std::vector<int>& submatches,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default );
dcl|num=4|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type& re,
std::initializer_list<int> submatches,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default );
dcl|num=5|since=c++11|1=
template< std::size_t N >
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type& re,
const int (&submatches)[N],
std::regex_constants::match_flag_type m =
std::regex_constants::match_default );
dcl|num=6|since=c++11|1=
regex_token_iterator( const regex_token_iterator& other );
dcl|num=7|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type&& re,
int submatch = 0,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default ) = delete;
dcl|num=8|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type&& re,
const std::vector<int>& submatches,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default ) = delete;
dcl|num=9|since=c++11|1=
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type&& re,
std::initializer_list<int> submatches,
std::regex_constants::match_flag_type m =
std::regex_constants::match_default ) = delete;
dcl|num=10|since=c++11|1=
template< std::size_t N >
regex_token_iterator( BidirIt a, BidirIt b,
const regex_type&& re,
const int (&submatches)[N],
std::regex_constants::match_flag_type m =
std::regex_constants::match_default ) = delete;
```

Constructs a new `regex_token_iterator`:
1. Default constructor. Constructs the end-of-sequence iterator.
@2-5@ First, copies the list of the requested submatch out of the `submatches` or `submatch` argument into the member list stored in the iterator and constructs the member `std::regex_iterator` by passing `a`, `b`, `re`, and `m` to its four-argument constructor (that constructor performs the initial call to `std::regex_search`) and sets the internal counter of `submatches` to zero.
* If, after construction, the member `regex_iterator` is not an end-of-sequence iterator, sets the member pointer to the address of the current `std::sub_match`.
* Otherwise (if the member `regex_iterator` is an end-of-sequence iterator), but the value `-1` is one of the values in `submatches`/`submatch`, turns `*this` into a ''suffix iterator'' pointing at the range [a, b) (the entire string is the non-matched suffix).
* Otherwise (if `-1` is not in the list of `submatches`), turns `*this` into the end-of-sequence iterator.
The behavior is undefined if any value in `submatches` is less than `-1`.
6. Copy constructor: performs member-wise copy (including making a copy of the member `regex_iterator` and the member pointer to current `sub_match`).
@7-10@ The overloads  are prohibited from being called with a temporary regex since otherwise the returned iterator would be immediately invalidated.

## Parameters


### Parameters

- `a` - *BidirectionalIterator* to the beginning of the target character sequence
- `b` - *BidirectionalIterator* to the end of the target character sequence
- `re` - regular expression used to search the target character sequence
- `submatch` - the index of the submatch that should be returned. "0" represents the entire match, and "-1" represents the parts that are not matched (e.g, the stuff between matches)
- `submatches` - the sequence of submatch indices that should be iterated over within each match, may include the special value `-1` for the non-matched fragments
- `m` - flags that govern the behavior of `re`

## Example


## Defect reports

