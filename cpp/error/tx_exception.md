---
title: std::tx_exception
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/tx_exception
---

ddcl|header=stdexcept|since=tm_ts|
template< class T >
class tx_exception : public std::runtime_error;
Defines an exception type that can be used to cancel and roll back an atomic transaction initiated by the keyword `cpp/language/transactional_memory|atomic_cancel`.
If `T` is not *TriviallyCopyable*, the program that specializes `std::tx_exception<T>` is ill-formed.

## Member functions

member|tx_exception|2=

```cpp
dcl|num=1|since=tm_ts|
explicit tx_exception( T value ) transaction_safe;
dcl|num=2|since=tm_ts|
tx_exception( T value, const std::string& what_arg ) transaction_safe;
dcl|num=3|since=tm_ts|
tx_exception( T value, const char* what_arg ) transaction_safe;
dcl|num=4|since=tm_ts|
tx_exception( const tx_exception& other ) transaction_safe noexcept;
```

@1-3@ Constructs the exception object with `what_arg` as explanatory string that can be accessed through `what()` and `value` as the object that can be accessed through `get()`.
4. Copy constructor. If `*this` and `other` both have dynamic type `std::tx_exception<T>` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `value` - payload object
- `what_arg` - explanatory string
- `other` - another exception object to copy

## Exceptions

@1-3@ May throw implementation-defined exceptions.
member|operator|

```cpp
dcl|since=tm_ts|1=
tx_exception& operator=( const tx_exception& other ) transaction_safe noexcept;
```

Assigns the contents with those of `other`. If `*this` and `other` both have dynamic type `std::tx_exception<T>` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another exception object to assign with

## Return value

`*this`
member|get|2=

```cpp
dcl|since=tm_ts|
T get() const transaction_safe;
```

Returns the payload object held by the exception object.

## Exceptions

May throw implementation-defined exceptions.
member|what|

```cpp
dcl|since=tm_ts|
virtual const char* what() const transaction_safe_dynamic noexcept;
```

Returns the explanatory string.

## Parameters

(none)

## Return value

Pointer to a null-terminated string with explanatory information.
