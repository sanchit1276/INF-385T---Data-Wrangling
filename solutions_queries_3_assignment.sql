
-- Q1. What is the name of the person who spent the most (and how much did they spend)?

-- We need the name of person
SELECT *
FROM people

-- Need the amount of money he or she spent
-- Accordingly, we need to join the tables which have information about purchases a person made & tickets belong to a purchase. A person may have made
-- more than one purchase.
SELECT *
FROM people, purchases, tickets
WHERE people.id = purchases.person_id
	AND purchases.id = tickets.purchase_id

SELECT *
FROM people, purchases, tickets
WHERE people.id = purchases.person_id
	AND purchases.id = tickets.purchase_id
ORDER BY people.id

-- Group the joined table by people.id, and perform SUM() on each group to get aggregate value.
SELECT people.name, people.id, SUM(tickets.price) AS total_spending
FROM people, purchases, tickets
WHERE people.id = purchases.person_id
	AND purchases.id = tickets.purchase_id
GROUP BY people.id

-- Sort the output in descending order
SELECT people.name, people.id, SUM(tickets.price) AS total_spending
FROM people, purchases, tickets
WHERE people.id = purchases.person_id
	AND purchases.id = tickets.purchase_id
GROUP BY people.id
ORDER BY total_spending DESC

-- Finally, get the first row
SELECT people.name, people.id, SUM( tickets.price) AS total_spending
FROM people, purchases, tickets
WHERE people.id = purchases.person_id
	AND purchases.id = tickets.purchase_id
GROUP BY people.id
ORDER BY total_spending DESC
LIMIT 1

-- Vebil Miesys	765

-- Q2. Which performance had the highest revenue? (ticket prices are incoming income, thus revenue)

-- We need information about performance and ticket prices
-- That is to say, we need performances table and tickets table
SELECT *
FROM performances, tickets
WHERE performances.id = tickets.performance_id

SELECT *
FROM performances, tickets
WHERE performances.id = tickets.performance_id
ORDER BY performances.id

-- Group the joined table by performance.id & perform SUM() function on each group.
SELECT performances.id, SUM(tickets.price) AS revenue
FROM performances, tickets
WHERE performances.id = tickets.performance_id
GROUP BY performances.id

-- Sort the output in the order that revenue is highest
SELECT performances.id, SUM(tickets.price) AS revenue
FROM performances, tickets
WHERE performances.id = tickets.performance_id
GROUP BY performances.id
ORDER BY revenue DESC

-- Finally, get the first row, using LIMIT clause.
SELECT performances.id, SUM(tickets.price) AS revenue
FROM performances, tickets
WHERE performances.id = tickets.performance_id
GROUP BY performances.id
ORDER BY revenue DESC
LIMIT 1;

--Answer: id- 41, revenue- 57968

-- Q3. Which performance was the most profitable? (profit is revenue - costs.  bands.fee is the cost)

-- Start with the performances table.
SELECT *
FROM performances

-- We need to get the value of revenue and bands.fee
-- That means we need to join other tables such as tickets & bands.
SELECT *
FROM performances, tickets
WHERE performances.id = tickets.performance_id

SELECT *
FROM performances, tickets, bands
WHERE performances.id = tickets.performance_id
AND bands.id = performances.band_id

SELECT *
FROM performances, tickets, bands
WHERE performances.id = tickets.performance_id
AND bands.id = performances.band_id
ORDER BY performances.id

-- GROUP the joined table by performances.id & perform SUM() on each partitioned group.
SELECT performances.id, SUM(tickets.price)
FROM performances, tickets, bands
WHERE performances.id = tickets.performance_id
AND bands.id = performances.band_id
GROUP BY performances.id

-- We want to subtract bands.fee to get the profit value.
SELECT performances.id, SUM(tickets.price) - bands.fee AS profit
FROM performances, tickets, bands
WHERE performances.id = tickets.performance_id
AND bands.id = performances.band_id
GROUP BY performances.id
ORDER BY profit DESC

-- Finally, we get the first row
SELECT performances.id, SUM(tickets.price) - bands.fee AS profit
FROM performances, tickets, bands
WHERE performances.id = tickets.performance_id
AND bands.id = performances.band_id
GROUP BY performances.id
ORDER BY profit DESC
LIMIT 1

--Answer id-41 with profit 53305

-- Q4. Which band was the least profitable for the festival? (note: bands are paid their fee for each performance, hint: dealing with that requires a COUNT(DISTINCT ...) within a group) (If you have trouble with this one, just do as though they are only paid the fee once).

