---
title: std::fpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/fpos
---


```cpp
**Header:** `<`ios`>`
dcl|1=
template< class State >
class fpos;
```

Specializations of the class template `std::fpos` identify absolute positions in a stream or in a file. Each object of type `fpos` holds the byte position in the stream (typically as a private member of type `std::streamoff`) and the current shift state, a value of type `State` (typically `std::mbstate_t`).
The following typedef names for `std::fpos<std::mbstate_t>` are provided (although they are spelled differently in the standard, they denote the same type):


| Item | Description |
|------|-------------|
| iosfwd | |
| **Type** | Definition |

All specializations of `fpos` meet the *DefaultConstructible*, *CopyConstructible*, *CopyAssignable*, *Destructible*, and *EqualityComparable* requirements.
If `State` is trivially copy constructible, `fpos` has a trivial copy constructor.
If `State` is trivially copy assignable, `fpos` has a trivial copy assignment operator.
If `State` is trivially destructible, `fpos` has a trivial destructor.

## Template parameter


### Parameters

- `State` - the type representing the shift state

**Type requirements:**

- `State`

## Member functions

In addition, member and non-member functions are provided to support the following operations:
* A default constructor that stores an offset of zero and value-initializes the state object.
* A non-explicit constructor that accepts an argument of type (possibly const) `std::streamoff`, which stores that offset and value-initializes the state object. This constructor must also accept the special value `std::streamoff(-1)`: the `std::fpos` constructed in this manner is returned by some stream operations to indicate errors.
* Explicit conversion from (possibly const) `fpos` to `std::streamoff`. The result is the stored offset.
* `1=operator==` and `1=operator!=` that compare two objects of type (possibly const) `std::fpos` and return a `bool` prvalue. `1=p != q` is equivalent to `1=!(p == q)`.
* `operator+` and `operator-` such that, for an object `p` of type (possibly const) `fpos<State>` and an object `o` of type (possibly const) `std::streamoff`
:* `p + o` has type `fpos<State>` and stores an offset that is the result of adding `o` to the offset of `p`.
:* `o + p` has a type convertible to `fpos<State>` and the result of the conversion is equal to `p + o`.
:* `p - o` has type `fpos<State>` and stores an offset that is the result of subtracting `o` from the offset of `p`.
* `1=operator+=` and `1=operator-=` which can accept a (possibly const) `std::streamoff` and adds/subtracts it from the stored offset, respectively.
* `operator-` which can subtract two objects of type (possibly const) `std::fpos` producing an `std::streamoff`, such that for two such objects `p` and `q`, `1=p == q + (p - q)`.

## Notes

Some of the `I/O streams member functions` return and manipulate objects of member typedef `pos_type`. For streams, these member typedefs are provided by the template parameter `Traits`, which defaults to `std::char_traits`, which define their `pos_type`s to be specializations of `std::fpos`. The behavior of the I/O streams library is implementation-defined when `Traits::pos_type` is not `std::fpos<std::mbstate_t>` (aka `std::streampos`, `std::wstreampos`, etc.).

## Defect reports


## See also


| cpp/io/dsc streamoff | (see dedicated page) |
| cpp/io/basic_ostream/dsc tellp | (see dedicated page) |
| cpp/io/basic_ostream/dsc seekp | (see dedicated page) |
| cpp/io/c/dsc fgetpos | (see dedicated page) |

