# **Python Yelp Api**
We are going to create a new project let's name it pyyelp. This project sends http request to Yelp api to get list of business. The full process of the project will be documented here breaking down step by step:

## 1. Create a new project:
                        a. Open the terminal
                        b. And create a root diectory: Terminal command: mkdir pyyelp
                        c. Open the directory in VScode: Terminal command: code .
                        d. Make a source directory under root directory: name it for example, src
                        e. Then create a py file inside src directory named e.g app.py

## 2. Virtual environment & Install packages:
                        a. Open terminal in vscode
                        b. Install request package: Terminal command: pipenv install requests
                           This will create a virtual environment as well as install the package.
                           And the Pipfile and lock file are created.  
                        c. Then change the virtual environment for the pyyelp project in vscode.
                        d. At this point if vscode suggets to install linter pylint then go ahead and install it
                        
## 3. Start coding:
                        a. Go to app.py file
                        b. Import request package
                        c. Then use get method to get data. The code will be like:
```python
                            import requests

                            requests.get()
```
                        f. Here we need to pass a str "url" the url is the address of the endpoint. To get this visit
                           yelp site on fusion api doc page: https://docs.developer.yelp.com/docs/fusion-intro
                           here you find business search endpoint: https://api.yelp.com/v3/businesses/search
                           just copy this address and pass as parameter in get method. So the code comes like,
```python
                           import requests

                           requests.get("https://api.yelp.com/v3/businesses/search")
```

                        g. This get method returns a response object. We created a variable called response. So the
                           code is now: 
```python
                           response = requests.get("https://api.yelp.com/v3/businesses/search")
```
                        h. At this point, vscode may suggest to install code formatter for this virtual environment
                           so let's install it.
                        i. Now pirnt the response. The code now looks like:
```python
                            import requests

                            response = requests.get("https://api.yelp.com/v3/businesses/search")

                            print(response)
```

## 4. Run the code and get output:
                        a. Now save the changes and run the code.
                        b. OutPut: <Response [401]>

## 5. Authentication:
                        a. The 401 is the status of one of the standard http error codes.
                        b. If you search the 401 in google you see this error indicates unauthorized request. In
                           this case, we got this error because we did not tell yelp who we are. So every time we want to call any of the endpoints of Yelp we need to send the key to tell Yelp who we are. This is we call authentication. 
                        c. Now back to the Yelp developer portal: https://docs.developer.yelp.com/
                           And get started the dcumentation: https://docs.developer.yelp.com/docs
                           Then go to fusion authentication in left menu: https://docs.developer.yelp.com/docs/fusion-authentication
                        d. This page is telling us that first we need to create app to get the api key. We already
                           did this(See yelpapi file). 
                        e. Next is Authenticate api call with api key. To authenticate the api call with
                           api key, set the Authorization HTTP header value as Bearer api_key. Which means, these 
                           http requests have two sections, or two components. Header section and Payload section.
                           In the header section we have few headers that specify a few metadata about this request. These headers are key: value pairs. One of this headers is authorization header which is define in the http protocol, we this header to tell the web server who we are. Let's take a look how to do that in code:

## 6. Refactor the code:
                        a. To make the code little cleaner, put the endpoint url in a separate varibale. And the code looks like:
