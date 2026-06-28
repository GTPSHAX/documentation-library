---
title: std::chrono::operator/(calendar)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator_slash
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++20|
constexpr auto operator/( const std::chrono::year& y,
const std::chrono::month& m ) noexcept
-> std::chrono::year_month;
dcl|num=2|since=c++20|
constexpr auto operator/( const std::chrono::year& y, int m ) noexcept
-> std::chrono::year_month;
dcl|num=3|since=c++20|
constexpr auto operator/( const std::chrono::month& m,
const std::chrono::day& d ) noexcept
-> std::chrono::month_day;
dcl|num=4|since=c++20|
constexpr auto operator/( const std::chrono::month& m, int d ) noexcept
-> std::chrono::month_day;
dcl|num=5|since=c++20|
constexpr auto operator/( int m, const std::chrono::day& d ) noexcept
-> std::chrono::month_day;
dcl|num=6|since=c++20|
constexpr auto operator/( const std::chrono::day& d,
const std::chrono::month& m ) noexcept
-> std::chrono::month_day;
dcl|num=7|since=c++20|
constexpr auto operator/( const std::chrono::day& d, int m ) noexcept
-> std::chrono::month_day;
dcl|num=8|since=c++20|
constexpr auto operator/( const std::chrono::month& m,
std::chrono::last_spec ) noexcept
-> std::chrono::month_day_last;
dcl|num=9|since=c++20|
constexpr auto operator/( int m, std::chrono::last_spec ) noexcept
-> std::chrono::month_day_last;
dcl|num=10|since=c++20|
constexpr auto operator/( std::chrono::last_spec,
const std::chrono::month& m ) noexcept
-> std::chrono::month_day_last;
dcl|num=11|since=c++20|
constexpr auto operator/( std::chrono::last_spec, int m ) noexcept
-> std::chrono::month_day_last;
dcl|num=12|since=c++20|
constexpr auto operator/( const std::chrono::month& m,
const std::chrono::weekday_indexed& wdi ) noexcept
-> std::chrono::month_weekday;
dcl|num=13|since=c++20|
constexpr auto operator/( int m, const std::chrono::weekday_indexed& wdi ) noexcept
-> std::chrono::month_weekday;
dcl|num=14|since=c++20|
constexpr auto operator/( const std::chrono::weekday_indexed& wdi,
const std::chrono::month& m ) noexcept
-> std::chrono::month_weekday;
dcl|num=15|since=c++20|
constexpr auto operator/( const std::chrono::weekday_indexed& wdi, int m ) noexcept
-> std::chrono::month_weekday;
dcl|num=16|since=c++20|
constexpr auto operator/( const std::chrono::month& m,
const std::chrono::weekday_last& wdl ) noexcept
-> std::chrono::month_weekday_last;
dcl|num=17|since=c++20|
constexpr auto operator/( int m, const std::chrono::weekday_last& wdl ) noexcept
-> std::chrono::month_weekday_last;
dcl|num=18|since=c++20|
constexpr auto operator/( const std::chrono::weekday_last& wdl,
const std::chrono::month& m ) noexcept
-> std::chrono::month_weekday_last;
dcl|num=19|since=c++20|
constexpr auto operator/( const std::chrono::weekday_last& wdl, int m ) noexcept
-> std::chrono::month_weekday_last;
dcl|num=20|since=c++20|
constexpr auto operator/( const std::chrono::year_month& ym,
const std::chrono::day& d ) noexcept
-> std::chrono::year_month_day;
dcl|num=21|since=c++20|
constexpr auto operator/( const std::chrono::year_month& ym, int d ) noexcept
-> std::chrono::year_month_day;
dcl|num=22|since=c++20|
constexpr auto operator/( const std::chrono::year& y,
const std::chrono::month_day& md ) noexcept
-> std::chrono::year_month_day;
dcl|num=23|since=c++20|
constexpr auto operator/( int y, const std::chrono::month_day& md ) noexcept
-> std::chrono::year_month_day;
dcl|num=24|since=c++20|
constexpr auto operator/( const std::chrono::month_day& md,
const std::chrono::year& y ) noexcept
-> std::chrono::year_month_day;
dcl|num=25|since=c++20|
constexpr auto operator/( const std::chrono::month_day& md, int y ) noexcept
-> std::chrono::year_month_day;
dcl|num=26|since=c++20|
constexpr auto operator/( const std::chrono::year_month& ym,
std::chrono::last_spec ) noexcept
-> std::chrono::year_month_day_last;
dcl|num=27|since=c++20|
constexpr auto operator/( const std::chrono::year& y,
const std::chrono::month_day_last& mdl ) noexcept
-> std::chrono::year_month_day_last;
dcl|num=28|since=c++20|
constexpr auto operator/( int y, const std::chrono::month_day_last& mdl ) noexcept
-> std::chrono::year_month_day_last;
dcl|num=29|since=c++20|
constexpr auto operator/( const std::chrono::month_day_last& mdl,
const std::chrono::year& y ) noexcept
-> std::chrono::year_month_day_last;
dcl|num=30|since=c++20|
constexpr auto operator/( const std::chrono::month_day_last& mdl, int y ) noexcept
-> std::chrono::year_month_day_last;
dcl|num=31|since=c++20|
constexpr auto operator/( const std::chrono::year_month& ym,
const std::chrono::weekday_indexed& wdi ) noexcept
-> std::chrono::year_month_weekday;
dcl|num=32|since=c++20|
constexpr auto operator/( const std::chrono::year& y,
const std::chrono::month_weekday& mwd ) noexcept
-> std::chrono::year_month_weekday;
dcl|num=33|since=c++20|
constexpr auto operator/( int y, const std::chrono::month_weekday& mwd ) noexcept
-> std::chrono::year_month_weekday;
dcl|num=34|since=c++20|
constexpr auto operator/( const std::chrono::month_weekday& mwd,
const std::chrono::year& y ) noexcept
-> std::chrono::year_month_weekday;
dcl|num=35|since=c++20|
constexpr auto operator/( const std::chrono::month_weekday& mwd, int y ) noexcept
-> std::chrono::year_month_weekday;
dcl|num=36|since=c++20|
constexpr auto operator/( const std::chrono::year_month& ym,
const std::chrono::weekday_last& wdl ) noexcept
-> std::chrono::year_month_weekday_last;
dcl|num=37|since=c++20|
constexpr auto operator/( const std::chrono::year& y,
const std::chrono::month_weekday_last& mwdl ) noexcept
-> std::chrono::year_month_weekday_last;
dcl|num=38|since=c++20|
constexpr auto operator/( int y, const std::chrono::month_weekday_last& mwdl ) noexcept
-> std::chrono::year_month_weekday_last;
dcl|num=39|since=c++20|
constexpr auto operator/( const std::chrono::month_weekday_last& mwdl,
const std::chrono::year& y ) noexcept
-> std::chrono::year_month_weekday_last;
dcl|num=40|since=c++20|
constexpr auto operator/( const std::chrono::month_weekday_last& mwdl, int y ) noexcept
-> std::chrono::year_month_weekday_last;
```

These `operator/` overloads provide a conventional syntax for the creation of [Proleptic Gregorian calendar](https://en.wikipedia.org/wiki/Proleptic Gregorian calendar) dates.
For creation of a full date, any of the following three orders are accepted:
* ,
* ,
* .
In each case  can replaced with one of:
* `std::chrono::last`, for the last day of the month;
* `''weekday''[''i'']`, for the  ''weekday'' of the month;
* `''weekday''[`std::chrono::last`]`, for the last ''weekday'' of the month.
A plain integer is accepted if its meaning is unambiguous from the types of other operands: `2005y/4/5` is allowed, but `5/April/2005` is not.
Partial-date types (`year_month`, `month_day`, etc.) can be created by not applying the second `operator/` in any of the three orders.

## Return value

1. `std::chrono::year_month(y, m)`
2. `std::chrono::year_month(y, std::chrono::month(m))`
@3,6@ `std::chrono::month_day(m, d)`
4. `std::chrono::month_day(m, std::chrono::day(d))`
@5,7@ `std::chrono::month_day(std::chrono::month(m), d)`
@8,10@ `std::chrono::month_day_last(m)`
@9,11@ `std::chrono::month_day_last(std::chrono::month(m))`
@12,14@ `std::chrono::month_weekday(m, wdi)`
@13,15@ `std::chrono::month_weekday(std::chrono::month(m), wdi)`
@16,18@ `std::chrono::month_weekday_last(m, wdl)`
@17,19@ `std::chrono::month_weekday_last(std::chrono::month(m), wdl)`
20. `std::chrono::year_month_day(ym.year(), ym.month(), d)`
21. `std::chrono::year_month_day(ym.year(), ym.month(), std::chrono::day(d))`
@22,24@ `std::chrono::year_month_day(y, md.month(), md.day())`
@23,25@ `std::chrono::year_month_day(std::chrono::year(y), md.month(), md.day())`
26. `std::chrono::year_month_day_last(ym.year(), std::chrono::month_day_last(ym.month()))`
@27,29@ `std::chrono::year_month_day_last(y, mdl)`
@28,30@ `std::chrono::year_month_day_last(std::chrono::year(y), mdl)`
31. `std::chrono::year_month_weekday(ym.year(), ym.month(), wdi)`
@32,34@ `std::chrono::year_month_weekday(y, mwd.month(), mwd.weekday_indexed())`
@33,35@ `std::chrono::year_month_weekday(std::chrono::year(y), mwd.month(), mwd.weekday_indexed())`
36. `std::chrono::year_month_weekday_last(ym.year(), ym.month(), wdl)`
@37,39@ `std::chrono::year_month_weekday_last(y, mwdl.month(), mwdl.weekday_last())`
@38,40@ `std::chrono::year_month_weekday_last(std::chrono::year(y), mwdl.month(), mwdl.weekday_last())`

## Example


### Example

```cpp
#include <chrono>
using namespace std::chrono;

constexpr auto ym{2021y/8};
static_assert(ym == year_month(year(2021), August));

constexpr auto md{9/15d};
static_assert(md == month_day(September, day(15)));

constexpr auto mdl{October/last};
static_assert(mdl == month_day_last(month(10)));

constexpr auto mw{11/Monday[3]};
static_assert(mw == month_weekday(November, Monday[3]));

constexpr auto mwdl{December/Sunday[last]};
static_assert(mwdl == month_weekday_last(month(12), weekday_last(Sunday)));

// Those 3 year/month/day orders that people actually use on this planet and beyond:
constexpr auto ymd{year(2021)/January/day(23)};
static_assert(ymd == month{1}/23/2021);
static_assert(ymd == day{23}/1/2021);
static_assert(ymd == year_month_day(2021y, month(January), 23d));

int main() {}
```

