---
title: std::invalid_argument
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/invalid_argument
---

ddcl|header=stdexcept|
class invalid_argument;
Defines a type of object to be thrown as exception. It reports errors that arise because an argument value has not been accepted.
This exception is thrown by `std::bitset::bitset`, and the `std::stoi` and `std::stof` families of functions.

## Member functions


## Notes

The purpose of this exception type is similar to the error condition `std::errc::invalid_argument` (thrown in `std::system_error` from member functions of `std::thread`) and the related errno constant `EINVAL`.

## Example


### Example


**Output:**
```
#1: bitset string ctor has invalid argument
#2: stoi: no conversion
#3: stof: no conversion
```


## Defect reports