-- Start with the bands table.
-- It has the value of bands.fee
SELECT *
FROM bands

-- We need to join the table that has tickets.price to get the value of profits.
-- We can go to tickets table via the performances table.
SELECT *
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
  AND tickets.performance_id = performances.id

-- The question is about bands, not individual performances, so we want to
-- order the table by band.
SELECT *
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
  AND tickets.performance_id = performances.id
ORDER BY bands.id

-- We're going to get the revenue per band by adding up all the tickets.price.

-- But we also need to get the number of performances. Looking inside each group
-- we can see that we have the performance_id column and the unique values of that gives us the count of performances for each band.

-- So the group gets collapsed in two different ways.

-- Note that when my SELECT is complicated I swap to one column per line.

SELECT bands.id,
       SUM(tickets.price) AS revenue,
	   COUNT(DISTINCT performances.id) * bands.fee AS cost
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
  AND tickets.performance_id = performances.id
GROUP BY bands.id

-- Now do some math with revenue and cost values to get profit.
-- We can't just do revenue - cost AS profit_per_band because
-- those columns don't exist yet, so we have to repeat the calculations.
SELECT bands.id, bands.name,
       SUM(tickets.price) AS revenue,
	   COUNT(DISTINCT performances.id) * bands.fee AS cost,
	   -- revenue - cost AS profit_per_bands
       SUM(tickets.price) - (COUNT(DISTINCT performances.id) * bands.fee) AS profit_per_bands
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
  AND tickets.performance_id = performances.id
GROUP BY bands.id

-- Sort the output in ascending order
SELECT bands.id, bands.name,
       SUM(tickets.price) AS revenue,
	   COUNT(DISTINCT performances.id) * bands.fee AS cost,
       SUM(tickets.price) - (COUNT(DISTINCT performances.id) * bands.fee) AS profit_per_bands
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
  AND tickets.performance_id = performances.id
GROUP BY bands.id
ORDER BY profit_per_bands ASC

-- Finally, we get the first row, using LIMIT clause.
SELECT bands.id, bands.name,
       SUM(tickets.price) AS revenue,
	   COUNT(DISTINCT performances.id) * bands.fee AS cost,
       SUM(tickets.price) - (COUNT(DISTINCT performances.id) * bands.fee) AS profit_per_bands
FROM bands, performances, tickets
WHERE bands.id = performances.band_id
	AND tickets.performance_id = performances.id
GROUP BY bands.id
ORDER BY profit_per_bands ASC
LIMIT 1

ORDER BY SUM(tickets.price - bands.fee) as profit

-- ANSWER: id 87, WAX, profit: 2279 (Revenue- 2519, cost- 240)

-- Q5. Which venues were oversold (and what were their capacities)? (hint: this should use a HAVING clause) (oversold requires math around capacity)

-- Start with the venues table
SELECT *
FROM venues

-- To count the number of tickets sold, we need to join the tickets table over performances
SELECT *
FROM venues, performances
WHERE venues.id = performances.venue_id

SELECT *
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
  AND tickets.performance_id = performances.id

-- For a venue to be oversold it means that there was at least one performance
-- in which the venue was oversold. So we're going to count the number of
-- tickets sold for each show.

SELECT *
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
  AND tickets.performance_id = performances.id
ORDER BY performances.id

-- Now we can do our three part GROUP BY move.

SELECT performances.id, COUNT(*) as tickets_sold
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
  AND tickets.performance_id = performances.id
GROUP BY performances.id

-- Do math with a number of tickets per performance held in a venue and capacity
SELECT performances.id,
       COUNT(*) as tickets_sold,
	   venues.capacity
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
	AND tickets.performance_id = performances.id
GROUP BY performances.id

-- Now we want to fitler group aggregate value on HAVING clause
SELECT performances.id,
       COUNT(*) as tickets_sold,
	   venues.capacity
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
	AND tickets.performance_id = performances.id
GROUP BY performances.id
HAVING tickets_sold > venues.capacity

-- Get the name of venue. Only one venue per performance, so we can
-- add venue name in.
SELECT performances.id,
       venues.name,
       COUNT(*) as tickets_sold,
	   venues.capacity
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
	AND tickets.performance_id = performances.id
GROUP BY performances.id
HAVING tickets_sold > venues.capacity

-- Gives:
--
-- name	capacity	overselling
-- AMD		700			164
-- AMD		700			67
-- AMD		700			120
-- AMD		700			114
-- AMD		700			116
-- AMD		700			181
-- AMD		700			110
-- AMD		700			142
-- AMD		700			105
-- AMD		700			85
-- AMD		700			138
-- AMD		700			119
-- AMD		700			108
-- AMD		700			117

