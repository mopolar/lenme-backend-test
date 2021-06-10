# Use case
One of Lenme’s borrowers submitted a loan request for $5,000 to pay them back in 6 months. They received an offer from one of the investors on the platform with a 15% Annual Interest Rate. A $3.00 Lenme fee will be added to the total loan amount to be paid by the investor.


## Requirements:
You are required to develop a Django REST project to be able to build the following flow-through its APIs;
1. The borrower submits a loan request for $5,000 `loan amount` and 6 months `loan period`
2. The investor will submit an offer to the borrower with 15% `Annual Interest Rate`
3. The borrower will accept the offer
4. Check if the investor has sufficient balance in their account to fund the `Total Loan Amount` (Loan Amount + Lenme Fee)
5. The loan will be funded successfully and the loan status will be `Funded`
6. Six monthly payments will be scheduled from the day the loan was funded successfully
7. Once all the payments are successfully paid back to the investor, the loan status will be changed to `Completed`
---


## Virtualenv & Dependencies

create a virtualenv and run requirements.txt<br/>
<b>virtualenv</b>

<pre>pip install virtualenv</pre>

<pre>$ pip install -r requirements.txt</pre>

here <b>env/</b> folder contains all dependencies

## Running locally

<ol>
  <li>
      clone repository 
  </li>
  <li>
    run migrations 
    <pre>$ python manage.py migrate</pre>
  </li>
  <li>
    now, runserver 
    <pre>$ python manage.py runserver</pre>
  </li>
 </ol>
