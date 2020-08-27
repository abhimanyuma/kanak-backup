# Models

The base models of the project will be the following

## Transaction

Transaction will be the base unit of the transactions, and will for now represent
all that is required

1. timestamp
2. debit_account
3. debit_asset
4. debit_amount
5. exchange_rate (Calculated but stored for posterity)
6. credit_account
7. credit_asset
8. credit_amount
9. transaction_amount
10. transaction_asset_type
11. start_timestamp
12. transaction_type
13. transaction_category
14. transaction_subcategory
15. description

## Asset (also liability)

Assets are meant to be used for representing every single asset/liability we have.
Liabilities are also represented with

1. asset_type
2. start_date
3. opening_balance
4. asset_type
5. is_liability

## Account

This is an amalgamation of assets, sometimes an account may contain only one asset,
for example most bank accounts are a single currency account, however consider a
brokerage account, it is an account that holds multiple assets each of which
is a particular stock/mutual fund.

1. account_type
    - checking
    - savings
    - cash
    - debit
    - credit card
    - Investments
    - Liability

2. is_single_asset
3. account_name
4. account_description
5. start_date
6. account_currency - This is the currency in which this account will be reported

## Asset Type

Asset types represent the various assets the user can own, and this is where it is
customized to my needs.

1. category
2. symbol
3. name
4. description
5. is_physical
6. tracking_symbol
7. is_linked
