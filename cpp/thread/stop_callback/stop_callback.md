---
title: std::stop_callback::stop_callback
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_callback/stop_callback
---


```cpp
dcl|since=c++20|num=1|
template< class C >
explicit stop_callback( const std::stop_token& st, C&& cb ) noexcept(/*see below*/);
dcl|since=c++20|num=2|
template< class C >
explicit stop_callback( std::stop_token&& st, C&& cb ) noexcept(/*see below*/);
dcl|since=c++20|num=3|1=
stop_callback( const stop_callback& ) = delete;
dcl|since=c++20|num=4|1=
stop_callback( stop_callback&& ) = delete;
```

Constructs a new `stop_callback` object, saving and registering the `cb` callback function into the given `cpp/thread/stop_token|std::stop_token`'s associated stop-state, for later invocation if stop is requested on the associated `cpp/thread/stop_source|std::stop_source`.
1. Constructs a `stop_callback` for the given `st` `cpp/thread/stop_token|std::stop_token` (copied), with the given invocable callback function `cb`.
2. Constructs a `stop_callback` for the given `st` `cpp/thread/stop_token|std::stop_token` (moved), with the given invocable callback function `cb`.
@3,4@ `stop_callback` is neither *CopyConstructible* nor *MoveConstructible*.
Both constructors participate overload resolution only if `Callback` and `C` satisfy  of `std::constructible_from<Callback, C>`. If `Callback` and `C` satisfy the concept but fail to satisfy its semantic requirement, the behavior is undefined.

## Parameters


### Parameters

- `st` - a `cpp/thread/stop_token|std::stop_token` object to register this `stop_callback` object with
- `cb` - the type to invoke if stop is requested

## Exceptions

@1,2@
Any exception thrown by constructor-initializing the given callback into the `stop_callback` object.

## Notes

If `1=st.stop_requested() == true` for the passed-in `cpp/thread/stop_token|std::stop_token`, then the callback function is invoked in the current thread before the constructor returns.
