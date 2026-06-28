---
title: std::weak_ptr::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/reset
---

ddcla|since=c++11|constexpr=c++26|
void reset() noexcept;
Releases the reference to the managed object. After the call `*this` manages no object.

## Example


### Example


**Output:**
```
shared.use_count(): 3
weak.use_count(): 3
weak.expired(): false
weak.reset();
shared.use_count(): 3
weak.use_count(): 0
weak.expired(): true
```


## See also


| cpp/memory/weak_ptr/dsc expired | (see dedicated page) |

