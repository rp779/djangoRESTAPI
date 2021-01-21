
---------------------------------------------------------------------------------------------------------------------------------------------
# This project uses the Django REST Framework to build an API for consumption. 

### Here is a quick introduction to Django REST Framework and how to make data from your Django models consumable.

With the Django REST Framework (DRF), there are only few additional steps on top of creating a traditional Django App.

- define a serializer.
  - A serializer takes data from a database model, or table, and converts it into a JSON format. 
  - To create a custom serializer, add a file to app level directory tree named `serializer.py` and import `serializers` from `rest_framework`. Next, import the model you would like to use as the API data source.
  - Subclass the `ModelSerializer` from `rest_framework.serializers` and add an inner class called `Meta`.
  - Inside the inner `Meta` class define the model you would like to use and the fields you want exposed. Note: it is wise to expose the `id` field for use in url routing. Django creates the `id` field automatically and sets it as the primary key. No need to create an id field manually in your models. 
- Now that the serializer is created, add some views in a views.py file in the App directory. 
    - Traditional django views are used to customize what 'regular' data is sent to the templates. Whereas, Django REST Framework views are used to customize what 'serialized data' is sent to the templates. Django REST Framework, like traditional django ships with generic views. So, I will be using these generic views. generics provide commonly needed behavior. In most cases I will only need to subclass a generic view rather than create my own views.
   - Here I am using two views. One view to display all entries in the model (`ListTodo`) subclassed from `generics.ListAPIView`. The other view is used to display a single entry (`DetailView`) subclassed from generics.RetrieveAPIview. I have two routes in `urls.py` defined for these views. The DetailTodo view can be accessed with an additional parameter in the url, the primary key of the entry. In this case the `id` that django automatically created. 
   - Inside the views, override the default attributes of `queryset` and `serializer_class` with the queryset from the model being used and the serializer created earlier. 
   
With these steps taken, the API is fully functioning, go to '127.0.0.1:8000/api' to see the model data displayed in JSON format. The great thing about Django REST Framework is that is comes with a browseable API. No need to use cURL or Postman for now. Although later on as the API becomes more complex and more customization is needed, those tools can come in handy. 
 
In order for this API become consumble from another domain, we need to install `django-cores-headers`. This library automatically includes the correct headers in our HTTP responses based on project settings. 

Next update the `settings.py` file in three places:
- add `corsheaders` to the `INSTALLED_APPS`
- add `CorsMiddleware` above `CommonMiddleWare` in the `MIDDLEWARE` setting
- create a `CORS_ORIGIN_WHITELIST`

The `CORS_ORIGIN_WHITELIST` whitelists domains. In my case that setting looks like:

```CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",  # default for React
    "http://localhost:8000",  # default for Django
)
```
`http://localhost:3000` is the default domain for React. This way you can add a React front end. 
It is important to make sure that `CorsMiddleware` is in the correct place because Middleware settings are loaded from top to bottom.

---------------------------------------------------------------------------------------------------------------------------------------------------------
With that done, all that is left is to build out a simple React App and gather data from the django endoint.
- Assuming React is already installed, create a React app. Also, install axios. [Axios](https://github.com/axios/axios) will be used instead of FetchAPI.
- In the app.js folder delete every thing and import the modules needed:
  - `import React, { Component } from "react";
  - `import axios from 'axios';`
  
When using React to fetch API's, best practice is to make HTTP requests inside `componentDidMount`. So make a function to request the API using axios and call it from inside `componentDidMount`.

Lastly, render the component with data from the API, using `map()` to iterate over the list of items returned from the API and created HTML elements from them.





