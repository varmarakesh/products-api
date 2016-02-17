# products-api
Django restframework project that offers get and post api's for a basic data structure

##Install Instructions

1. Clone the project to your machine. Make sure git is installed first.
    *   git --version
    *   git clone https://github.com/varmarakesh/products-api.git
2. Verify python 2.7 in installed. Also verify pip is installed.
    *   python --version
    *   pip --version
    pip is the package manager for installing python packages. Next step uses pip to install the python packages needed to run this project.
3. Install the python packages (requests, django, djangorestframewort, pymongo and fabric) that are required to run this project. Running pip on requirements.txt will install the packages.
    *    cd products-api
    *    pip install -r requirements.txt
    Suggest to use a virtualenv
4. Run django
    *   python manage.py runserver
5. Run tests (test_product_creation will create a product by invoking the post api and ensure it is created by invoking the get api).
    *   fab run_tests
    
This has been tested so far on the mac osx.
