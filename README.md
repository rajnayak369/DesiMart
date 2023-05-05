# DesiMart

## What is the application about?
DesiMart is ecommerce website which sells Indian grocery which allows customers to purchase a wide variety of food items from the comfort of their homes. It is a one stop destination to find everything Indian. This application has a very user-friendly interface that makes it easy for customers to browse through different categories of products, add items to their shopping cart, and complete their purchase with a few clicks. The website offers a range of products, including spices, grains, lentils, snacks, sweets, and beverages that are commonly used in Indian cooking. It provides a convenient and accessible way for customers to purchase high-quality products which are essential to Indian cooking and dietary habits.

## Features

DesiMart offers following features:
*   Login, Register and continue as guest options for a user
*   Product filter feature of various categories 
*	Product view page with details of the product
*	Similar product recommendations feature for the user
*	Admin features like dashboard viewing, access to all user orders and reports.
*	Search feature to browse product by a keyword.
*	Add to cart and check out feature for a customer to place an order
*	User can login and view orders.

## Requirements

All the packages and libraries required for this application to run can be found in requirements.txt file.

## Installation

To install the application, you need to clone/download the application  

```bash
git clone "repo_link"
```
Run the below command to install pyenv

```bash
pyenv update
pyenv install 3.10.7 # to install the pyenv on your server.
```

You need to create a virtual environment. Set present location in termial to root directory of the project and then run the following commands to create and start the virtunal environment.  
```bash
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```

To install the dependencies run the following command.
```bash
pip install -r requirements.txt
```




## Deployment

To start the application run the following command from root directory.
```bash
 python3 manage.py runserver
```
To terminate the application use ctrl+c or follow the commands shown in terminal.



## Demo

The application is deployed and you can find it using the below link:
[Desi Mart](https://desi-mart.herokuapp.com/)

## Credits
The data source for this application was taken from https://www.kaggle.com/datasets/satyamsundaram/jiomart-products-dataset. 
This is a dataset containing products details from the e-commerce website Jiomart. The table contains product title, price, discount price, category and image link.
We used open source (chart.js) https://www.chartjs.org/ to implement chart view of the data.