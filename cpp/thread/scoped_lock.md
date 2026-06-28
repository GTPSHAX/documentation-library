---
title: std::scoped_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/scoped_lock
---

ddcl|header=mutex|since=c++17|1=
template< class... MutexTypes >
class scoped_lock;
The class `scoped_lock` is a mutex wrapper that provides a convenient RAII-style mechanism for owning zero or more mutexes for the duration of a scoped block.
When a `scoped_lock` object is created, it attempts to take ownership of the mutexes it is given. When control leaves the scope in which the `scoped_lock` object was created, the `scoped_lock` is destructed and the mutexes are released. If several mutexes are given, deadlock avoidance algorithm is used as if by `std::lock`.
The `scoped_lock` class is non-copyable.

## Template parameters


### Parameters

- `MutexTypes` - the types of the mutexes to lock. The types must meet the *Lockable* requirements unless `1=sizeof...(MutexTypes) == 1`, in which case the only type must meet *BasicLockable*

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| dsc|`mutex_type`<br>| | |
| If `1=sizeof...(MutexTypes) == 1`, member type `mutex_type` is the same as `Mutex`, the sole type in `MutexTypes...`. | |
| Otherwise, there is no member `mutex_type`. | |


## Member functions


| cpp/thread/scoped_lock/dsc constructor | (see dedicated page) |
| cpp/thread/scoped_lock/dsc destructor | (see dedicated page) |
| 1=cpp/thread/scoped_lock/dsc operator= | (see dedicated page) |


## Notes

A common beginner error is to "forget" to give a `scoped_lock` variable a name, e.g. `std::scoped_lock(mtx);` (which default constructs a `scoped_lock` variable named `mtx`) or } (which constructs a prvalue object that is immediately destroyed), thereby not actually constructing a lock that holds a mutex for the rest of the scope.

## Example


### Example

```cpp
#include <chrono>
#include <functional>
#include <iostream>
#include <mutex>
#include <string>
#include <syncstream>
#include <thread>
#include <vector>
using namespace std::chrono_literals;

struct Employee
{
    std::vector<std::string> lunch_partners;
    std::string id;
    std::mutex m;
    Employee(std::string id) : id(id) {}
    std::string partners() const
    {
        std::string ret = "Employee " + id + " has lunch partners: ";
        for (int count{}; const auto& partner : lunch_partners)
            ret += (count++ ? ", " : "") + partner;
        return ret;
    }
};

void send_mail(Employee&, Employee&)
{
    // Simulate a time-consuming messaging operation
    std::this_thread::sleep_for(1s);
}

void assign_lunch_partner(Employee& e1, Employee& e2)
{
    std::osyncstream synced_out(std::cout);
    synced_out << e1.id << " and " << e2.id << " are waiting for locks" << std::endl;

    {
        // Use std::scoped_lock to acquire two locks without worrying about
        // other calls to assign_lunch_partner deadlocking us
        // and it also provides a convenient RAII-style mechanism

        std::scoped_lock lock(e1.m, e2.m);

        // Equivalent code 1 (using std::lock and std::lock_guard)
        // std::lock(e1.m, e2.m);
        // std::lock_guard<std::mutex> lk1(e1.m, std::adopt_lock);
        // std::lock_guard<std::mutex> lk2(e2.m, std::adopt_lock);

        // Equivalent code 2 (if unique_locks are needed, e.g. for condition variables)
        // std::unique_lock<std::mutex> lk1(e1.m, std::defer_lock);
        // std::unique_lock<std::mutex> lk2(e2.m, std::defer_lock);
        // std::lock(lk1, lk2);
        synced_out << e1.id << " and " << e2.id << " got locks" << std::endl;
        e1.lunch_partners.push_back(e2.id);
        e2.lunch_partners.push_back(e1.id);
    }

    send_mail(e1, e2);
    send_mail(e2, e1);
}

int main()
{
    Employee alice("Alice"), bob("Bob"), christina("Christina"), dave("Dave");

    // Assign in parallel threads because mailing users about lunch assignments
    // takes a long time
    std::vector<std::thread> threads;
    threads.emplace_back(assign_lunch_partner, std::ref(alice), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(alice));
    threads.emplace_back(assign_lunch_partner, std::ref(dave), std::ref(bob));

    for (auto& thread : threads)
        thread.join();
    std::osyncstream(std::cout) << alice.partners() << '\n'  
                                << bob.partners() << '\n'
                                << christina.partners() << '\n' 
                                << dave.partners() << '\n';
}
```


**Output:**
```
Alice and Bob are waiting for locks
Alice and Bob got locks
Christina and Bob are waiting for locks
Christina and Alice are waiting for locks
Dave and Bob are waiting for locks
Dave and Bob got locks
Christina and Alice got locks
Christina and Bob got locks
Employee Alice has lunch partners: Bob, Christina
Employee Bob has lunch partners: Alice, Dave, Christina
Employee Christina has lunch partners: Alice, Bob
Employee Dave has lunch partners: Bob
```


## Defect reports


## See also


| cpp/thread/dsc unique_lock | (see dedicated page) |
| cpp/thread/dsc lock_guard | (see dedicated page) |