```python
                           import requests

                           url = "https://api.yelp.com/v3/businesses/search"
                           response = requests.get(url)
                           print(response)
```
                        b. Now the get method optionally takes keyword arguments, one of them is headers(we can
                           read more on this on the requests package documentation: https://pypi.org/project/requests/). We can set the headers as dictionary of key:value pairs; headers={}
                           and the code looks like:
```python
                                                response = requests.get(url, headers={key: value})
```
                        c. For clearity, create the dictionary and keep in a separate variable called headers. 
                           The dictionary syntax: 
 ```python
                                                variable = {"key": "value " + api_key}
 ```

                           Note: We can find the api key on Yelp manage app page. And for clearity, keep the api_key in a separate varibale called api_key.

                           So the codes looks now:
```python
                           import requests

                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           response = requests.get(url, headers=headers)
                           print(response)
```
## 7. Run the code and get output:
                        a. Now save the change and run the codes once again
                        b. This time we get output: <Response 400>
                        c. This is a different status code 400 which means a bad request. 
                        d. Bad request indicates that the server expects some data that we did not supply.
                        e. How do we know what the server expected? Well, this response object has an attribute
                           called text. With that we can see the details of what the server sent us. So if we 
                           print(response.text) then in the terminal it returns the detail as below:
                           {"error": {"code": "VALIDATION_ERROR", "description": "Please specify a location or 
                           a latitude and longitude"}}

                           This output is a josn object with the property called error. which is set to another json object. 
                        f. Now refactor the codes once again with the help of Yelp documentation.

## 8. Refactor codes once again:
                        a. Go to Yelp documentation: https://docs.developer.yelp.com/reference/v3_business_search
                        b. Here we can see the parameters that are must required to set in the request. 
                           For example, location parameter.
                        c. Now take a look in the code how to set parameter to send http request. The get method
                           optionally takes another keyword: arguments, params= just like we set headers dictionary.

                           So the params dictionary syntax:
                                                      variable = {"key": "geo_location"}
                           The code looks like now:
```python
                           import requests

                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           params = {
                            "location": "NYC"
                           }
                           response = requests.get(url, headers=headers, params=params)
                           print(response.text)
```
## 9. Run the codes and get output:
                        a. Now save the changes and run the program
                        b. This time we did not get error instead we get the json object that includes a list of
                           businesses in New York city. 
                        c. Now we can fiter this.

## 10. Refactor codes filtering the results:
                        a. In the params dictionary we set another key: value pairs like "term": "Barber"
```python
                           params = {
                            "term": "Barber",
                            "Location": "NYC"
                           }
```
                        b. This will return only the barbers in New York city in the terminal.
                        c. And if you scroll at the top you see in this json object has property called businesses
                           and this is set to a list/array because we have a square bracket. In this array, we have bunch of json objects because we have curly brackets. 
                        d. Now back to the code on response object now instead text attribute we are going to call
                           json method and this will convert the result in a dictionary. And we can store the result in a variable called result.
                           So the codes look like;
```python
                           import requests

                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           params = {
                            "Location": "NYC"
                           }
                           response = requests.get(url, headers=headers, params=params)
                           result = response.json()
                           print(result)
```
                        e. Another thing as we see the dictionary returns in the terminal has key called businesses 
                           and it set to a list so we can immediately access this key and code looks like:
                           result = response.json()["businesses"] and let's change the result variable to businesses. Now we have a list of dictionaries. The codes looks like this;
```python
                           import requests

                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           params = {
                            "Location": "NYC"
                           }
                           response = requests.get(url, headers=headers, params=params)
                           businesses = response.json()["businesses"]
                           print(businesses)
```
## 11. Run the codes and get output:
                        a. Run the program and it rutunrs a list of dictionaries with key: value
                        b. The key like: id, alias, name etc

## 12. Refactor codes with more filter:
                        a. Now let's say we want to get only the name of the businesses
                        b. Then just iterate over the list. We will get the each dictionary and 
                           extract the value of the name key.
                        c. So the iteration will be:
```python
                           for business in businesses:
                                print(business["name"])
```
                        d. The code looks like now:
```python                          
                           import requests

                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           params = {
                            "Location": "NYC"
                           }
                           response = requests.get(url, headers=headers, params=params)
                           businesses = response.json()["businesses"]

                           for business in businesses:
                               print(business["name"])
```
## 13. Run the codes and get output:
                        a. Run the program and it rutunrs only the name of business
                        b. Now we can take this to the next level like, we can use list comprehension to get the
                           name of busenesses with rating of 4.5 or above.

## 14. Refactor codes use list comprehention:
                        a. list comprehention syntax: [item for item in list]
                           Here, 
                           the list is, businesses
                           the item is, business (Which is a  dictionary object)
                           now to get the name of the business we need business["name"]
                           So the list comprehention looks like;
                           [business["name"] for business in businesses]
                        b. Now we want to filter then name with rating more or equal 4.5 so we will do;
                           if business["rating"] which is another property of the list > 4.5 that added in the list and return. And store the list comprehention in a variable let's say names. So the codes finally looks like:
```python
                           import requests
           
                           url = https://api.yelp.com/v3/businesses/search 
                           api_key = "pjOSpM8jM5cnjryyOYWyROmoJgz_REijnieChEIJopCw-KTGWRM7nWof-tTXauSDNt-BDsPiA6uQ1jnUCemauAGqG0bpzy7RgTWMZWJ1KkFIi3_UTq2LERHBIRHBFIddfZXYx"
                           headers = {
                            "Authorization": "Bearer " + api_key
                           }
                           params = {
                            "Location": "NYC"
                           }
                           response = requests.get(url, headers=headers, params=params)
                           businesses = response.json()["businesses"]
                           
                           names = [business["name"] for business in businesses if business["rating"] > 4.5]
                           print(names)
```
## 15. Run the codes and get output:
                        a. Run the program and it rutunrs a list of the names of the barbers in New York city with
                           the rating 4.5 or more.

## 16. Secure the api key:
                     a. We must not hard code the api_key or password in the source code. So we need to hide
                        this information. 
                     b. There are few ways to do this. here we are going to highlight couple of them. One way is
                        environment variables in python. Another is manage a confiq file for the key and exclude it 
                        from the source code.
                        1. Environment variables: In python, environment variables are global variables that are accessible 
                           to a running Python script or application. These variables are set outside of the Python script, typically at the system level, and can be accessed by Python code to retrieve information or configure the behavior of the script. Environment variables are useful for storing configuration settings, sensitive information, or any data that needs to be shared across different parts of an application. By setting these environment variables outside of the script, you can easily change the configuration without modifying the code.
                           The steps of implementation are;

                              i. Add the secret info like pass/key into the bash profile:
                                      a. Open the terminal and go to users/home directory
                                      b. Then open the .bash_profile file: nano .bash_profile
                                      c. Export the api key: export variable_name="actual_api_key"
                                      d. Save the file: shortkey control+o
                                      e. Exit: shortkey control+x
                                      f. Then need to source: source .bash_profile

                              ii. Accessing Environment Variables in Python: In Python, you can access environment
                                 variables using the os module. 
                                      a. Go to py file where you want to implement.(restart vs code may needed)
                                      b. import os
                                      c. os has a method .environ.get() it take str: os.environ.get("variable_name")
                                      d. So en example:
```python
                                                api_key = os.environ.get("yelp_api_key")
                                                headers = {
                                                  "authorization": "Bearer " + api_key
                                                }
```
                                      e. Run the program now and it should work.

                        2. Hiding keys in a configuration file: Here we will create a configuration file named config.py in 
                           the source directory and keep the key here in the file then import the config module in the required py file and then the config module has attribute like key so we can access it using dot 
                           oparator. Then we will create gitignore file add the confiq file in the gitignore then we can push our code and the key is secured now. The detail step by step are as below:

                              i. Create config file:
                                       a. Create config.py file under source directory in VScode
                                       b. Store the api key here in a varibale called yelp_api_key
                              ii. Import module:
                                       a. Go to the py file where we need the api key
                                       b. At the top import config
                                       c. then inside the code where we need to access the key from config file access the
                                          yelp_api_key attribute on config.py file using .(dot) oparator. e.g config.api_key
                                       d. Save the changes.
                              iii. Gitignore:
                                       a. Create gitignore file under the source code
                                       b. Then open the gitignore file
                                       c. Just add the config file here
                                       d. Then all done and ready to share the codes
