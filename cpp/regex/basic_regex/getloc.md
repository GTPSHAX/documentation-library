---
title: std::basic_regex::getloc
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/getloc
---

ddcl|since=c++11|
locale_type getloc() const;
Returns the current locale associated with the regular expression.
Effectively calls `traits_i.getloc()` where `traits_i` is a default initialized instance of the type `Traits`, stored within the regular expression object.

## Parameters

(none)

## Return value

The current locale associated with the regular expression.

## Example

