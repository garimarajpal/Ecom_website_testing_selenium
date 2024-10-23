# Ecom_website_testing_selenium
This guide explains how to conduct automated testing on a locally hosted eCommerce website using Python and Selenium. 
Selenium is a robust tool that enables programmatic control of web browsers, making it ideal for comprehensive testing of web applications.

# eCommerce Website and Testing

## Overview

This project is an eCommerce website developed using **WordPress**, **WooCommerce**, **MAMP**, and **MySQL Workbench**. It features essential functionalities such as product listings, user authentication, and a shopping cart. A key aspect of this project is the **automated testing** implemented using **Python** and **Selenium**, alongside **API testing** conducted with **Postman**, ensuring a reliable and seamless user experience.


## Key Features

- **User Registration & Authentication**: Secure sign-up and login processes.
- **Product Catalog**: Comprehensive listings with search and filter capabilities.
- **Shopping Cart**: Easy management of selected items before purchase.
- **Checkout Process**: Seamless transition from cart to order confirmation.
- **Admin Panel**: Intuitive interface for managing products and orders.
- **WooCommerce Integration**: Full-featured eCommerce platform for handling products, orders, and payments.
- **Automated Testing**: 
  - Developed using **Python** and **Selenium**.
  - Ensures functionality and performance are consistent and reliable across updates.
- **API Testing with Postman**: 
  - Comprehensive testing of backend APIs to validate endpoints, request/response formats, and authentication processes.

## Technologies Used

- **WordPress**: Content management system for building the site.
- **WooCommerce**: Plugin for eCommerce functionalities.
- **MAMP**: Local server environment for development (Mac, Apache, MySQL, PHP).
- **MySQL Workbench**: Database management and design tool.
- **Python**: Programming language used for automated testing.
- **Selenium**: Framework for automated testing of web applications.
- **Postman**: Tool for API testing and development.

## Screen recording of Website

https://github.com/user-attachments/assets/e0c3e7a5-e707-42c3-b7e4-41ee9b2cdbf6


## Installation Guide

### Step 1: Clone the Repository
To get a copy of the project, run the following command in your terminal:
```bash
git clone (https://github.com/garimarajpal/Ecom_website_testing_selenium)
```

### Step 2: Install MAMP
1. Download and install MAMP from [MAMP's official website](https://www.mamp.info/).
2. Launch MAMP and start the servers.

### Step 3: Import the Database
1. Open MySQL Workbench and connect to your MAMP server.
2. Import the SQL file located in the project directory to set up the database.

### Step 4: Configure WordPress
1. Move the project files into the MAMP `htdocs` directory.
2. Open a web browser and navigate to `http://localhost:10004/` to complete the WordPress setup.

### Step 5: Install WooCommerce
1. Once in the WordPress dashboard, navigate to **Plugins > Add New**.
2. Search for "WooCommerce" and install the plugin.
3. Follow the setup wizard to configure your store.

### Step 6: Run Automated Tests with Selenium
1. Ensure you have Python and Selenium installed.
2. Execute the provided test scripts to validate the website's functionality and performance.

### Step 7: API Testing with Postman
1. Open Postman and import the API collection provided in the project.
2. Run the tests to verify the functionality of various endpoints.

Screenshot of a Postman Request
![postman_get_request](https://github.com/user-attachments/assets/a6dab53c-a064-455e-ae53-3bc040f19fc7)

## Contributing

Contributions are welcome! If you'd like to enhance the project, please fork the repository and submit a pull request.

## Acknowledgments

- [WordPress](https://wordpress.org/)
- [WooCommerce](https://woocommerce.com/)
- [MAMP](https://www.mamp.info/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [Selenium](https://www.selenium.dev/)
- [Postman](https://www.postman.com/)
