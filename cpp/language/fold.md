---
title: Fold expressions
type: Language
source: https://en.cppreference.com/w/cpp/language/fold
---


# Fold expressions mark since c++17

Reduces ([Fold (higher-order function)|folds](https://en.wikipedia.org/wiki/Fold (higher-order function)|folds)) a `pack` over a binary operator.

## Syntax


**Syntax:**

- `*pack op* **`... )`**`
- `*op pack* **`)`**`
- `*pack op* **`...`** *op init* **`)`**`
- `*init op* **`...`** *op pack* **`)`**`
1. Unary right fold.
2. Unary left fold.
3. Binary right fold.
4. Binary left fold.

### Parameters

- `{{spar` - op|any of the following 32 ''binary'' operators: `+` `-` `*` `/` `%` `^` `&` ` `1==` `<` `>` `<<` `>>` `1=+=` `1=-=` `1=*=` `1=/=` `1=%=` `1=^=` `1=&=` `1= `1=<<=` `1=>>=` `1===` `1=!=` `1=<=` `1=>=` `&&` ` `,` `.*` `->*`. In a binary fold, both *op*s must be the same.
- `{{spar` - pack|an expression that contains an unexpanded `pack` and does not contain an operator with `precedence` lower than cast at the top level (formally, a *cast-expression*)
- `{{spar` - init|an expression that does not contain an unexpanded `pack` and does not contain an operator with `precedence` lower than cast  at the top level (formally, a *cast-expression*)
Note that the opening and closing parentheses are a required part of the fold expression.

## Explanation

The instantiation of a ''fold expression'' expands the expression `e` as follows:
1. Unary right fold <span class="t-c">`(E` *op* `...)`</span> becomes <span class="t-c">`(E *op* `(`... *op* `(E *op* `E</span>
2. Unary left fold <span class="t-c">`(...` *op* `E)`</span> becomes <span class="t-c">`(((E *op* `E *op* ...`)` *op* `E</span>
3. Binary right fold <span class="t-c">`(E` *op* `...` *op* `I)`</span> becomes <span class="t-c">`(E *op* `(`... *op* `(E *op* `(E *op* `I))))`</span>
4. Binary left fold <span class="t-c">`(I` *op* `...` *op* `E)`</span> becomes <span class="t-c">`((((I` *op* `E *op* `E *op* ...`)` *op* `E</span>
(where `N` is the number of elements in the pack expansion)
For example,

```cpp
template<typename... Args>
bool all(Args... args) { return (... && args); }

bool b = all(true, true, true, false);
// within all(), the unary left fold expands as
//  return ((true && true) && true) && false;
// b is false
```

When a unary fold is used with a pack expansion of length zero, only the following operators are allowed:
1. Logical AND (`&&`). The value for the empty pack is `true`.
2. Logical OR (`). The value for the empty pack is `false`.
3. The comma operator (`,`). The value for the empty pack is `void()`.

## Notes

If the expression used as *init* or as *pack* has an operator with `precedence` below cast at the top level, it must be parenthesized:

```cpp
template<typename... Args>
int sum(Args&&... args)
{
//  return (args + ... + 1 * 2);   // Error: operator with precedence below cast
    return (args + ... + (1 * 2)); // OK
}
```


## Example


### Example

```cpp
#include <climits>
#include <concepts>
#include <cstdint>
#include <iostream>
#include <limits>
#include <type_traits>
#include <utility>
#include <vector>

// Basic usage, folding variadic arguments over operator<< 
template<typename... Args>
void printer(Args&&... args)
{
    (std::cout << ... << args) << '\n';
}

// Folding an expression that uses the pack directly over operator,
template<typename... Ts>
void print_limits()
{
    ((std::cout << +std::numeric_limits<Ts>::max() << ' '), ...) << '\n';
}

// Both a fold over operator&& using the pack
// and over operator, using the variadic arguments
template<typename T, typename... Args>
void push_back_vec(std::vector<T>& v, Args&&... args)
{
    static_assert((std::is_constructible_v<T, Args&&> && ...));
    (v.push_back(std::forward<Args>(args)), ...);
}

// Using an integer sequence to execute an expression
// N times by folding a lambda over operator,
template<class T, std::size_t... dummy_pack>
constexpr T bswap_impl(T i, std::index_sequence<dummy_pack...>)
{
    T low_byte_mask = static_cast<unsigned char>(-1);
    T ret{};
    ([&]
    {
        (void)dummy_pack;
        ret <<= CHAR_BIT;
        ret {{!
```

i >>= CHAR_BIT;
}(), ...);
return ret;
}
constexpr auto bswap(std::unsigned_integral auto i)
{
return bswap_impl(i, std::make_index_sequence<sizeof(i)>{});
}
int main()
{
printer(1, 2, 3, "abc");
print_limits<uint8_t, uint16_t, uint32_t>();
std::vector<int> v;
push_back_vec(v, 6, 2, 45, 12);
push_back_vec(v, 1, 2, 9);
for (int i : v)
std::cout << i << ' ';
std::cout << '\n';
static_assert(bswap<std::uint16_t>(0x1234u) == 0x3412u);
static_assert(bswap<std::uint64_t>(0x0123456789abcdefull) == 0xefcdab8967452301ULL);
}
|output=
123abc
255 65535 4294967295
6 2 45 12 1 2 9

## References


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-2611 | C++17 | the expansion results of fold expressions were not enclosed with parentheses | enclosed with parentheses |

