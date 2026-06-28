---
title: std::raise
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/raise
---

ddcl|header=csignal|
int raise( int sig );
Sends signal sig to the program. The signal handler (specified using the `std::signal()` function) is invoked.
If the user-defined signal handling strategy is not set using `std::signal()` yet, it is implementation-defined whether the signal will be ignored or default handler will be invoked.

## Parameters


### Parameters

- `sig` - the signal to be sent. It can be an implementation-defined value or one of the following values:


| cpp/utility/program/dsc SIG_types | (see dedicated page) |

<!--
-->

## Return value

`0` upon success, non-zero value on failure.

## Example


### Example

```cpp
#include <csignal>
#include <iostream>

void signal_handler(int signal)
{
    std::cout << "Received signal " << signal << '\n';
}

int main()
{
    // Install a signal handler
    std::signal(SIGTERM, signal_handler);

    std::cout << "Sending signal " << SIGTERM << '\n';
    std::raise(SIGTERM);
}
```


**Output:**
```
Sending signal 15
Received signal 15
```


## See also


| cpp/utility/program/dsc signal | (see dedicated page) |

