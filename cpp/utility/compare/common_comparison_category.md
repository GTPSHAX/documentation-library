---
title: std::common_comparison_category
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/common_comparison_category
---

ddcl|since=c++20|header=compare|1=
template< class... Ts >
struct common_comparison_category
{
using type = /* see below */ ;
};
The class template `std::common_comparison_category` provides an alias (as the member typedef `type`) for the strongest comparison category to which all of the template arguments `Ts...` can be converted.
In detail, the common comparison type of a list of n types `T`...`T` is defined as follows:
* If any `T` is not a comparison category type (`cpp/utility/compare/partial_ordering|std::partial_ordering`, `cpp/utility/compare/weak_ordering|std::weak_ordering`, `cpp/utility/compare/strong_ordering|std::strong_ordering`), `U` is `void`.
* Otherwise, if at least one `T` is `cpp/utility/compare/partial_ordering|std::partial_ordering`, `U` is `cpp/utility/compare/partial_ordering|std::partial_ordering`.
* Otherwise, if at least one `T` is `cpp/utility/compare/weak_ordering|std::weak_ordering`, `U` is `cpp/utility/compare/weak_ordering|std::weak_ordering`.
* Otherwise (if every `T` is `cpp/utility/compare/strong_ordering|std::strong_ordering`, or if the list is empty), `U` is `cpp/utility/compare/strong_ordering|std::strong_ordering`.

## Template parameters


### Parameters

- `...Ts` - a possibly empty list of types

## Helper template

ddcl|since=c++20|1=
template< class... Ts >
using common_comparison_category_t = common_comparison_category<Ts...>::type;

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Possible implementation

eq fun|1=
namespace detail
{
template<unsigned int>
struct common_cmpcat_base     { using type = void; };
template<>
struct common_cmpcat_base<0u> { using type = std::strong_ordering; };
template<>
struct common_cmpcat_base<2u> { using type = std::partial_ordering; };
template<>
struct common_cmpcat_base<4u> { using type = std::weak_ordering; };
template<>
struct common_cmpcat_base<6u> { using type = std::partial_ordering; };
} // namespace detail
template<class...Ts>
struct common_comparison_category :
detail::common_cmpcat_base<(0u | ... |
(std::is_same_v<Ts, std::strong_ordering>  ? 0u :
std::is_same_v<Ts, std::weak_ordering>    ? 4u :
std::is_same_v<Ts, std::partial_ordering> ? 2u : 1u)
)> {};

## Example

