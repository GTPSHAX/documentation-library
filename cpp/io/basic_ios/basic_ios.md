---
title: std::basic_ios::basic_ios
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/basic_ios
---


```cpp
dcl|num=1|
protected:
basic_ios();
dcl|num=2|
public:
explicit basic_ios( std::basic_streambuf<CharT, Traits>* sb );
dcl rev multi|num=3|until1=c++11|dcl1=
private:
basic_ios( const basic_ios& );
|dcl2=
public:
basic_ios( const basic_ios& ) = delete;
```

Constructs a new `std::basic_ios` object.
1. Default constructor. The internal state is not initialized. `init()` must be called before the first use of the object or before destructor, otherwise the behavior is undefined.
2. Initializes the internal state by calling `init(sb)`. The associated stream buffer is set to `sb`.
3. The copy constructor is <sup>(until C++11)</sup> declared private and not defined<sup>(since C++11)</sup> explicitly defined as deleted: I/O streams are not *CopyConstructible*.

## Parameters


### Parameters

- `sb` - stream buffer to associate to

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1249 | C++98 | internal state did not need to be initialized before first use | also needs to be initialized |

