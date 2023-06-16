

## Manually Testing Functionality
### **Navigation**

|Element               |Action|Expected Result               |Pass/Fail|
|:-------------         |:----|:----------------------------------|:---|
| **NavBar**            |                                         |    |
|Site Name              |Click|Redirect to home                   |Pass|
|My profile Dropdown    |Click|Open profile dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin logged in)   |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|My Wishlist Link     |Click|Redirect to user Wishlist page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
|Search Bar             |     |Enter key words to search products |Pass|
| **Mobile Nav**        |     |                                   |    |
|Hamburger Icon         |Click|Open Dropdown                      |Pass|
|- Home                 |Click|Redirect to home                   |Pass|
|- All Products Dropdown|Click|Displays links to All products     |Pass|
|                       |     |and filtered options and redirects |Pass|
|Search Link            |Click|Enter key words to search products |Pass|
|My Account Dropdown    |Click|Open account dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin logged in)   |Pass|
|My Wishlist Link     |Click|Redirect to user Wishlist page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
| **MainNav**           |     |                                   |    |
|All Products           |Click|Displays links to All products     |Pass|
|Dropdown               |     |and filtered options and redirects |Pass|
| **Footer**            |     |                                   |    |
|*Customer Services*    |     |                                   |    |
|FAQ's Link             |Click|Redirect to FAQ's page.            |Pass|
|Site Policy Link       |Click|Opens new tab to display policy    |Pass|
|Log in Link            |Click|Redirect to login page             |Pass|
|Register Link          |Click|Redirect to signup page            |Pass|
|*Contact us*           |     |                                   |    |
|Contact Us Link        |Click|Redirect to contact page           |Pass|
|*Mailchimp subscribe*  |     |                                   |    |
|Subscribe to newsletter|Click|Enter email to subscribe to site   |Pass|
|*Socials*              |     |                                   |    |
|Facebook Link          |Click|Open on external page (live page)  |Pass|

---
### **Home Page**
| Element               | Action| Expected Result           | Pass/Fail|
|:-------------         |:-----|:-----                            |:---|
|Shop Now button        |Click|Redirects to products page         |Pass|
|                       |Seipe|using arrow buttons or swiping     |Pass|
|                       |     |on phone                           |    |

---

### **Products Page**

| Element               | Action | Expected Result          | Pass/Fail|
|:-------------         |:-------|:-----                          |:---|
|'Sort By' Dropdown     |Click|Open 'sort by' options             |Pass|
|Product Card           |Click|Redirect to product detail page    |Pass|

---

### **Product Detail Page**

| Element               | Action |Expected Result           | Pass/Fail|
|:-------------         |:-------|:-----                          |:---|
|Qty control buttons    |Click|Increase/decrease quantity         |Fail|
|Keep Shopping button   |Click|Redirect to products page          |    |
|Add to bag button      |Click|Add item to bag                    |Pass|
|                       |     |Toast Success appears              |Pass|
|                       |     |Item visible in toast success      |Pass|
|Rate Product           |Click|Hover over the stars to rate       |Pass|
|                       |     |and click to confirm               |    |
|                       |     |(if logged in)                     |    |
|Review Product         |Enter|Leave a review of the product      |Pass|
|                       |     |(if logged in)                     |    |
|                       |     |Redirect to login page if not      |Pass|
|Read Review            |     |If a review has been left all users|Pass|
|                       |     |can read them                      |    |
|Update Review          |Click|If a review is yours update button |Pass|
|                       |     |visible and redirects to form      |    |
|Delete Review          |Click|If a review is yours delete button |Pass|
|                       |     |visible and redirects to form      |    |
|**admin only:**        |     |                                   |    |
|Edit product button    |Click|Redirect to edit product page      |Pass|
|Delete product button  |Click|Open delete confirmation modal     |Pass|

---

### **Add Product Page**

| Element               |Action| Expected Result             |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|Form Dropdown          |Click|Show dropdown category options     |Pass|
|Name field             |Enter|Field must be filled in or warning |Pass|
|Description field      |Enter|Field must be filled in or warning |Pass|
|Price field            |Enter|Field must be filled in or warning |Pass|
|Rating field           |Enter|Field must be filled in or warning |Pass|
|Image select button    |Click|Open device storage                |Pass|
|                       |     |Chosen image name displayed        |Pass|
|                       |     |If no image set, placeholder set   |Pass|
|Cancel button          |Click|Redirect to products page          |Pass|
|Add Product button     |Click|Form submit                        |Pass|
|                       |     |Redirect to product detail page    |Pass|
|                       |     |Product uploaded toast appears     |Pass|
|Add Product button     |Click|Form doesn't submit                |Pass|
|                       |     |Error messages on invalid fields   |Pass|

---

