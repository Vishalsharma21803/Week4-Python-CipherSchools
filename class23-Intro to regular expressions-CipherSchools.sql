SELECT * FROM Customers
where ContactName like "%m%"





SELECT * FROM Customers
where ContactName regexp "m"


SELECT * FROM [Customers]
where ContactName like "%m%"

SELECT * FROM [Customers]
where ContactName like "M____d"

-- Q- Select all the phone nos ending with 5 in supplier's table?
SELECT * FROM [Suppliers]
where Phone like "%5"


-- REGEXP: more flexibility

SELECT * FROM Customers
where ContactName regexp "m"



SELECT * FROM [Customers]
where City REGEXP "M"

SELECT * FROM [Customers]
where City REGEXP "^M"

SELECT * FROM [Customers]
where City REGEXP "d$"

SELECT * FROM [Customers]
where City REGEXP "^M" and city REGEXP "d$"

SELECT * FROM [Customers]
where City REGEXP "a|b|c"

SELECT * FROM [Customers]
where City REGEXP "^M|d$"

SELECT * FROM [Customers]
where City REGEXP "^M|ch|d$"

SELECT * FROM [Customers]
where City REGEXP "[abc]i"

-- match with ai or bi or ci

SELECT * FROM [Customers]
where City REGEXP "[a-h]i"


