# DreamBuild Fitness

Welcome to my Project 5 for Code Institute's Full-Stack Development Program  – DreamBuild Fitness, where we combine cutting-edge technology and expert fitness solutions to create a dynamic and engaging B2C experience. Powered by a robust stack of HTML, CSS, JavaScript, Python, and Django, DreamBuild Fitness is not just a fitness website; it's a testament to the seamless integration of technology and wellness. 

As we embark on this exciting journey, let's explore how our platform leverages these technologies, including Stripe, to offer you an exceptional fitness, shopping, and community-building experience, all in one place. Stripe, a secure and efficient payment gateway, ensures your transactions are smooth and hassle-free as you invest in your fitness journey with us.

![Screenshot of the site on Am I responsive](./readme_assets/img/am-i-responsive.jpg)

[View the live project here.](https://dreambuildfitness-7af9d60474bd.herokuapp.com/)

---

## Table of Contents
* [User Experience (UX)](#user-experience-ux)
    * [Intended Audience](#intended-audience)
    * [User Stories](#user-stories)
* [E-Commerce Business Model](#e-commerce-business-model)
    * [Facebook Marketing](#facebook-marketing)
    * [SEO](#seo)
* [Design](#design)
    * [Wireframes & Bootstrap Templates](#wireframes--bootstrap-templates)
    * [Colour Scheme](#colour-scheme)
    * [Typograpy](#typography)
    * [Imagery](#imagery)
    * [Database Design](#database-design)
* [Features](#features)
    * [Main Header](#main-header)
    * [Navigation](#navigation)
    * [Hero Section](#hero-section)
    * [Footer](#footer)
    * [About Us](#about-us)
    * []()
    * []()
    * []()
    * []()
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Future Testing](#future-testing)
* [Bugs](#bugs)
* [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)

---

# User Experience (UX)

This website is designed to give users and future customers the ability to browse for their latest piece of gym clothing or accessory to enchance their workouts, or if they a bit more help, there is a variety of plans available! It gives the user the ability browse all categorys, or search for possible items they're looking for, set up an account, make purchases, receive confirmation emails, check previous orders and sign up for our newsletter.  


## Intended Audience

DreamBuild Fitness aims to cater to a diverse audience, offering resources and products to help people at various fitness levels and with different fitness goals.

* **Fitness Enthusiasts**: Individuals who are passionate about fitness, exercise, and maintaining a healthy lifestyle.
* **Beginners**: People who are new to fitness and seek guidance on workouts, clothing, and nutrition to kickstart their fitness journey.
* **Seasoned Athletes**: Experienced athletes looking for advanced training programs and high-quality workout apparel to elevate their performance.
* **Health-conscious Individuals**: Those focused on improving their overall well-being, including diet and exercise.
* **Shoppers**: Users interested in stylish and functional gym clothing and accessories.
* **Busy Professionals**: Individuals looking for efficient workout solutions and meal plans to fit their busy schedules.
* **Tech-Savvy Users**: Those who appreciate websites that incorporate modern web development technologies for a smooth and visually appealing user experience.

<br>

## User Stories

Many user stories were developed for the project using Agile development methodology, for the project see the [DreamBuild Project](https://github.com/users/DeanBurke/projects/3/views/1).

#### **Buyer**
 * [Issue #1](https://github.com/DeanBurke/DreamBuild/issues/1) I can view a list of products so that I can select some to purchase.
 * [Issue #2](https://github.com/DeanBurke/DreamBuild/issues/2) I can view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
 * [Issue #3](https://github.com/DeanBurke/DreamBuild/issues/3) I can view individual product details so that I can identify the price, description, product rating, product image and available sizes.
 * [Issue #4](https://github.com/DeanBurke/DreamBuild/issues/4) I can quickly find what plans are available so that I can decide what training or meal plan is needed.
 * [Issue #5](https://github.com/DeanBurke/DreamBuild/issues/5) I can easily view the total of my purchases at any time so that I can avoid spending too much.
 * [Issue #11](https://github.com/DeanBurke/DreamBuild/issues/11) I can sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
 * [Issue #12](https://github.com/DeanBurke/DreamBuild/issues/12) I can sort a specific category of product so that I can find the best-priced or best-rated product in a specific category sort the products in that category by name.
 * [Issue #13](https://github.com/DeanBurke/DreamBuild/issues/13) I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories, such as "clothing" or "accessories".
 * [Issue #14](https://github.com/DeanBurke/DreamBuild/issues/14) I can search for a product by name or description so that I can Find a specific product I'd like to purchaset.
 * [Issue #15](https://github.com/DeanBurke/DreamBuild/issues/15) I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
 * [Issue #16](https://github.com/DeanBurke/DreamBuild/issues/16) I can easily select the size and quantity of a product when purchasing it so that I can Ensure I don't accidently select the wrong product, quantity or size.
 * [Issue #17](https://github.com/DeanBurke/DreamBuild/issues/17) I can view items in my bag to be purchased so that I can identiy the total cost of my purchase and all items I will receive.
 * [Issue #18](https://github.com/DeanBurke/DreamBuild/issues/18) I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
 * [Issue #19](https://github.com/DeanBurke/DreamBuild/issues/19) I can easily enter my payment information so that I can check out quickly and with no hassles.
 * [Issue #20](https://github.com/DeanBurke/DreamBuild/issues/20) I can feel my personal and payment information is safe and secure so that I can Confidently provide the needed information to make a purhcase.
 * [Issue #21](https://github.com/DeanBurke/DreamBuild/issues/21) I can view an order confirmation after checkout so that I can Verify that I haven't made any mistakes.
 * [Issue #22](https://github.com/DeanBurke/DreamBuild/issues/22) I can receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.

#### **Site User**
 * [Issue #6](https://github.com/DeanBurke/DreamBuild/issues/6) I can easily register for an account so that I can have a personal account and be able to view my profile.
 * [Issue #7](https://github.com/DeanBurke/DreamBuild/issues/7) I can easily login or logout so that I can access my personal account information.
 * [Issue #8](https://github.com/DeanBurke/DreamBuild/issues/8) I can easily recover my password in case I forget it so that I can Recover access to my account.
 * [Issue #9](https://github.com/DeanBurke/DreamBuild/issues/9) I can receive an email confirmation after registering so that I can verify that my account registration was successful.
 * [Issue #10](https://github.com/DeanBurke/DreamBuild/issues/10) I can have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information.
 * [Issue #26](https://github.com/DeanBurke/DreamBuild/issues/26) I can see if I'm on an error page so that I can see where I've gone wrong within the URL but not to be took away from the styling of the website.
 * [Issue #27](https://github.com/DeanBurke/DreamBuild/issues/27) I can view the company's about page so that I can find out a bit more and possibly contact them.

#### **Website Admin/Owner**
 * [Issue #23](https://github.com/DeanBurke/DreamBuild/issues/23) I can add a product so that I can add new items to my store.
 * [Issue #24](https://github.com/DeanBurke/DreamBuild/issues/24) I can edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
 * [Issue #25](https://github.com/DeanBurke/DreamBuild/issues/25) I can delete a product so that I can Remove items that no longer for sale.

<br>

![Screenshot of the User Stories Project](./readme_assets/img/user-stories.jpg)

[Back to top &uarr;](#dreambuild-fitness)

---

# E-Commerce Business Model

DreamBuild Fitness operates on a robust B2C e-commerce business model, serving as a direct bridge between our fitness-centric offerings and our valued customers. In this model, we focus on delivering a seamless, user-friendly shopping experience for fitness enthusiasts of all levels. With a wide array of high-quality gym clothing, accessories, and health-focused resources, we bring the world of fitness to our customers' fingertips. We offer a free delivery on all orders placed that are over £50. We've used social media marketing along with email marketing to reach a wider audience - with the hope of branching out towards using the following techniques in future: 

* **Influencer Collaborations**: Partner with fitness influencers and trainers to promote the brand. Their endorsements and testimonials can have a significant impact.
* **Community Building**: Create a forum or discussion board on the website where users can interact, share their fitness journeys, and provide support to one another.
* **Loyalty Programs**: Introduce loyalty programs that reward customers for repeated purchases or referrals, encouraging brand loyalty.
* **Targeted Advertising**: Utilize online advertising platforms like Google Ads and social media ads to reach potential customers based on their interests, demographics, and online behavior.
* **Affiliate Marketing**: Establish an affiliate program where fitness bloggers and enthusiasts can earn commissions for promoting DreamBuild Fitness products.

## Facebook Marketing

A Facebook business page was created for this website, which is [linked](https://www.facebook.com/profile.php?id=61552476312298) within the footer of the website. Due to Facebook, possibly removing it, as they don't allow fake businesses to be advertised, screenshots have been took(as per below).

<details>
<summary>Facebook Media</summary>

![Picture 1 of the Facebook website](./readme_assets/img/facebook-1.jpg)

![Picture 2 of the Facebook website](./readme_assets/img/facebook-2.jpg)

![Picture 3 of the Facebook website](./readme_assets/img/facebook-3.jpg)

</details>

## SEO

The website places a strong emphasis on Search Engine Optimization (SEO) to ensure that our valuable fitness resources and premium products are easily discoverable by our target audience. Our commitment to SEO involves meticulous use of meta tags, sitemap.xml, and robots.txt files. Meta tags are strategically crafted to accurately represent the content and purpose of each web page with their use in the base.html file, enhancing our visibility on search engine result pages (SERPs). 

Meanwhile, our sitemap.xml file provides search engines with a structured map of our website, ensuring that all pages are properly indexed, and updates are promptly recognized. Additionally, our robots.txt file is configured to guide search engine crawlers, allowing them to focus on indexing relevant content while respecting privacy and security settings. By employing these SEO strategies, DreamBuild Fitness ensures that fitness enthusiasts and potential customers can easily find the valuable fitness information and high-quality products they seek, reinforcing our position as a reliable and accessible online fitness resource.

[Back to top &uarr;](#dreambuild-fitness)

---

# Design

## Wireframes & Bootstrap Templates

For the site design, I took inspiration from the Boutique Ado walkthrough project along with the [Gymshark](https://uk.gymshark.com/) and [ALLSAINTS](https://www.allsaints.com/men.html) website.

Wireframes were created for the site with [Wireframe.cc](https://wireframe.cc/)

![Screenshot of home page for desktop done on Wireframe.cc](./readme_assets/img/wireframes-desktop.jpg)

<br>

![Screenshot of products page for mobile done on Wireframe.cc](./readme_assets/img/wireframes-mobile.jpg)

<br>

## Colour Scheme

Colour palette was created using: 

* [Colormind](http://colormind.io/)

![Screenshot of colour palette done on colormind.io](./readme_assets/img/colormind.jpg)

Along with a bright vibrant blue gradient for the Hero image. 

<br>

## Typography

Lato was chosen from [Google Fonts](https://fonts.google.com/).

![Screenshot of Lato font from Google fonts](./readme_assets/img/fonts-lato.jpg)

<br>


## Imagery

Images are located throught the website. As the header/hero image, on the about page, and as products throughout. 

Images were took from stock photo websites: 

* [Pexels](https://www.pexels.com/)
* [Freepik](https://www.freepik.com/)
* [Unsplash](https://unsplash.com/)

Along with some example of products took from various gym stores, as this is purely a fake website. (**No copyright infringement intended**):

* [MyProtein](https://www.myprotein.com/)
* [Gymshark](https://uk.gymshark.com/)
* [Pursue Fitness](https://www.pursuefitness.com/)
* [Decathalon](https://www.decathlon.co.uk/)
* [Lifthing the Dream](https://www.liftingthedream.com/)
* [Strength Shop](https://www.strengthshop.co.uk/)


Icons were used throught the website, for buttons, menu layout, challenge section, contact seciont and for social links on the footer of the website. The icons used on the site were taken from: 

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://icons.getbootstrap.com/)

<br>

## Database Design

Multiple apps and classes/models were created for the project, each one supporting the full site functionality.

* **About App** - No classes or models needed as just an about page

* **Bag App** - No classes or models needed, primarily focused on bag calculations via context.py

* **Checkout App** - Order and OrderLineItem models

    * Order Model:

    |Name           |Database Key   |Field Type     |Validation                                                                            |
    |---------------|---------------|---------------|--------------------------------------------------------------------------------------|
    |order_number   |order_number   |CharField      |max_length=32, null=False, editable=False                                             |
    |user_profile   |user_profile   |ForeignKey     |'UserProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'|
    |full_name      |full_name      |CharField      |max_length=50, null=False, blank=False                                                |
    |email          |email          |EmailField     |max_length=254, null=False, blank=False                                               |
    |phone_number   |phone_number   |CharField      |max_length=20, null=False, blank=False                                                |
    |country        |country        |CountryField   |blank_label='Country *', null=False, blank=False                                      |
    |postcode       |postcode       |CharField      |max_length=20, null=True, blank=True                                                  |
    |town_or_city   |town_or_city   |CharField      |max_length=40, null=False, blank=False                                                |
    |street_address1|street_address1|CharField      |max_length=80, null=False, blank=False                                                |
    |street_address2|street_address2|CharField      |max_length=80, null=True, blank=True                                                  |
    |county         |county         |CharField      |max_length=80, null=True, blank=True                                                  |
    |date           |date           |DateTimeField  |auto_now_add=True                                                                     |
    |delivery_cost  |delivery_cost  |DecimalField   |max_digits=6, decimal_places=2, null=False, default=0                                 |
    |order_total    |order_total    |DecimalField   |max_digits=10, decimal_places=2, null=False, default=0                                |
    |grand_total    |grand_total    |DecimalField   |max_digits=10, decimal_places=2, null=False, default=0                                |
    |original_bag   |original_cart  |TextField      |null=False, blank=False, default=''                                                   |
    |stripe_pid     |stripe_pid     |CharField      |max_length=254, null=False, blank=False, default=''                                   |

    <br>

    * OrderLineItem Model:

    |Name           |Database Key   |Field Type     |Validation                                                                          |
    |---------------|---------------|---------------|------------------------------------------------------------------------------------|
    |order          |order          |ForeignKey     |'Order', null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
    |product        |product        |ForeignKey     |'Product', null=False, blank=False, on_delete=models.CASCADE                        |
    |product_size   |product_size   |CharField      |max_length=2, null=True, blank=True                                                 |
    |quantity       |quantity       |IntegerField   |null=False, blank=False, default=0                                                  |
    |lineitem_total |lineitem_total |DecimalField   |max_digits=6, decimal_places=2, null=False, blank=False, editable=False             |

    
    <br>

* **DreamBuild** - Main app

* **Home App** - No classes or models needed as it is the index page

* **Products App** - Category and Product models

    * Category Model:  

    | Name          | Database Key  | Field Type    | Validation                            |
    | ------------- | ------------- | ------------- | ------------------------------------- |
    | name          | name          | CharField     | max_length=254                        |
    | friendly_name | friendly_name | CharField     | max_length=254, null=True, blank=True |

    <br>

    * Product Model:

    | Name        | Database Key  | Field Type        | Validation                                                   |
    | ----------- | ------------- | ----------------- | ------------------------------------------------------------ |
    | category    | category      | ForeignKey        | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
    | sku         | sku           | CharField         | max_length=254, null=True, blank=True                        |
    | name        | name          | CharField         | max_length=254                                               |
    | description | description   | TextField         |                                                              |
    | has_sizes   | has_sizes     | BooleanField      | default=False, null=True, blank=True                         |
    | price       | price         | DecimalField      | max_digits=6, decimal_places=2                               |
    | rating      | rating        | DecimalField      | max_digits=6, decimal_places=2, null=True, blank=True        |
    | image       | image         | ImageField        | null=True, blank=True                                        |

    <br>

* **Profiles App** - UserProfile model

    * UserProfile Model:  

| Name                   | Database Key            | Field Type        | Validation                                   |
| ---------------------- | ----------------------- | ----------------- | -------------------------------------------- |
| user                   | user                    | OneToOneField     | 'User', on_delete=models.CASCADE             |
| default_phone_number   | default_phone_number    | CharField         | max_length=20, null=True, blank=True         |
| default_street_address1| default_street_address1 | CharField         | max_length=80, null=True, blank=True         |
| default_street_address2| default_street_address2 | CharField         | max_length=80, null=True, blank=True         |
| default_town_or_city   | default_town_or_city    | CharField         | max_length=40, null=True, blank=True         |
| default_county         | default_county          | CharField         | max_length=80, null=True, blank=True         |
| default_postcode       | default_postcode        | CharField         | max_length=20, null=True, blank=True         |
| default_country        | default_country         | CountryField      | blank_label='Country', null=True, blank=True |

[Back to top &uarr;](#dreambuild-fitness)

---

# Features

## Main Header

* Featured at the top of the page and consistent throughout the website. Stays in place as scrolling.
* Features the brand name located to the top left, which is clickable and returns the site user to the home page.

    ![Screenshot of main header logo](./readme_assets/img/header-logo.jpg) <br>
    *Screenshot of main header logo*

* A functional searchbar is located centrally (will chat about functionality in the [Products Section](#products)) 

    ![Screenshot of searchbar](./readme_assets/img/searchbar.jpg) <br>
    *Screenshot of searchbar*

* Located in the top right is a 'My Account' icon which is a dropdown menu along with a Bag icon that shows the site user's current bag total (will chat about both functionality in the [Account Section](#account) and [Bag Section](#bag) respectively)

    ![Screenshot of account and bag icons](./readme_assets/img/account-bag-icons.jpg) <br>
    *Screenshot of account and bag icons*

* On smaller screens the logo disappears (being replaced with the navbar functionality) and the search bar turns into a dropdown function. 

    ![Screenshot of mobile view of the header](./readme_assets/img/header-mobile-view.jpg) <br>
    *Screenshot of mobile view of the header*

* Just below the navbar there is a ticker stating the free delivery threshold.

<br>

## Navigation

* Featured at the top of the page and consistent throughout the website. Stays in place as scrolling.

    ![Screenshot of navigation bar on desktop](./readme_assets/img/navbar-desktop.jpg) <br>
    *Screenshot of navigation bar on desktop*

* Where neccessary, a dropdown menu is available to further specify a search. 

    ![Screenshot of navigation bar dropdown on desktop](./readme_assets/img/navbar-desktop-dropdown.jpg) <br>
    *Screenshot of navigation bar dropdown on desktop*

* On smaller screens the navigation menu is hidden away, revealed when clicked the icon in the top left. Likewise the dropdown is available where neccessary.

    ![Screenshot of navigation bar on mobile](./readme_assets/img/navbar-mobile.jpg) <br>
    *Screenshot of navigation bar on mobile*

    ![Screenshot of navigation bar dropdown on mobile](./readme_assets/img/navbar-mobile-dropdown.jpg) <br>
    *Screenshot of navigation bar dropdown on mobile*

<br>

## Hero Section 


* The Hero section contains one main Hero image, along with a Shop Now button to direct site users to the 'All Products' section and an inspirational message to site users on arrival.

    ![Screenshot of hero section](./readme_assets/img/hero-section.jpg) <br>
    *Screenshot of hero section*

* When the site user hovers over the Shop Now button, it changes to a shade of grey mentioned above. 

    ![Screenshot of hero section button](./readme_assets/img/hero-section-button.jpg) <br>
    *Screenshot of hero section button*

<br>

## Footer

* Located at the bottom of the majority of pages throughout the website. 
* The footer is broke up into 4 sections, 3 across the top and the one section just below, following by a copyright tag. This then collapses, to being on top of one another on a mobile view. 
* First section contains the brand name along with a mission statement. 

    ![Screenshot of footer mission statement](./readme_assets/img/footer-mission-statement.jpg) <br>
    *Screenshot of footer mission statement*

* Second section is a selection of quick links for the site user to choose from to direct them to relative pages.

    ![Screenshot of footer quick links](./readme_assets/img/footer-quick-links.jpg) <br>
    *Screenshot of footer quick links*

* Third section contains the company's social links, with a working (currently at the time of this write up) [Facebook page](https://www.facebook.com/profile.php?id=61552476312298). The icons reverse in colour when hovered over. 

    ![Screenshot of footer social links](./readme_assets/img/footer-social-links.jpg) <br>
    *Screenshot of footer social links*

    ![Screenshot of footer social link swhen hovered](./readme_assets/img/footer-social-links-hover.jpg) <br>
    *Screenshot of footer social links when hovered*


* Fourth section contains newsletter subscription service, powered by [Mailchimp](https://mailchimp.com/), where the site user enters their email details to sign up for the company's newsletter

    ![Screenshot of footer newsletter](./readme_assets/img/footer-newsletter.jpg) <br>
    *Screenshot of footer newsletter section*

<br>

## About Us


[Back to top &uarr;](#dreambuild-fitness)

---