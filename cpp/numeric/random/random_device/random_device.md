---
title: std::random_device::random_device
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/random_device/random_device
---


```cpp
dcl|num=1|since=c++11|1=
random_device() : random_device( /*implementation-defined*/ ) {}
dcl|num=2|since=c++11|1=
explicit random_device( const std::string& token );
dcl|num=3|since=c++11|1=
random_device( const random_device& ) = delete;
```

1. Default constructs a new `std::random_device` object with an implementation-defined `token`.
2. Constructs a new `std::random_device` object, making use of the argument `token` in an implementation-defined manner.
3. The copy constructor is deleted: `std::random_device` is not copyable nor movable.

## Exceptions

Throws an implementation-defined exception derived from `std::exception` on failure.

## Notes

The implementation in [https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/src/c%2B%2B11/random.cc#L319 libstdc++] expects `token` to name the source of random bytes. Possible token values include `"default"`,  `"hw"`, `"rand_s"`, `"rdseed"`, `"rdrand"`, `"rdrnd"`, `"/dev/urandom"`, `"/dev/random"`, `"mt19937"`, and integer string specifying the seed of the mt19937 engine. (Token values other than `"default"` are only valid for certain targets.)
The implementation in [https://github.com/llvm/llvm-project/blob/main/libcxx/src/random.cpp#L124 libc++], when configured to use character device as the source, expects `token` to be the name of a character device that produces random numbers when read from; otherwise it expects `token` to be `"/dev/urandom"`.
Both libstdc++ and libc++ throw an exception if provided an unsupported token. [https://github.com/microsoft/STL/blob/c10ae01b4d9508eed9d5f059a120ee7223b6ac12/stl/inc/random#L5026 Microsoft's stdlib] ignores the token entirely.

## Example


### Example

```cpp
#include <iostream>
#include <random>

void demo(std::random_device&& rd)
{
    static std::uniform_int_distribution<int> d(0, 9);
    for (int n = 0; n != 10; ++n)
        std::cout << d(rd) << ' ';
    std::cout << '\n';
}

int main()
{
    // Note: How the supplied token is handled is implementation-defined!

    // Default token for random_device is usually /dev/urandom on Linux
    demo(std::random_device {});

    // Request /dev/random, blocks when entropy is empty
    // Works on libstdc++, ignored in msvc++, might throw on libc++ (as of Nov 2022)
    demo(std::random_device {"/dev/random"});

    // Request non-blocking /dev/urandom, ensures that RDRAND is not used
    // Works on libstdc++ and libc++, ignored in msvc++ (as of Nov 2022)
    demo(std::random_device {"/dev/urandom"});

    // Request "hw", will use hardware-based random generation like rdrand
    // Works on libstdc++, ignored in msvc++, throws on libc++ (as of Nov 2022)
    demo(std::random_device {"hw"});
}
```


**Output:**
```
9 5 2 7 5 9 4 1 0 7 
4 7 6 5 1 5 5 1 8 6 
3 3 6 1 4 1 4 1 0 2 
4 6 3 9 1 9 4 0 9 3
```


## Defect reports

