---
title: std::thread::id
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/id
---

ddcl|header=thread|since=c++11|
class thread::id;
The class `thread::id` is a lightweight, trivially copyable class that serves as a unique identifier of `std::thread` <sup>(since C++20)</sup> and `std::jthread` objects.
Instances of this class may also hold the special distinct value that does not represent any thread. Once a thread has finished, the value of `std::thread::id` may be reused by another thread.
This class is designed for use as key in associative containers, both ordered and unordered.

## Member functions


## Non-member functions


| cpp/thread/thread/id/dsc operator_cmp | (see dedicated page) |
| cpp/thread/thread/id/dsc operator_ltlt | (see dedicated page) |


## Helper classes


| cpp/thread/thread/id/dsc hash | (see dedicated page) |
| cpp/thread/thread/id/dsc formatter | (see dedicated page) |


## See also


| cpp/thread/thread/dsc get_id|thread | (see dedicated page) |
| cpp/thread/dsc get_id | (see dedicated page) |

