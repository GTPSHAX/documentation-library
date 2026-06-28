---
title: std::basic_stacktrace::max_size
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/max_size
---

ddcl | since=c++23 |
size_type max_size() const noexcept;
Returns the maximum number of elements the underlying container (typically a `std::vector`) is able to hold due to system or library implementation limitations, i.e. `std::distance(begin(), end())` for the largest underlying container.

## Parameters

(none)

## Return value

Maximum number of elements.

## Complexity

Constant.

## Notes

This value typically reflects the theoretical limit on the size of the underlying container, at most `std::numeric_limits<difference_type>::max()`. At runtime, the size of the container may be limited to a value smaller than `max_size()` by the amount of RAM available.

## Example


### Example

```cpp
#include <iostream>
#include <stacktrace>

int main()
{
    std::stacktrace trace;
    std::cout << "Maximum size of a 'basic_stacktrace' is " << trace.max_size() << "\n";
}
```


**Output:**
```
Maximum size of a 'basic_stacktrace' is 1152921504606846975
```


## See also

