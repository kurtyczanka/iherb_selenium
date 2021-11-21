# Example of automated tests in Selenium
This repository contains UI test cases using Python and Selenium
for www.iherb.com website.

# Test cases
|ID      | Test case | Description|
|--------|-----------|-----------------------------|
| 001    | Add product to cart from home page | Given Application is open on www.iherb.com  <br> When I add product to a cart from home page <br> Then Value of quantity in basket increase by one |
| 002    | Check product title on product page|Given Application is open on www.iherb.com <br> When I click on product from trending category <br> Then Product title on product page is equal to product title on home page |
| 003    | Add product to cart from product page |Given Application is open on www.iherb.com  <br> When I click on product from trending category <br> And Click Add to cart button on product page <br> Then Cart popup is displayed <br> And Value of quantity in basket increase by one|
| 004    | Search product on home page | Given Application is open on www.iherb.com  <br> When I search for 'Carmex strawberry 10g' on home page <br> Then One product will be displayed |
| 005    | Switch number of shown product on page | Given Application is open on www.iherb.com  <br> When I search for 'Shampoo' on home page <br> And change number of shown products <br> Then Number of products on page is equal to selected|

# Run tests
* In order to run prepare your environment
> $ python3 -m venv .venv
> $ pip3 install -r requirements.txt

* Run tests
> $ python3 -m unittest