### **Edit Product Page**

| Element               |Action| Expected Result             |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|Form Dropdown          |Click|Show dropdown category options     |Pass|
|Name field             |Enter|Field must be filled in or warning |Pass|
|Description field      |Enter|Field must be filled in or warning |Pass|
|Price field            |Enter|Field must be filled in or warning |Pass|
|Rating field           |Enter|Field must be filled in or warning |Pass|
|Image select button    |Click|Open device storage                |Pass|
|                       |     |Chosen image name displayed        |Pass|
|                       |     |If no image set, placeholder set   |Pass|
|Cancel button          |Click|Redirect to products page          |Pass|
|Update Product button  |Click|Form submit                        |Pass|
|                       |     |Redirect to product detail page    |Pass|
|                       |     |Product uploaded toast appears     |Pass|
|Update Product button  |Click|Form doesn't submit                |Pass|
|                       |     |Error messages on invalid fields   |Pass|
|Toast Alert            |     |Alert you are editing product      |Pass|

---

### **Delete Product**

| Element               |Action| Expected Result             |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|Delete product         |Click|click delete button and product is |Pass|
|                       |     |deleted                            |    |

---

### **Bag Page**

| Element               |Action|Expected Result               |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|**No Bag Items**       |     |.                                  |    |
|Keep Shopping button   |Click|Redirect to products page          |Pass|
|**Bag Items**          |     |                                   |    |
|Qty control buttons    |Click|Increase/decrease quantity         |Pass|
|Update button          |Click|Update bag item quantity           |Pass|
|                       |     |Updated confirmation toast appears |Pass|
|Remove button          |Click|Remove item from bag               |Pass|
|                       |     |Removed confirmation toast appears |Pass|
|Continue shopping      |Click|Redirect to products page          |Pass|
|button                 |     |                                   |Pass|
|Checkout button        |Click|Redirect to checkout summary page  |Pass|

---

### **Checkout Summary Page**

| Element               |Action|Expected Result              |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|Checkout button        |Click|Redirect to checkout page          |Pass|


---

### **Checkout Page**

| Element                   | Action           | Expected Result                      | Pass/Fail |
|:-------------             |:-----------------|:-----                                     |:-----|
|Form fields                |On load |fields populated with user default info              |Pass  |
|(if user logged in)        |        |(if previously saved)                                |Pass  |
|Text Input(if required)    |Leave blank|On submit:form won't submit                       |Pass  |
|                           |                  |error message on invalid field(s)          |Pass  |
|                           |Fill in correctly |On submit: form submits                    |Pass  |
|Phone number Input         |Leave blank       |On submit:form won't submit                |Pass  |
|                           |                  |error message on field                     |Pass  |
|Email Input                |Leave blank       |On submit:form won't submit                |Pass  |
|                           |                  |error message on field                     |Pass  |
|                           |Fill in correctly |On submit: form submits                    |Pass  |
|Form country Dropdown      |Click             |Show dropdown options                      |Pass  |
|Save to profile checkbox   |On page           |(user logged in) Shown                     |Pass  |
|                           |On page           |(user not logged in) Not shown             |Pass  |
|                           |Checked           |On submit:Delivery information saved       |Pass  |
|                           |                  |to user profile                            |Pass  |
|                           |Unchecked         |On submit:Delivery information not saved   |Pass  |
|                           |                  |to user profile                            |Pass  |
|Payment card input         |Invalid card No.  |Error message on field                     |Pass  |
|                           |Invalid card date |Error message on field                     |Pass  |
|Adjust Bag button          |Click             |Redirect to bag page                       |Pass  |
|Complete Order button      |Click             |Form won't submit                          |Pass  |
|(form invalid)             |                  |                                           |      |
|                           |                  |Error message on invalid fields            |Pass  |
|Complete Order button      |Click             |                                           |      |
|(form valid)               |Payment succeeds  |loading screen reappears                   |Pass  |
|                           |                  |form submits                               |Pass  |
|                           |                  |redirect to checkout success page          |Pass  |
|                           |(user logged in)  |order saved to user profile                |Pass  |
|                           |Payment failed    |Loading animation appears                  |Pass  |
|                           |                  |form won't submit                          |Pass  |
|                           |                  |error message at bottom of form            |Pass  |
|              |Payment Requires authentication|Loading animation appears                  |Pass  |
|                           |                  |Authentication box appears                 |Pass  |
|Fail Authentication button |Click             |Authentication box closes                  |Pass  |
|                           |                  |User directed back to form                 |Pass  |
|                           |                  |error message at bottom of form            |Pass  |
|Complete Authentication button|Click          |loading screen reappears                   |Pass  |
|                           |                  |form submits                               |Pass  |
|                           |                  |redirect to order confirmation page        |Pass  |
|                           |(user logged in)  |order saved to user profile                |Pass  |

