# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

Purpose: The purpose of this lab is to determine how much a costumer owes their mobile phone provider based on their package plan.

Constant numbers per package:

Package Green: 

49.99/month, 2GB of data is provided. 

Additional GB are 15/GB.

Coupon takes 20 off a bill of 75 or more.

Package Blue: 

70/month, 4GB of data provided

Additional GB are 10/GB 

Package Purple: 

99.95/month, Unlimited data

Algorithm:
1. Prompt user to input their package color. (Blue, Green, Purple)
2. While user doesn't input "green, blue, or purple" output "Invalid" 
   1. Prompt user to answer question again
   2. Convert
4. If the user inputs green use the numbers for green package constants:
* Prompt user to input the number of additional GB they want
* gb = int(input) + 2
* gb_price = 15*gb
* price = 49.99 + (gb_price)
* Ask user to input whether they have a coupon or not.
* If user chooses "no": output price
* If price > 75: coupon = price - 20
* If price < 75: coupon = price
* Output price or coupon and gb
5. If user inputs "Blue": use constants for blue
* Prompt user to input the amount of additional GB they want
* gb = int(input) + 4
* gb = 10*(gb)
* price = 70 + gb
* output price and gb
6. If user inputs purple: use constants for purple package
* price = 99.95
* output price and "Unlimited data."