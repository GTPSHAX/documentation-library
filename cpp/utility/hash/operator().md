---
title: std::hash::operator()
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/hash/operator()
---


# dsc small|hash<Key>::

operator()
Specializations of `std::hash` should define an `operator()` that:
* Takes a single argument `key` of type `Key`.
* Returns a value of type `std::size_t` that represents the hash value of `key`.
* For two parameters `k1` and `k2` that are equal, `1=std::hash<Key>()(k1) == std::hash<Key>()(k2)`.
* For two different parameters `k1` and `k2` that are not equal, the probability that `1=std::hash<Key>()(k1) == std::hash<Key>()(k2)` should be very small, approaching `1.0 / std::numeric_limits<size_t>::max()`.

## Parameters


### Parameters

- `key` - the object to be hashed

## Return value

A `std::size_t` representing the hash value.

## Exceptions

Hash functions should not throw exceptions.

## Example


### Example

```cpp
#include <cstddef>
#include <functional>
#include <iostream>
#include <string>

struct Employee
{
    std::string name;
    std::size_t ID;
};

static_assert([](auto... sz) { return ((sizeof(std::size_t) == sz) or ...); }(4, 8));

namespace std
{
    template <>
    class hash<Employee>
    {
    public:
        static constexpr std::size_t operator()(const Employee& employee)
        {
             // Computes the hash of an employee using Fowler-Noll-Vo-1a hash function.
             constexpr std::size_t prime{sizeof(size_t) < 8 ? 0x01000193 : 0x100000001b3};
             std::size_t result{sizeof(size_t) < 8 ? 0x811c9dc5 : 0xcbf29ce484222325};

             for (auto ch : employee.name)
                 result = (result ^ ch) * prime;

             return result ^ (employee.ID << 1);
         }
    };
}

int main()
{
    std::hash<Employee> hash_fn;
    std::cout << std::hex << hash_fn(Employee{"Zaphod Beeblebrox", 42}) << '\n';
}
```


**Output:**
```
6fbb35ba06f7b013
```

