# Con Fusion
It is a capstone project for [Full Stack Web Developer Udacity Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044). This app is inspired form [NodeJS Coursera Course](https://www.coursera.org/learn/server-side-nodejs)
. Con Fusion is a restaurant and we want to implement its api from scratch. There are users which visit the restaurant, a chef and the director of the restaurant.

### Getting Started

#### Run app locally
- make sure you setup your `database_url` correctly in `./setup.sh`
- make sure also you setup not expired tokens in `./setup.sh`
- install all packages needed to run the app `pip3 install -r requirements.txt`
- then you can run the following commands (from the root directory)
```
source ./setup.sh
export FLASK_APP=app.py 
export FLASK_ENV=development
flask run
```
The default url: `http://localhost:5000`

#### Use the live app
- make sure you setup not expired tokens in `./setup.sh`
- then you can run the following commands (from the root directory)
```
source ./setup.sh
```

The default url: `https://confusion20.herokuapp.com/`

#### Tests
- make sure you setup not expired tokens in `./setup.sh`
- make sure also you setup your `database url` for testing correctly in `./test_app.py`
- then you can run the following commands (from the root directory)
```
source ./setup.sh
psql confusion_test < ./sql/test_loading_data.sql # Be sure confusion_test db already exist
python3 test_app.py
```

### API Reference
#### Getting Started
Base URL: you can run locally `http://localhost:5000` or live api `https://confusion20.herokuapp.com/`
##### Authentication
 - Anyone can make GET request for any endpoint (No authentication needed), otherwise a certain authentication needed
 - There are 3 roles in this api:
   - User: has a permission to create a comment for a certain dish.
   - Chef: has the permissions of the User in addition to creating, deleting , modifying the price of any dish.
   - Director: has the permissions of the Chef in addition to creating, deleteing any promotion.
 - you can use auth0 env variables in `./setup.sh` and [auth0 docs link](https://auth0.com/docs/api/authentication?http#login) to get a new token
#### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": false,
  "error": 404,
  "message": "Resource Not Found"
}
```
types of errors:
- 404: Resource Not Found
- 400: Bad Request
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error
- 401: Unauthorized
- 403: Forbidden

### Endpoints
**Before running any authorized endpoint, please make sure you setup NOT expired tokens in `./setup.sh`**<br>
**then running the command `source ./setup.sh`**
#### GET /dishes
- ##### General:
  - Return a list of dishes and a success value.
- `curl -X GET 'https://confusion20.herokuapp.com/dishes'`
```
{
  "dishes": [
    {
      "category": "mains",
      "description": "A unique combination of Indian Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer.",
      "featured": true,
      "id": 1,
      "image": "images/uthappizza.png",
      "label": "Hot",
      "name": "Uthappizza",
      "price": 4.99
    },
    {
      "category": "appetizer",
      "description": "Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce",
      "featured": false,
      "id": 2,
      "image": "images/zucchipakoda.png",
      "label": "",
      "name": "Zucchipakoda",
      "price": 1.99
    },
    {
      "category": "appetizer",
      "description": "A quintessential ConFusion experience, is it a vada or is it a donut?",
      "featured": false,
      "id": 3,
      "image": "images/vadonut.png",
      "label": "New",
      "name": "Vadonut",
      "price": 1.99
    },
    {
      "category": "dessert",
      "description": "A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms",
      "featured": false,
      "id": 4,
      "image": "images/elaicheesecake.png",
      "label": "",
      "name": "ElaiCheese Cake",
      "price": 2.99
    }
  ],
  "success": true
}
```
#### POST /dishes
- ##### General:
  - Return a created id, a list of dishes and a success value.
- `curl -X POST -H "content-type: application/json" -H "Authorization: Bearer $TOKEN_CHEF" -d '{"name": "tname", "image": "timage", "category": "tcategory", "price": 1.23}' 'https://confusion20.herokuapp.com/dishes'`
```
{
  "created": 5,
  "dishes": [
    {
      "category": "mains",
      "description": "A unique combination of Indian Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer.",
      "featured": true,
      "id": 1,
      "image": "images/uthappizza.png",
      "label": "Hot",
      "name": "Uthappizza",
      "price": 4.99
    },
    {
      "category": "appetizer",
      "description": "Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce",
      "featured": false,
      "id": 2,
      "image": "images/zucchipakoda.png",
      "label": "",
      "name": "Zucchipakoda",
      "price": 1.99
    },
    {
      "category": "appetizer",
      "description": "A quintessential ConFusion experience, is it a vada or is it a donut?",
      "featured": false,
      "id": 3,
      "image": "images/vadonut.png",
      "label": "New",
      "name": "Vadonut",
      "price": 1.99
    },
    {
      "category": "dessert",
      "description": "A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms",
      "featured": false,
      "id": 4,
      "image": "images/elaicheesecake.png",
      "label": "",
      "name": "ElaiCheese Cake",
      "price": 2.99
    },
    {
      "category": "tcategory",
      "description": null,
      "featured": null,
      "id": 5,
      "image": "timage",
      "label": null,
      "name": "tname",
      "price": 1.23
    }
  ],
  "success": true
}
```
#### DELETE /dishes/{id}
- ##### General:
  - Return a deleted id, a list of dishes and a success value.
- `curl -X DELETE -H "Authorization: Bearer $TOKEN_CHEF" 'https://confusion20.herokuapp.com/dishes/1'`
```
{
  "deleted": 1,
  "dishes": [
    {
      "category": "appetizer",
      "description": "Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce",
      "featured": false,
      "id": 2,
      "image": "images/zucchipakoda.png",
      "label": "",
      "name": "Zucchipakoda",
      "price": 1.99
    },
    {
      "category": "appetizer",
      "description": "A quintessential ConFusion experience, is it a vada or is it a donut?",
      "featured": false,
      "id": 3,
      "image": "images/vadonut.png",
      "label": "New",
      "name": "Vadonut",
      "price": 1.99
    },
    {
      "category": "dessert",
      "description": "A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms",
      "featured": false,
      "id": 4,
      "image": "images/elaicheesecake.png",
      "label": "",
      "name": "ElaiCheese Cake",
      "price": 2.99
    },
    {
      "category": "tcategory",
      "description": null,
      "featured": null,
      "id": 5,
      "image": "timage",
      "label": null,
      "name": "tname",
      "price": 1.23
    }
  ],
  "success": true
}
```
#### PATCH /dishes/{id}
- ##### General:
  - Return a modified dish and a success value.
- `curl -X PATCH -H "content-type: application/json" -H "Authorization: Bearer $TOKEN_CHEF" -d '{"price": 5.67}' 'https://confusion20.herokuapp.com/dishes/3'`
```
{
  "dish": {
    "category": "appetizer",
    "description": "A quintessential ConFusion experience, is it a vada or is it a donut?",
    "featured": false,
    "id": 3,
    "image": "images/vadonut.png",
    "label": "New",
    "name": "Vadonut",
    "price": 5.67
  },
  "success": true
}
```
#### GET /dishes/{dishid}/comments
- ##### General:
  - Return a list of comments for a certain dish and a success value.
- `curl -X GET 'https://confusion20.herokuapp.com/dishes/2/comments'`
```
{
  "comments": [
    {
      "author": "John Lemon",
      "comment": "Imagine all the eatables, living in conFusion!",
      "date": "Tue, 16 Oct 2012 17:57:28 GMT",
      "dishid": 2,
      "id": 6,
      "rating": 5
    },
    {
      "author": "Paul McVites",
      "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
      "date": "Fri, 05 Sep 2014 17:57:28 GMT",
      "dishid": 2,
      "id": 7,
      "rating": 4
    },
    {
      "author": "Michael Jaikishan",
      "comment": "Eat it, just eat it!",
      "date": "Fri, 13 Feb 2015 17:57:28 GMT",
      "dishid": 2,
      "id": 8,
      "rating": 3
    },
    {
      "author": "Ringo Starry",
      "comment": "Ultimate, Reaching for the stars!",
      "date": "Mon, 02 Dec 2013 17:57:28 GMT",
      "dishid": 2,
      "id": 9,
      "rating": 4
    },
    {
      "author": "25 Cent",
      "comment": "It is your birthday, we are gonna party!",
      "date": "Fri, 02 Dec 2011 17:57:28 GMT",
      "dishid": 2,
      "id": 10,
      "rating": 2
    }
  ],
  "success": true
}
```
#### POST /comments
- ##### General:
  - Return created id, a list of comments and a success value.
- `curl -X POST -H "content-type: application/json" -H "Authorization: Bearer $TOKEN_USER" -d '{"dishid": 3, "rating": 5, "author": "tauthor", "date": "2020-01-02T17:57:28.556094", "comment": "tcomment"}' 'https://confusion20.herokuapp.com/comments'`
```
{
  "comments": [
    {
      "author": "John Lemon",
      "comment": "Imagine all the eatables, living in conFusion!",
      "date": "Tue, 16 Oct 2012 17:57:28 GMT",
      "dishid": 2,
      "id": 6,
      "rating": 5
    },
    {
      "author": "Paul McVites",
      "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
      "date": "Fri, 05 Sep 2014 17:57:28 GMT",
      "dishid": 2,
      "id": 7,
      "rating": 4
    },
    {
      "author": "Michael Jaikishan",
      "comment": "Eat it, just eat it!",
      "date": "Fri, 13 Feb 2015 17:57:28 GMT",
      "dishid": 2,
      "id": 8,
      "rating": 3
    },
    {
      "author": "Ringo Starry",
      "comment": "Ultimate, Reaching for the stars!",
      "date": "Mon, 02 Dec 2013 17:57:28 GMT",
      "dishid": 2,
      "id": 9,
      "rating": 4
    },
    {
      "author": "25 Cent",
      "comment": "It is your birthday, we are gonna party!",
      "date": "Fri, 02 Dec 2011 17:57:28 GMT",
      "dishid": 2,
      "id": 10,
      "rating": 2
    },
    {
      "author": "John Lemon",
      "comment": "Imagine all the eatables, living in conFusion!",
      "date": "Tue, 16 Oct 2012 17:57:28 GMT",
      "dishid": 3,
      "id": 11,
      "rating": 5
    },
    {
      "author": "Paul McVites",
      "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
      "date": "Fri, 05 Sep 2014 17:57:28 GMT",
      "dishid": 3,
      "id": 12,
      "rating": 4
    },
    {
      "author": "Michael Jaikishan",
      "comment": "Eat it, just eat it!",
      "date": "Fri, 13 Feb 2015 17:57:28 GMT",
      "dishid": 3,
      "id": 13,
      "rating": 3
    },
    {
      "author": "Ringo Starry",
      "comment": "Ultimate, Reaching for the stars!",
      "date": "Mon, 02 Dec 2013 17:57:28 GMT",
      "dishid": 3,
      "id": 14,
      "rating": 4
    },
    {
      "author": "25 Cent",
      "comment": "It is your birthday, we are gonna party!",
      "date": "Fri, 02 Dec 2011 17:57:28 GMT",
      "dishid": 3,
      "id": 15,
      "rating": 2
    },
    {
      "author": "John Lemon",
      "comment": "Imagine all the eatables, living in conFusion!",
      "date": "Tue, 16 Oct 2012 17:57:28 GMT",
      "dishid": 4,
      "id": 16,
      "rating": 5
    },
    {
      "author": "Paul McVites",
      "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
      "date": "Fri, 05 Sep 2014 17:57:28 GMT",
      "dishid": 4,
      "id": 17,
      "rating": 4
    },
    {
      "author": "Michael Jaikishan",
      "comment": "Eat it, just eat it!",
      "date": "Fri, 13 Feb 2015 17:57:28 GMT",
      "dishid": 4,
      "id": 18,
      "rating": 3
    },
    {
      "author": "Ringo Starry",
      "comment": "Ultimate, Reaching for the stars!",
      "date": "Mon, 02 Dec 2013 17:57:28 GMT",
      "dishid": 4,
      "id": 19,
      "rating": 4
    },
    {
      "author": "25 Cent",
      "comment": "It is your birthday, we are gonna party!",
      "date": "Fri, 02 Dec 2011 17:57:28 GMT",
      "dishid": 4,
      "id": 20,
      "rating": 2
    },
    {
      "author": "John Lemon",
      "comment": "Imagine all the eatables, living in conFusion!",
      "date": "Tue, 16 Oct 2012 17:57:28 GMT",
      "dishid": null,
      "id": 1,
      "rating": 5
    },
    {
      "author": "Paul McVites",
      "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
      "date": "Fri, 05 Sep 2014 17:57:28 GMT",
      "dishid": null,
      "id": 2,
      "rating": 4
    },
    {
      "author": "Michael Jaikishan",
      "comment": "Eat it, just eat it!",
      "date": "Fri, 13 Feb 2015 17:57:28 GMT",
      "dishid": null,
      "id": 3,
      "rating": 3
    },
    {
      "author": "Ringo Starry",
      "comment": "Ultimate, Reaching for the stars!",
      "date": "Mon, 02 Dec 2013 17:57:28 GMT",
      "dishid": null,
      "id": 4,
      "rating": 4
    },
    {
      "author": "25 Cent",
      "comment": "It is your birthday, we are gonna party!",
      "date": "Fri, 02 Dec 2011 17:57:28 GMT",
      "dishid": null,
      "id": 5,
      "rating": 2
    },
    {
      "author": "tauthor",
      "comment": "tcomment",
      "date": "Thu, 02 Jan 2020 17:57:28 GMT",
      "dishid": 3,
      "id": 21,
      "rating": 5
    }
  ],
  "created": 21,
  "success": true
}
```
#### GET /promotions
- ##### General:
  - Return a list of promotions and a success value.
- `curl -X GET 'https://confusion20.herokuapp.com/promotions'`
```
{
  "promotions": [
    {
      "description": "Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person ",
      "featured": true,
      "id": 1,
      "image": "images/buffet.png",
      "label": "New",
      "name": "Weekend Grand Buffet",
      "price": 19.99
    }
  ],
  "success": true
}
```
#### POST /promotions
- ##### General:
  - Return a created id, a list of promotions and a success value.
- `curl -X POST -H "content-type: application/json" -H "Authorization: Bearer $TOKEN_DIRECTOR" -d '{"name": "tname", "image": "timage", "price": 5.67, "description": "tdesc"}' 'https://confusion20.herokuapp.com/promotions'`
```
{
  "created": 2,
  "promotions": [
    {
      "description": "Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person ",
      "featured": true,
      "id": 1,
      "image": "images/buffet.png",
      "label": "New",
      "name": "Weekend Grand Buffet",
      "price": 19.99
    },
    {
      "description": "tdesc",
      "featured": null,
      "id": 2,
      "image": "timage",
      "label": null,
      "name": "tname",
      "price": 5.67
    }
  ],
  "success": true
}
```
#### DELETE /promotions/{id}
- ##### General:
  - Return a deleted id, a list of promotions and a success value.
- `curl -X DELETE -H "Authorization: Bearer $TOKEN_DIRECTOR" 'https://confusion20.herokuapp.com/promotions/1'`
```
{
  "deleted": 1,
  "promotions": [
    {
      "description": "tdesc",
      "featured": null,
      "id": 2,
      "image": "timage",
      "label": null,
      "name": "tname",
      "price": 5.67
    }
  ],
  "success": true
}
```
