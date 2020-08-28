# Kanak - How am I doing financially?

Kanak is a personal project. It combines three things, but in a way I want it.
It is going to be a wealth manager, expense tracker, and a budgeting tool. It is
specifically designed for my personal use case. If the solution works for you please
note that it is through sheer luck. It may not work in future for you.

I loved Kubera[^kubera], I really liked it, but it met only part of my requirement, what
I wanted was an app that combined both wealth tracking and an expense manager. While
I came across many wonderful solutions for expense tracking too and currently use
Home Budget[^home_budget] on my phone to track my expenses, but again want a single application,
that will eventually work across desktop, web and mobile.

Here are the questions I want to answer in a single application.

1. What was my income this month/year?
2. What were my expenses this month/year?
3. Are there any expenses that I should be aware of ahead?
4. How did my investments do this year?
5. What is the status of my liabilities this year?
6. What is the net cost adjusted CAGR of each of my investments?

In addition, there is a worry about the entire financial information being stored
online in a bad way, so this uses Web Crypto API to ensure that no information is
stored online that is accessible to anyone BUT the user.

The following are the information that is stored online that is NOT client encrypted.

1. Any documents attached to any of the transactions. Possibly at a later stage
   this will be client side encrypted.

2. Like Kubera[^kubera] this will eventually include way to backup information that
   might need to be passed on to the beneficiaries should something happen to the
   account holder. For obvious reasons these cannot be encrypted.


[kubera]: https://app.kubera.com
[home_budget]: http://www.anishu.com/homebudget.html
