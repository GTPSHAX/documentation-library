---
title: std::bad_expected_access
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/bad_expected_access
---


```cpp
**Header:** `<`expected`>`
dcl | num=1 | since=c++23 |1=
template< class E >
class bad_expected_access : public std::bad_expected_access<void>
dcl | num=2 | since=c++23 |1=
template<>
class bad_expected_access<void> : public std::exception
```

1. Defines a type of object to be thrown by `cpp/utility/expected/value|std::expected::value` when accessing an expected object that contains an unexpected value. `bad_expected_access<E>` stores a copy of the unexpected value.
2. `bad_expected_access<void>` is the base class of all other `bad_expected_access` specializations.

## Members of the primary template

member | 1=bad_expected_access | 2=

```cpp
dcl |
explicit bad_expected_access( E e );
```

Constructs a new `bad_expected_access<E>` object. Initializes the stored value with `std::move(e)`.
member | 1=error |2=

```cpp
dcl |
const E& error() const & noexcept;
E& error() & noexcept;
const E&& error() const && noexcept;
E&& error() && noexcept;
```

Returns a reference to the stored value.
member | what |

```cpp
dcl |
const char* what() const noexcept override;
```

Returns the explanatory string.

## Parameters

(none)

## Return value

Pointer to a null-terminated string with explanatory information. The string is suitable for conversion and display as a `std::wstring`. The pointer is guaranteed to be valid at least until the exception object from which it is obtained is destroyed, or until a non-const member function (e.g. copy assignment operator) on the exception object is called.

## Notes

Implementations are allowed but not required to override `what()`.

## Members of the `bad_expected_access<void>` specialization

Special member functions of `bad_expected_access<void>` are protected. They can only be called by derived classes.

## Example

