---
title: std::nested_exception::nested_exception
type: Utilities
source: https://en.cppreference.com/w/cpp/error/nested_exception/nested_exception
---


```cpp
dcla|num=1|since=c++11|constexpr=c++26|
nested_exception() noexcept;
dcla|num=2|since=c++11|constexpr=c++26|1=
nested_exception( const nested_exception& other ) noexcept = default;
```

Constructs new `nested_exception` object.
1. Default constructor. Stores an exception object obtained by calling `std::current_exception()` within the new `nested_exception` object.
2. Copy constructor. Initializes the object with the exception stored in `other`.

## Parameters


### Parameters

- `other` - nested exception to initialize the contents with
