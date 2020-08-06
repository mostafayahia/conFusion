#----------------------------------------------------------------
# using this code to convert dummy data to print sql statements
#----------------------------------------------------------------

data = {
    "dishes": [
        {
            "id": 0,
            "name": "Uthappizza",
            "image": "images/uthappizza.png",
            "category": "mains",
            "label": "Hot",
            "price": "4.99",
            "featured": True,
            "description": "A unique combination of Indian Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer."
        },
        {
            "id": 1,
            "name": "Zucchipakoda",
            "image": "images/zucchipakoda.png",
            "category": "appetizer",
            "label": "",
            "price": "1.99",
            "featured": False,
            "description": "Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce"
        },
        {
            "id": 2,
            "name": "Vadonut",
            "image": "images/vadonut.png",
            "category": "appetizer",
            "label": "New",
            "price": "1.99",
            "featured": False,
            "description": "A quintessential ConFusion experience, is it a vada or is it a donut?"
        },
        {
            "id": 3,
            "name": "ElaiCheese Cake",
            "image": "images/elaicheesecake.png",
            "category": "dessert",
            "label": "",
            "price": "2.99",
            "featured": False,
            "description": "A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms"
        }
    ],
    "comments": [
        {
            "id": 0,
            "dishId": 0,
            "rating": 5,
            "comment": "Imagine all the eatables, living in conFusion!",
            "author": "John Lemon",
            "date": "2012-10-16T17:57:28.556094Z"
        },
        {
            "id": 1,
            "dishId": 0,
            "rating": 4,
            "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
            "author": "Paul McVites",
            "date": "2014-09-05T17:57:28.556094Z"
        },
        {
            "id": 2,
            "dishId": 0,
            "rating": 3,
            "comment": "Eat it, just eat it!",
            "author": "Michael Jaikishan",
            "date": "2015-02-13T17:57:28.556094Z"
        },
        {
            "id": 3,
            "dishId": 0,
            "rating": 4,
            "comment": "Ultimate, Reaching for the stars!",
            "author": "Ringo Starry",
            "date": "2013-12-02T17:57:28.556094Z"
        },
        {
            "id": 4,
            "dishId": 0,
            "rating": 2,
            "comment": "It's your birthday, we're gonna party!",
            "author": "25 Cent",
            "date": "2011-12-02T17:57:28.556094Z"
        },
        {
            "id": 5,
            "dishId": 1,
            "rating": 5,
            "comment": "Imagine all the eatables, living in conFusion!",
            "author": "John Lemon",
            "date": "2012-10-16T17:57:28.556094Z"
        },
        {
            "id": 6,
            "dishId": 1,
            "rating": 4,
            "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
            "author": "Paul McVites",
            "date": "2014-09-05T17:57:28.556094Z"
        },
        {
            "id": 7,
            "dishId": 1,
            "rating": 3,
            "comment": "Eat it, just eat it!",
            "author": "Michael Jaikishan",
            "date": "2015-02-13T17:57:28.556094Z"
        },
        {
            "id": 8,
            "dishId": 1,
            "rating": 4,
            "comment": "Ultimate, Reaching for the stars!",
            "author": "Ringo Starry",
            "date": "2013-12-02T17:57:28.556094Z"
        },
        {
            "id": 9,
            "dishId": 1,
            "rating": 2,
            "comment": "It's your birthday, we're gonna party!",
            "author": "25 Cent",
            "date": "2011-12-02T17:57:28.556094Z"
        },
        {
            "id": 10,
            "dishId": 2,
            "rating": 5,
            "comment": "Imagine all the eatables, living in conFusion!",
            "author": "John Lemon",
            "date": "2012-10-16T17:57:28.556094Z"
        },
        {
            "id": 11,
            "dishId": 2,
            "rating": 4,
            "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
            "author": "Paul McVites",
            "date": "2014-09-05T17:57:28.556094Z"
        },
        {
            "id": 12,
            "dishId": 2,
            "rating": 3,
            "comment": "Eat it, just eat it!",
            "author": "Michael Jaikishan",
            "date": "2015-02-13T17:57:28.556094Z"
        },
        {
            "id": 13,
            "dishId": 2,
            "rating": 4,
            "comment": "Ultimate, Reaching for the stars!",
            "author": "Ringo Starry",
            "date": "2013-12-02T17:57:28.556094Z"
        },
        {
            "id": 14,
            "dishId": 2,
            "rating": 2,
            "comment": "It's your birthday, we're gonna party!",
            "author": "25 Cent",
            "date": "2011-12-02T17:57:28.556094Z"
        },
        {
            "id": 15,
            "dishId": 3,
            "rating": 5,
            "comment": "Imagine all the eatables, living in conFusion!",
            "author": "John Lemon",
            "date": "2012-10-16T17:57:28.556094Z"
        },
        {
            "id": 16,
            "dishId": 3,
            "rating": 4,
            "comment": "Sends anyone to heaven, I wish I could get my mother-in-law to eat it!",
            "author": "Paul McVites",
            "date": "2014-09-05T17:57:28.556094Z"
        },
        {
            "id": 17,
            "dishId": 3,
            "rating": 3,
            "comment": "Eat it, just eat it!",
            "author": "Michael Jaikishan",
            "date": "2015-02-13T17:57:28.556094Z"
        },
        {
            "id": 18,
            "dishId": 3,
            "rating": 4,
            "comment": "Ultimate, Reaching for the stars!",
            "author": "Ringo Starry",
            "date": "2013-12-02T17:57:28.556094Z"
        },
        {
            "id": 19,
            "dishId": 3,
            "rating": 2,
            "comment": "It's your birthday, we're gonna party!",
            "author": "25 Cent",
            "date": "2011-12-02T17:57:28.556094Z"
        },
        {
            "dishId": 0,
            "rating": "3",
            "author": "yahia",
            "comment": "this is a comment.",
            "date": "2020-02-04T11:08:19.834Z",
            "id": 20
        },
        {
            "dishId": 0,
            "rating": "4",
            "author": "yahia2",
            "comment": "this is a 2nd comment.",
            "date": "2020-02-04T11:13:20.786Z",
            "id": 21
        }
    ],
    "promotions": [
        {
            "id": 0,
            "name": "Weekend Grand Buffet",
            "image": "images/buffet.png",
            "label": "New",
            "price": "19.99",
            "featured": True,
            "description": "Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person "
        }
    ],
    "leaders": [
        {
            "id": 0,
            "name": "Peter Pan",
            "image": "images/alberto.png",
            "designation": "Chief Epicurious Officer",
            "abbr": "CEO",
            "featured": False,
            "description": "Our CEO, Peter, credits his hardworking East Asian immigrant parents who undertook the arduous journey to the shores of America with the intention of giving their children the best future. His mother's wizardy in the kitchen whipping up the tastiest dishes with whatever is available inexpensively at the supermarket, was his first inspiration to create the fusion cuisines for which The Frying Pan became well known. He brings his zeal for fusion cuisines to this restaurant, pioneering cross-cultural culinary connections."
        },
        {
            "id": 1,
            "name": "Dhanasekaran Witherspoon",
            "image": "images/alberto.png",
            "designation": "Chief Food Officer",
            "abbr": "CFO",
            "featured": False,
            "description": "Our CFO, Danny, as he is affectionately referred to by his colleagues, comes from a long established family tradition in farming and produce. His experiences growing up on a farm in the Australian outback gave him great appreciation for varieties of food sources. As he puts it in his own words, Everything that runs, wins, and everything that stays, pays!"
        },
        {
            "id": 2,
            "name": "Agumbe Tang",
            "image": "images/alberto.png",
            "designation": "Chief Taste Officer",
            "abbr": "CTO",
            "featured": False,
            "description": "Blessed with the most discerning gustatory sense, Agumbe, our CFO, personally ensures that every dish that we serve meets his exacting tastes. Our chefs dread the tongue lashing that ensues if their dish does not meet his exacting standards. He lives by his motto, You click only if you survive my lick."
        },
        {
            "id": 3,
            "name": "Alberto Somayya",
            "image": "images/alberto.png",
            "designation": "Executive Chef",
            "abbr": "EC",
            "featured": True,
            "description": "Award winning three-star Michelin chef with wide International experience having worked closely with whos-who in the culinary world, he specializes in creating mouthwatering Indo-Italian fusion experiences. He says, Put together the cuisines from the two craziest cultures, and you get a winning hit! Amma Mia!"
        }
    ]
}

import re

'''
return true if s arg is float otherwise return false
'''
def is_float(s):
    return re.match(r'^-?\d+(?:\.\d+)?$', str(s)) is not None

# setting table name
table_name = 'comments'

# setting table cols
table_cols = []
for col in data[table_name][0]: table_cols.append(col)
table_cols.remove('id') # remove id (already autoincrement)

# construct sql statement --> INSERT INTO dishes (name, id) VALUES ({}, {});
sql_statement = f'INSERT INTO {table_name} (' +\
    '{}, ' * (len(table_cols) - 1) + ' {}) VALUES ('
sql_statement = sql_statement.format(*table_cols)
sql_statement += '{}, ' * (len(table_cols) - 1) + ' {});'

# print full sql statement
for r in data[table_name]: 
    values = []
    for col in table_cols:
        val = r[col]
        val = val if is_float(val) else f"'{val}'"
        values.append(val)
    print(sql_statement.format(*values))