---

### **Checkout Success Page**

| Element                   | Action | Expected Result         | Pass/Fail |
|:-------------             |:-------|:-----                        |:-----|
|Shop Again! button         |Click   |Redirect to products page       |Pass|

---

### **Profile Page**

| Element                   | Action           | Expected Result                      | Pass/Fail |
|:-------------             |:-----------------|:------------------------------------------|:-----|
|Form fields         |On load |fields populated with user default info(if previously saved)|Pass  |
|All input fields           |Leave blank       |On submit: form submits                    |Pass  |
|                           |Just whitespace   |On submit: form submits                    |Pass  |
|                           |Fill in correctly |On submit: form submits                    |Pass  |
|Form Dropdown              |Click             |Show dropdown options                      |Pass  |
|Update button              |Click             |Form submits                               |Pass  |
|                           |                  |Form updated toast appears                 |Pass  |
|Previous order number      |Click             |Redirect to previous order page            |Pass  |

---

### **Previous Order Page**

| Element                   | Action | Expected Result           |Pass/Fail|
|:-------------             |:----|:-----                            |:---|
|Toast                      |loads|Previous order info toast appears |    |
|Back to Profile button     |Click|Redirect to profile page          |Pass|

---

### **FAQ's Page**

| Element                   | Action | Expected Result          |Pass/Fail|
|:-------------             |:----|:-----                           |:----|
|Home button                |Click|Redirect to Home page             |Pass|
|Contact link in answer     |Click|Redirect to contact page          |Pass|

---

---

### **Allauth Pages**

| Element                   | Action | Expected Result                   | Pass/Fail |
|:-------------             |:-------|:---------------------------------------|:-----|
|**Register**               |        |                                        |      |
|Sign in link               |Click   |Redirect to sign in page                |Pass  |
|*Form*                     |        |                                        |      |
|Email field                |Fill in |On submit: form wont'submit             |Pass  |
|(incorrect format)         |        |Error message on invalid field          |Pass  |
|(correct format)           |Fill in |On submit: form submit                  |Pass  |
|(email already used)       |Fill in |On submit: form wont'submit             |Pass  |
|                           |        |Error message on invalid field          |Pass  |
|(email not already used)   |Fill in |On submit: form submit                  |Pass  |
|Username field             |Fill in |On submit: form submit                  |Pass  |
|(correct format)           |        |                                        |Pass  |
|(username already used)    |Fill in|On submit: form wont'submit              |Pass  |
|                           |        |Error message on invalid field          |Pass  |
|(username not already used)|Fill in|On submit: form submit                   |Pass  |
|Password field             |Fill in |On submit: form wont'submit             |Pass  |
|(incorrect format)         |        |error message on invalid field          |Pass  |
|(correct format)           |Fill in |On submit: form submits                 |Pass  |
|(passwords don't match)    |Fill in|On submit: form wont'submit              |Pass  |
|                           |        |error message on invalid field          |Pass  |
|(passwords match)          |Fill in |On submit: form submit                  |Pass  |
|Sign Up button(form invalid)|Click  |Form wont'submit                        |Pass  |
|                           |        |error message on invalid fields         |Pass  |
|Sign Up button(form valid) |Click   |Form submit                             |Pass  |
|                           |        |redirect to email verification page     |Pass  |
|                           |        |email sent to user                      |Pass  |
|**Email Verification**     |        |                                        |      |
|Follow link from email     |Click   |redirect to confirm email page          |Pass  |
|Confirm button             |Click   |redirect to log in page                 |Pass  |
|                           |        |email confirmation toast appears        |Pass  |
|                           |        |with discount coupon code               |Pass  |
|**Login**                  |        |                                        |      |
|Sign up link               |Click   |Redirect to sign up page                |Pass  |
|*Form*                     |        |                                        |      |
|Username Field             |Fill in|On submit:form won't submit              |Pass  |
|(wrong username)           |        |error message for username/password     |Pass  |
|Password Field             |Fill in|On submit:form won't submit              |Pass  |
|(wrong password)           |        |error message for username/password     |Pass  |
|Forgot Password button     |Click   |redirect to password reset page         |Pass  |
|Sign In button(form invalid)|Click  |form won't submit                       |Pass  |
|                           |        |error message on invalid field(s)       |Pass  |
|Sign In button(form valid) |Click   |form submit                             |Pass  |
|                           |        |redirect to home page                   |Pass  |
|                           |        |sign in confirmation toast appears      |Pass  |
|**Logout Confirmation**    |        |                                        |      |
|Sign out button            |Click   |Redirect to homepage                    |Pass  |
|                           |        |Sign out confirmation toast appears     |Pass  |

---
---
