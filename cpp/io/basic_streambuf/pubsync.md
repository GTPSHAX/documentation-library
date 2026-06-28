---
title: std::basic_streambuf::sync
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pubsync
---


```cpp
dcl | num=1 |1=
int pubsync();
dcl | num=2 |1=
protected:
virtual int sync();
```

Synchronizes the controlled character sequence (the buffers) with the associated character sequence.
1) Calls `sync()` of the most derived class
2) The base class version of this function has no effect. The derived classes may override this function to allow synchronizing the underlying device with the buffers.
For output streams, this typically results in writing the contents of the put area into the associated sequence, i.e. flushing of the output buffer. For input streams, this typically empties the get area and forces a re-read from the associated sequence to pick up recent changes. The default behavior (found, for example, in `std::basic_stringbuf`), is to do nothing.

## Parameters

(none)

## Return value

1) The return value of `sync()`.
2) Returns `0` on success, `-1` otherwise. The base class version returns `0`.

## Example


## See also

de:cpp/io/basic streambuf/pubsync
es:cpp/io/basic streambuf/pubsync
fr:cpp/io/basic streambuf/pubsync
it:cpp/io/basic streambuf/pubsync
ja:cpp/io/basic streambuf/pubsync
pt:cpp/io/basic streambuf/pubsync
ru:cpp/io/basic streambuf/pubsync
zh:cpp/io/basic streambuf/pubsync
