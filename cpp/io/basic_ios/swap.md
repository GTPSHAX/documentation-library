---
title: std::basic_ios::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/swap
---

ddcl|since=c++11|
protected:
void swap( basic_ios& other ) noexcept;
Exchanges the states of `*this` and `other`, except for the associated `rdbuf` objects. `rdbuf()` and `other.rdbuf()` returns the same values as before the call.
This swap function is protected: it is called by the swap member functions of the derived stream classes such as `std::basic_ofstream` or `std::basic_istringstream`, which know how to correctly swap the associated stream buffers.

## Parameters


### Parameters

- `other` - the `basic_ios` object to exchange the state with

## See also


| cpp/io/basic_ios/dsc move | (see dedicated page) |

