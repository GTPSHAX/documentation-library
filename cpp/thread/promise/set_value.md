---
title: std::promise::set_value
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/promise/set_value
---


```cpp
dcl|num=1|since=c++11|
void set_value( const R& value );
dcl|num=2|since=c++11|
void set_value( R&& value );
dcl|num=3|since=c++11|
void set_value( R& value );
dcl|num=4|since=c++11|
void set_value();
```

@1-3@ Atomically stores `value` into the shared state and makes the state ready.
4. Makes the state ready.
The operation behaves as though `set_value`, `set_exception`, `set_value_at_thread_exit`, and `set_exception_at_thread_exit` acquire a single mutex associated with the promise object while updating the promise object.
Calls to this function do not introduce data races with calls to `get_future` (therefore they need not synchronize with each other).

## Parameters


### Parameters

- `value` - value to store in the shared state

## Return value

(none)

## Exceptions

`std::future_error` on the following conditions:
* `*this` has no shared state. The error code is set to `cpp/thread/future_errc|no_state`.
* The shared state already stores a value or exception. The error code is set to `cpp/thread/future_errc|promise_already_satisfied`.
Additionally:
1. Any exception thrown by the constructor selected to copy an object of type `R`.
2. Any exception thrown by the constructor selected to move an object of type `R`.

## Example


### Example

```cpp
#include <algorithm>
#include <cctype>
#include <chrono>
#include <future>
#include <iostream>
#include <iterator>
#include <sstream>
#include <thread>
#include <vector>

using namespace std::chrono_literals;

int main()
{
    std::istringstream iss_numbers{"3 4 1 42 23 -23 93 2 -289 93"};
    std::istringstream iss_letters{" a 23 b,e a2 k k?a;si,ksa c"};

    std::vector<int> numbers;
    std::vector<char> letters;
    std::promise<void> numbers_promise, letters_promise;

    auto numbers_ready = numbers_promise.get_future();
    auto letter_ready = letters_promise.get_future();

    std::thread value_reader([&]
    {
        // I/O operations
        std::copy(std::istream_iterator<int>{iss_numbers},
                  std::istream_iterator<int>{},
                  std::back_inserter(numbers));

        // notify for numbers
        numbers_promise.set_value();

        std::copy_if(std::istreambuf_iterator<char>{iss_letters},
                     std::istreambuf_iterator<char>{},
                     std::back_inserter(letters),
                     ::isalpha);

        // notify for letters
        letters_promise.set_value();
    });


    numbers_ready.wait();

    std::sort(numbers.begin(), numbers.end());

    if (letter_ready.wait_for(1s) == std::future_status::timeout)
    {
        // output the numbers while letters are being obtained
        for (int num : numbers)
            std::cout << num << ' ';
        numbers.clear(); // numbers were already printed
    }

    letter_ready.wait();
    std::sort(letters.begin(), letters.end());

    // does nothing if numbers were already printed
    for (int num : numbers)
        std::cout << num << ' ';
    std::cout << '\n';

    for (char let : letters)
        std::cout << let << ' ';
    std::cout << '\n';

    value_reader.join();
}
```


**Output:**
```
-289 -23 1 2 3 4 23 42 93 93 
a a a a b c e i k k k s s
```


## Defect reports


## See also


| cpp/thread/promise/dsc set_value_at_thread_exit | (see dedicated page) |
| cpp/thread/promise/dsc set_exception | (see dedicated page) |

