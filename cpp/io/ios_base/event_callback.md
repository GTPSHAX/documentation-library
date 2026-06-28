---
title: std::ios_base::event_callback
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/event_callback
---

ddcl|
typedef void ( *event_callback )( event type, ios_base& ios, int index );
The type of function callbacks that can be registered using `register_callback()` to be called on specific events.
`type` is a value of type  which indicates the type of the event that will invoke this callback.
`ios` refers to the stream object for which the callback is invoked: `*this` is passed as the argument when callbacks are invoked by `std::ios_base` and `std::basic_ios` member functions.
`index` is the user-provided value passed to `register_callback()` when registering the function.

## See also


| cpp/io/basic_ios/dsc copyfmt | (see dedicated page) |
| cpp/io/ios_base/dsc imbue | (see dedicated page) |
| cpp/io/ios_base/dsc destructor | (see dedicated page) |
| cpp/io/ios_base/dsc register_callback | (see dedicated page) |

