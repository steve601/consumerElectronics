# ONLINE CUSTOMER ELECTRONIC SALES ANALYSIS
->The purpose of this project is to predict whether a customer will intend to purchase a product online or not based on some features

## Prerequisites
 *Python 3.x*
 *Pip (Python package installer)*
 *AWS CLI*
 *AWS Elastic Beanstalk CLI*

### Table of Contents
*1.Project Overview*
*2.Features*
*3.Installation*
*4.Usage*
*5.Deploymnet to AWS*
*6.Contributing*



## Project Overview
The application provides a comprehensive view into the dynamics of online customer-product interactions. It captures essential variables that influence the likelihood of a customer purchasing the product or not.
## Installation
->To run this project locally, you need to have Python and the necessary libraries installed.
**1.Clone the repo.;**
        git clone https://github.com/steve601/consumerElectronics.git
        cd consumerElectronics
**2.Create a virtual environment and activate it:**
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
**3.Install the required packages:**
        pip install -r requirements.txt

## Usage
=>Load the Model,then run the incomeapp.py file on localhost then perform your prediction

## Deployment to AWS Elastic Beanstalk
**1.Initialize Elastic Beanstalk:**
      eb init
  Follow the prompts to configure your application. Choose the appropriate region and platform (Python).
**2.Create an Elastic Beanstalk environment:**
      eb create flask-env
**3.Deploy the application:**
      eb deploy
**4.Access the application:** After deployment, access your application using the URL provided by Elastic Beanstalk.

## Configuration File: .ebextensions/python.config
=>Ensure your configuration file is set up correctly:
       option_settings:
         aws:elasticbeanstalk:container:python:
           WSGIPath: consumer:app
## Contributing
Contributions are welcome!

