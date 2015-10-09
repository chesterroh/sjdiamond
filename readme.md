
## Future To-do list

 * user auth / user registration / user deregistration feature
 * e-mail integration
 * bootstrap -- responsive web experience


## 2015.10.10

* Create user auth
* find out some deployment site

## 2015.10.09

* Create search view with proper error handling
* Adding wholesale_price column to the database
* Adding SJ diamond corporate-related information table ( such as discount_rate etc, etc ) 

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