-- We can't simply get only the venue name because we can't use DISTINCT
-- to reduce the repeated venue names while also using tickets_sold in HAVING.
-- We have to have the columns used in HAVING in the SELECT.

-- This is an option, but I don't like it because doesn't have the GROUP BY
-- variable in the SELECT.
SELECT DISTINCT venues.name, venues.capacity
FROM venues, performances, tickets
WHERE venues.id = performances.venue_id
	AND tickets.performance_id = performances.id
GROUP BY performances.id
HAVING COUNT(*) > venues.capacity

-- My preference is to treat the results table as a table to make further queries from, using a sub-query.
SELECT DISTINCT oversolds.venue_name
FROM (
	SELECT performances.id,
	       venues.name as venue_name,
	       COUNT(*) as tickets_sold,
		   venues.capacity
	FROM venues, performances, tickets
	WHERE venues.id = performances.venue_id
		AND tickets.performance_id = performances.id
	GROUP BY performances.id
	HAVING tickets_sold > venues.capacity
) as oversolds

-- Q6. What was the total revenue from ticket sales each month? (hint: needs MONTH(date) in the SELECT clause)

-- Start with the tickets table
SELECT *
FROM tickets

-- We need to get date information from purchases table
SELECT *
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id

-- We are going to order the table by the purchases.date column.
SELECT *
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id
ORDER BY purchases.date

-- But we actually want to group by just part of the date.
-- MONTH(purchases.date) pulls that part out for us.
SELECT *
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id
ORDER BY MONTH(purchases.date)

-- GROUP the joined table by each month, using MONTH() function.
SELECT MONTH(purchases.date), SUM(tickets.price) as total_revenue_per_month
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id
GROUP BY MONTH(purchases.date)

-- MONTH(purchases.date)	SUM( tickets.price)
-- 1						264510
-- 2						226199
-- 3						247469
-- 4						254352
-- 5						281448
-- 6						258480
-- 7						260668
-- 8						263922
-- 9						127317


-- Q7. What was the average purchase total each month? (note: purchase total is the sum of the price of tickets bought together in the same purchase, Q1 in in-class exercises.) (two ways to get this done, one that uses AVG and that uses /).

-- Start with the tickets table
SELECT *
FROM tickets

-- We need to get date information from purchases table
SELECT *
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id

-- It can be helpful, if we look at the joined table by sorting it with the MONTH(purchases.date)
SELECT *
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id
ORDER BY MONTH(purchases.date) ASC

-- Given that purchase total is the sum of the price of tickets bought together in the same purchase, we divide the SUM(tickets.price) into the number of distinct purchases. COUNT(DISTINCT tickets.purchase_id) gives us the number of purchases each month, while still allowing us to add up the tickets total.
-- i.e., total tickets sold in month / number of purchases in month.
SELECT MONTH(purchases.date),
       SUM(tickets.price) / COUNT(DISTINCT tickets.purchase_id)
FROM tickets, purchases
WHERE tickets.purchase_id = purchases.id
GROUP BY MONTH(purchases.date)


-- month	avg_purchase
-- 1		201.7620
-- 2		203.2336
-- 3		204.6890
-- 4		202.3484
-- 5		207.2518
-- 6		203.2075
-- 7		196.4341
-- 8		205.2271
-- 9		200.4992

-- Note you can also use MONTHNAME.

--Another way to answer this question, using a subquery.

-- First add up totals for each purchase.
SELECT *
FROM tickets, purchases
WHERE purchases.id = tickets.purchase_id
ORDER BY purchases.id

SELECT purchases.id, SUM(tickets.price) AS total_of_purchase
FROM tickets, purchases
WHERE purchases.id = tickets.purchase_id
GROUP BY purchases.id

-- add the date of the purchase in. Only one date for a purchase
-- so it's safe to add this to the SELECT.
SELECT purchases.id, purchases.date, SUM(tickets.price) AS total
FROM tickets, purchases
WHERE purchases.id = tickets.purchase_id
GROUP BY purchases.id

-- Now treat that results table as a new table and calculte AVG.
SELECT MONTH(purchase_totals.date),
       AVG(purchase_totals.total) as avg_total_purchase_for_month,
FROM (
	SELECT purchases.id, purchases.date, SUM(tickets.price) AS total
	FROM tickets, purchases
	WHERE purchases.id = tickets.purchase_id
	GROUP BY purchases.id
) AS purchase_totals
GROUP BY MONTH(purchase_totals.date)
