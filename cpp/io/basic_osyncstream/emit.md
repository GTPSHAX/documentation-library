---
title: std::basic_osyncstream::emit
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream/emit
---


```cpp
dcl|1=
void emit();
```

Emits all buffered output and executes any pending flushes, by calling `cpp/io/basic_syncbuf/emit|emit()` on the underlying `cpp/io/basic_syncbuf|std::basic_syncbuf`.

## Parameters

(none)

## Example


### Example

```cpp
#include <iostream>
#include <syncstream>

int main()
{
    {
        std::osyncstream bout(std::cout);
        bout << "Hello," << '\n'; // no flush
        bout.emit(); // characters transferred; cout not flushed
        bout << "World!" << std::endl; // flush noted; cout not flushed
        bout.emit(); // characters transferred; cout flushed
        bout << "Greetings." << '\n'; // no flush
    } // destructor calls emit(): characters transferred; cout not flushed

    // emit can be used for local exception-handling on the wrapped stream
    std::osyncstream bout(std::cout);
    bout << "Hello, " << "World!" << '\n';
    try
    {
        bout.emit();
    }
    catch (...)
    {
        // handle exceptions
    }
}|output=
Hello,
World!
Greetings.
Hello, World!
```


## See also


| cpp/io/basic_osyncstream/dsc destructor | (see dedicated page) |
| cpp/io/basic_syncbuf/dsc emit | (see dedicated page) |

