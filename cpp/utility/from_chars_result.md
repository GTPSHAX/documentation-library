---
title: std::from_chars_result
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/from_chars_result
---

`std::from_chars_result` is the return type of . It has no base classes, and only has the following members.

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member and friend functions

member|operator|
ddcl|since=c++20|1=
friend bool operator==( const from_chars_result&,
const from_chars_result& ) = default;
Compares the two arguments using  (which uses `1=operator==` to compare `ptr` and `ec` respectively).
member|operator bool|
ddcl|since=c++26|
constexpr explicit operator bool() const noexcept;
Checks whether the conversion is successful. Returns }.

## Notes


## Example


## See also


| cpp/utility/dsc from_chars | (see dedicated page) |

