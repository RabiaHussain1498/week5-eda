# Orders Dataset — Summary

## What this dataset contains
This analysis covers 5,015 synthetic customer orders, each recording an
order date, customer, product category, quantity, unit price, and region.
It is deliberately generated with realistic data-quality problems
missing values, inconsistent labels, invalid quantities, price errors, and
duplicate records to practice diagnosing and fixing the kinds of issues
that show up in real business data.

## What I found and fixe
- **Missing data**: about 3% of orders had no customer ID and were removed,
  since there's no reliable way to guess who a customer was. About 4% had
  no region recorded; rather than discard these, they were labeled
  "Unknown" so the orders themselves weren't lost.
- **Inconsistent labels**: "Electronics" and "electronics" were being
  counted as two different categories due to a capitalization mismatch
  merged into one.
- **Invalid values**: 30 orders had negative quantities (likely returns
  recorded incorrectly) corrected by converting them to their absolute
  value, restoring a valid order count. A smaller,
  related issue was also found: some prices were negative (as low as
  -$25.58), which isn't valid for a real price, these are corrected the
  same way as the negative quantities, by taking the absolute value.
  
- **Duplicate records**: 15 orders were exact duplicates of others and were
  removed to avoid double-counting.

## Beyond the assigned checklist
A few additional issues were found that weren't explicitly called out in
the assignment brief, but were worth catching:
- The customer ID column was stored as a decimal number instead of a whole
  number a side effect of having missing values and was converted back
  to a proper integer after cleaning.
- The order ID, which is supposed to uniquely identify each order, had 15
  repeated values, confirming the duplicate rows were genuine duplicates
  and not just coincidentally similar orders.
- The region column was checked for the same capitalization problem found
  in product category, and confirmed to be clean  ruling out a second
  instance of that issue rather than assuming it wasn't there.
 

## Top findings
- Average price is nearly identical across all product categories
  (roughly $44–$45), so category alone doesn't explain price differences.
- There's no relationship between how many units are ordered and the price
  per unit , customers ordering 1 item pay the same range of prices as
  customers ordering 7.
- Orders missing a region behave no differently, price-wise, than orders
  with a known region the missing data appears random, not tied to any
  underlying pattern worth further investigation.

## Honest limitation
The raw data recorded some returned orders by simply making the quantity
negative (e.g. -7 instead of 7), rather than using a separate field to
mark that an order was returned. 
To make the quantity column usable, I corrected these by converting them
back to positive numbers. This fixes the numbers, but it also erases the
one piece of information that told us which orders were returns in the
first place. After cleaning, a return and a normal order of the same size
look identical. A more complete dataset would have kept a separate
"is_return" column instead of encoding it through a negative sign.