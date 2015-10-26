
## Future To-do list

 * e-mail integration
 * bootstrap -- responsive web experience
 * (to-do) maintaining the search condition (carat,color,clarity)

## 2015.10.27

* adding login auth

* Adding SJ diamond corporate-related information table ( such as discount_rate etc, etc )

* in order to fully implement USER auth, I should understand Forms,Views class template structure for that. then implement user auth form.. it would be a breeze!!
   -- change the view function ---> view class
   -- use custom form ---> form class
   -- then, let's create login

## 2016.10.26 

* find out some deployment site  --- select domain name --
  ---- chungdam.moreover.co.kr .. deployment

## 2015.10.12

* Adding consumer_price column to the database (DONE) + order_by price (DONE)
* Create user auth --- study completed anyway... (DONE)
* check out l.py properly works  (DONE)

## 2015.10.09

* Create search view with proper error handling (DONE)
 
## 2015.10.08

* Create search view (delayed)

* Create index/detail/stockupdate view  (priority-1) (DONE)
   - If you look at the deleted view : you can catch the trend which is sold well, which one is not..

* integrating cert_no with GIA.ORG site (DONE)

## 2015.10.05

* Model date ;;;; let's finish reading model document (DONE)

## 2015.10.03

 * DatetimeField should be changed to DateFiled... and DateField should be aligned with GIA_UPDATE_LIST ( do it with command line argument input ) (DONE)
 * Creating DB updater (DONE)
    - we should decide what kind of datetime index we use as our default input/update date. 

## 2015.10.02

* Django manual page download - wget - DONE
* changing the date-type of clarity & color to the *numeric* type
* creating database updater
   - check the cert-no in which "L" suffixes have been attached. (DONE)
   - add more field that "delete_flag",   (DONE)
   - add more field that "updated_date", update_date will be used as deleted_date once   ( Once finished with updating with new db, update_date < 2_days would be marked as delete_flag=True )  (DONE)
