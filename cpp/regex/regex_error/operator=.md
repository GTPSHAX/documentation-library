---
title: std::regex_error::operator=
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_error/operator=
---

ddcl|since=c++11|1=
regex_error& operator=( const regex_error& other ) noexcept;
Assigns the contents with those of `other`. If `*this` and `other` both have dynamic type `std::regex_error` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another `regex_error` object to assign with

## Return value

`*this`

## Example

