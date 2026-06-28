---
title: operator<<(std::thread::id)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/id/operator_ltlt
---


# operator<<<small>(std::thread::id)</small>


```cpp
**Header:** `<`thread`>`
dcl|since=c++11|1=
template< class CharT, class Traits >
std::basic_ostream<CharT,Traits>&
operator<<( std::basic_ostream<CharT,Traits>& ost, std::thread::id id );
```

Writes a textual representation of a thread identifier `id` to the output stream `ost`.
If two thread identifiers compare equal, they have identical textual representations; if they do not compare equal, their representations are distinct.

## Parameters


### Parameters

- `ost` - output stream to insert the data into
- `id` - thread identifier

## Return value

`ost`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <thread>
using namespace std::chrono;

int main()
{
    std::thread t1([]{ std::this_thread::sleep_for(256ms); });
    std::thread t2([]{ std::this_thread::sleep_for(512ms); });

    std::clog << t1.get_id() << '\n' << t2.get_id() << '\n';

    t1.join();
    t2.join();
}
```


**Output:**
```
141592653589793
141421356237309
```

