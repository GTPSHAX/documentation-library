---
title: std::hash<std::thread::id>
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/id/hash
---


# hashsmall|<std::thread::id>


```cpp
**Header:** `<`thread`>`
dcl|since=c++11|1=
template<> struct hash<std::thread::id>;
```

The template specialization of `std::hash` for the `std::thread::id` class allows users to obtain hashes of the identifiers of threads.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <thread>
#include <vector>
using namespace std::chrono_literals;

void foo()
{
    std::this_thread::sleep_for(10ms);
}

int main()
{
    std::vector<std::thread> v;
    for (int n = 0; n < 4; ++n)
        v.emplace_back(foo);

    std::hash<std::thread::id> hasher;
    for (auto& t : v)
    {
        std::cout << "thread " << t.get_id() << " hashes to "
                  << hasher(t.get_id()) << '\n';
        t.join();
    }
}
```


**Output:**
```
thread 139786440144640 hashes to 8905351942358389397
thread 139786431751936 hashes to 9222844670065909738
thread 139786423359232 hashes to 18199000599186780501
thread 139786414966528 hashes to 15386662774029264672
```


## See also


| cpp/utility/dsc hash | (see dedicated page) |

