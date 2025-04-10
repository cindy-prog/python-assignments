## question one 

   SELECT paymentDate, SUM(amount) As totalAmount
   FROM payments,
   GROUP BY paymentDate,
   ORDER BY paymentDate DESC,
   LIMIT 5;

## Question two
    
    SELECT customerName, country, AVG(creditLimit) AS averagecreditLimit
    FROM customers,
    GROUP BY customerName, country;

## Question three
   
   SELECT productCode, quantityOrdered, SUM(price) AS totalPrice
   FROM orderDetails,
   GROUP BY productCode, quantityOrdered;

## Question four 
   
   SELECT checkNumber, MAX(amount) AS highestAmount
   FROM payments,
   GROUP BY checkNumber;
