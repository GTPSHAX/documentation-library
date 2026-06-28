---
title: std::noop_coroutine_handle
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle
---


```cpp
**Header:** `<`coroutine`>`
dcl|num=1|since=c++20|1=
template< class Promise = void >
struct coroutine_handle;
dcl|num=2|since=c++20|
template<>
struct coroutine_handle<void>;
dcl|num=3|since=c++20|
template<>
struct coroutine_handle<std::noop_coroutine_promise>;
dcl|num=4|since=c++20|1=
using noop_coroutine_handle =
std::coroutine_handle<std::noop_coroutine_promise>;
```

The class template `coroutine_handle` can be used to refer to a suspended or executing coroutine. Every specialization of `coroutine_handle` is a *LiteralType*.
1. Primary template, can be created from the promise object of type `Promise`.
2. Specialization `std::coroutine_handle<void>` erases the promise type. It is convertible from other specializations.
3. Specialization `std::coroutine_handle<std::noop_coroutine_promise>` refers to no-op coroutines. It cannot be created from a promise object.
On typical implementations, every specialization of `std::coroutine_handle` is *TriviallyCopyable*.

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member functions


| cpp/coroutine/coroutine_handle/dsc constructor | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc operator{{= | (see dedicated page) |

#### Conversion

| cpp/coroutine/coroutine_handle/dsc operator coroutine_handle void | (see dedicated page) |

#### Observers

| cpp/coroutine/coroutine_handle/dsc done | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc operator bool | (see dedicated page) |

#### Control

| cpp/coroutine/coroutine_handle/dsc resume | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc destroy | (see dedicated page) |

#### Promise Access

| cpp/coroutine/coroutine_handle/dsc promise | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc from_promise | (see dedicated page) |

#### Export/Import

| cpp/coroutine/coroutine_handle/dsc address | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc from_address | (see dedicated page) |


## Non-member functions


| cpp/coroutine/coroutine_handle/dsc operator_cmp | (see dedicated page) |


## Helper classes


| cpp/coroutine/coroutine_handle/dsc hash | (see dedicated page) |


## Notes

A `coroutine_handle` may be dangling, in which case the `coroutine_handle` must be used carefully in order to avoid undefined behavior.

## Example


### Example

```cpp
#include <coroutine>
#include <iostream>
#include <optional>

template<std::movable T>
class Generator
{
public:
    struct promise_type
    {
        Generator<T> get_return_object()
        {
            return Generator{Handle::from_promise(*this)};
        }
        static std::suspend_always initial_suspend() noexcept
        {
            return {};
        }
        static std::suspend_always final_suspend() noexcept
        {
            return {};
        }
        std::suspend_always yield_value(T value) noexcept
        {
            current_value = std::move(value);
            return {};
        }
        // Disallow co_await in generator coroutines.
        void await_transform() = delete;
        [[noreturn]]
        static void unhandled_exception() { throw; }

        std::optional<T> current_value;
    };

    using Handle = std::coroutine_handle<promise_type>;

    explicit Generator(const Handle coroutine) :
        m_coroutine{coroutine}
    {}

    Generator() = default;
    ~Generator()
    {
        if (m_coroutine)
            m_coroutine.destroy();
    }

    Generator(const Generator&) = delete;
    Generator& operator=(const Generator&) = delete;

    Generator(Generator&& other) noexcept :
        m_coroutine{other.m_coroutine}
    {
        other.m_coroutine = {};
    }
    Generator& operator=(Generator&& other) noexcept
    {
        if (this != &other)
        {
            if (m_coroutine)
                m_coroutine.destroy();
            m_coroutine = other.m_coroutine;
            other.m_coroutine = {};
        }
        return *this;
    }

    // Range-based for loop support.
    class Iter
    {
    public:
        void operator++()
        {
            m_coroutine.resume();
        }
        const T& operator*() const
        {
            return *m_coroutine.promise().current_value;
        }
        bool operator==(std::default_sentinel_t) const
        {
            return !m_coroutine {{!!
```

}
explicit Iter(const Handle coroutine) :
m_coroutine{coroutine}
{}
private:
Handle m_coroutine;
};
Iter begin()
{
if (m_coroutine)
m_coroutine.resume();
return Iter{m_coroutine};
}
std::default_sentinel_t end() { return {}; }
private:
Handle m_coroutine;
};
template<std::integral T>
Generator<T> range(T first, const T last)
{
while (first < last)
co_yield first++;
}
int main()
{
for (const char i : range(65, 91))
std::cout << i << ' ';
std::cout << '\n';
}
|output=
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

## Defect reports


## See also


| cpp/ranges/dsc generator | (see dedicated page) |

