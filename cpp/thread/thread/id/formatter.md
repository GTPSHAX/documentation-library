---
title: std::formatter<std::thread::id>
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/id/formatter
---


# formattersmall|<std::thread::id>

ddcl|header=thread|since=c++23|
template< class CharT >
struct formatter<std::thread::id, CharT>;
The template specialization of `std::formatter` for the `std::thread::id` class allows users to convert a thread identifier to its textual representation using formatting functions.

## Format specification

The syntax of format specifications is:

**Syntax:**

- `*width* (optional)`
*fill-and-align* and *width* have the same meaning as in standard format specification. The default alignment is **`>`**.
The formatted output matches the output of `operator<<`, adjusted as appropriate for the format specifiers.

## Notes


## Example


### Example

```cpp
#include <format>
#include <iostream>
#include <thread>

int main()
{
    std::thread::id this_id = std::this_thread::get_id();
    std::thread::id null_id;

    std::cout << std::format("current thread id: {}\n", this_id);
    std::cout << std::format("{:=^10}\n", null_id);
}
```


**Output:**
```
current thread id: 140046396632256
====0=====
```


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |

