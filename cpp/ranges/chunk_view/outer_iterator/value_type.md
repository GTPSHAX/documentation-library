---
title: std::ranges::chunk_view::outer-iterator::value_type
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/outer_iterator/value_type
---

ddcl|header=ranges|since=c++23|
struct value_type : view_interface<value_type>
A value type of the iterator `chunk_view::''outer-iterator''`, formed when `V` models .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|value_type|
ddcl|since=c++23|1=
private:
// exposition only
constexpr explicit value_type( chunk_view& parent );
Constructs the `value_type` object so that  is initialized with `std::addressof(parent)`.

## Parameters


### Parameters

- `parent` - the `chunk_view` object
member|begin|
ddcl|since=c++23|
constexpr /*inner-iterator*/ begin() const noexcept;
Equivalent to `return /*inner-iterator*/(*parent_);`.
member|end|
ddcl|since=c++23|
constexpr std::default_sentinel_t end() const noexcept;
Equivalent to `return std::default_sentinel;`.
member|size|
ddcl|since=c++23|
constexpr auto size() const
requires std::sized_sentinel_for<ranges::sentinel_t<V>, ranges::iterator_t<V>>;
Returns the size of the view.
Equivalent to<br>c|
return /*to-unsigned-like*/(
ranges::min(parent_->remainder_, ranges::end(parent_->base_) - *parent_->current_));

## Example


## References


## See also

