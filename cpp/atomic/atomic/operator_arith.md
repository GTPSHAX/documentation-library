---
title: std::atomic::operators (int)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/operator_arith
---


```cpp
dcl|num=1|since=c++11|
T operator++() noexcept;
dcl|num=2|since=c++11|
T operator++() volatile noexcept;
dcl|num=3|since=c++11|
T operator++( int ) noexcept;
dcl|num=4|since=c++11|
T operator++( int ) volatile noexcept;
dcl|num=5|since=c++11|
T operator--() noexcept;
dcl|num=6|since=c++11|
T operator--() volatile noexcept;
dcl|num=7|since=c++11|
T operator--( int ) noexcept;
dcl|num=8|since=c++11|
T operator--( int ) volatile noexcept;
dcl|num=9|since=c++11|
T* operator++() noexcept;
dcl|num=10|since=c++11|
T* operator++() volatile noexcept;
dcl|num=11|since=c++11|
T* operator++( int ) noexcept;
dcl|num=12|since=c++11|
T* operator++( int ) volatile noexcept;
dcl|num=13|since=c++11|
T* operator--() noexcept;
dcl|num=14|since=c++11|
T* operator--() volatile noexcept;
dcl|num=15|since=c++11|
T* operator--( int ) noexcept;
dcl|num=16|since=c++11|
T* operator--( int ) volatile noexcept;
```

Atomically increments or decrements the current value. The operation is read-modify-write operation.
* `operator++()` performs atomic pre-increment. Equivalent to `return fetch_add(1) + 1;`.
* `operator++(int)` performs atomic post-increment. Equivalent to `return fetch_add(1);`.
* `operator--()` performs atomic pre-decrement. Equivalent to `return fetch_sub(1) - 1;`.
* `operator--(int)` performs atomic post-decrement. Equivalent to `return fetch_sub(1);`.
@1-8@ For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
@9-16@ The result may be an undefined address, but the operations otherwise have no undefined behavior.
@@ If `T` is not a complete object type, the program is ill-formed.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is false and any `volatile` overload participates in overload resolution.

## Return value

`operator++()` and `operator--()` return the value of the atomic variable after the modification. Formally, the result of incrementing/decrementing the value immediately preceding the effects of this function in the  of `*this`.
`operator++(int)` and `operator--(int)` return the value of the atomic variable before the modification. Formally, the value immediately preceding the effects of this function in the  of `*this`.

## Notes

Unlike most pre-increment and pre-decrement operators, the pre-increment and pre-decrement operators for atomic types do not return a reference to the modified object. They return a copy of the stored value instead.

## Example


### Example


**Output:**
```
▒  2  ░  1  ▒  5  ▒  7  █  4  ░  6  ▓  3  ▒  8  
▓ 11  █  9  ▓ 13  ░ 10  █ 14  ▒ 12  ░ 16  ░ 19  
▓ 15  ▒ 18  ▓ 21  ▒ 22  █ 17  █ 25  ▒ 24  █ 26  
░ 20  ░ 29  ▒ 27  ▓ 23  ▒ 31  ▒ 33  ▓ 32  █ 28  
░ 30  ░ 37  ▒ 34  ▓ 35  █ 36  █ 41  ▓ 40  ▒ 39  
░ 38  ▓ 43  █ 42  ▓ 46  ▓ 48  █ 47  █ 50  ░ 45  
▒ 44  ▒ 53  ▒ 54  ▓ 49  ▒ 55  █ 51  ▒ 57  █ 58  
░ 52  ▓ 56  ░ 61  ▒ 59  █ 60  ▓ 62  ▒ 64  ░ 63  
░ 68  ▓ 66  █ 65  █ 71  ▒ 67  ▓ 70  ░ 69  █ 72
```


## Defect reports


## See also


| cpp/atomic/atomic/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith2 | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith3 | (see dedicated page) |

