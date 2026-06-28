---
title: std::chrono::weekday
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|
class weekday;
}
}
}
}
}
}
}
```

The class `weekday` represent a day of the week in the [proleptic Gregorian calendar](https://en.wikipedia.org/wiki/proleptic Gregorian calendar). Its normal range is , for Sunday through Saturday, but it can hold any value in the range . Seven named constants are predefined in the `std::chrono` namespace for the seven days of the week.
`weekday` is a *TriviallyCopyable* *StandardLayoutType*.

## Member functions


| cpp/chrono/weekday/dsc constructor | (see dedicated page) |
| cpp/chrono/weekday/dsc operator inc dec | (see dedicated page) |
| cpp/chrono/weekday/dsc operator arith | (see dedicated page) |
| cpp/chrono/weekday/dsc encoding | (see dedicated page) |
| cpp/chrono/weekday/dsc ok | (see dedicated page) |
| cpp/chrono/weekday/dsc operator at | (see dedicated page) |


## Nonmember functions


| cpp/chrono/weekday/dsc operator cmp | (see dedicated page) |
| cpp/chrono/weekday/dsc operator arith 2 | (see dedicated page) |
| cpp/chrono/weekday/dsc operator ltlt | (see dedicated page) |
| cpp/chrono/weekday/dsc from_stream | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|weekday | (see dedicated page) |
| cpp/chrono/weekday|nested=true|notes= | |


## Example


### Example


**Output:**
```
Wed
Thu
Fri
```


## See also


| cpp/chrono/dsc weekday_indexed | (see dedicated page) |

