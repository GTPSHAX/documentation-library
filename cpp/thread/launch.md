---
title: std::launch
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/launch
---

ddcl|header=future|since=c++11|1=
enum class launch : /* unspecified */ {
async =    /* unspecified */,
deferred = /* unspecified */,
/* implementation-defined */
};
`std::launch` is a *BitmaskType*. It specifies the launch policy for a task executed by the `std::async` function.

## Constants

The following constants denoting individual bits are defined by the standard library:


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |

In addition, implementations are allowed to:
* define additional bits and bitmasks to specify restrictions on task interactions applicable to a subset of launch policies, and
* enable those additional bitmasks for the first (default) overload of `std::async`.

## Defect reports


## See also


| cpp/thread/dsc async | (see dedicated page) |

