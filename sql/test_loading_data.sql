-- DROP TABLES IF EXISTS TO CREATE NEW ONES
-- #############################################
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS dishes;
DROP TABLE IF EXISTS promotions;

-- Dishes
-- #################
CREATE TABLE dishes (
  id serial primary key,
  name varchar not null,
  image varchar not null,
  category varchar not null,
  label varchar,
  price float not null,
  featured boolean default false,
  description varchar
);
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Uthappizza', 'images/uthappizza.png', 'mains', 'Hot', 4.99, 'True',  'A unique combination of Indian Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer.');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Zucchipakoda', 'images/zucchipakoda.png', 'appetizer', '', 1.99, 'False',  'Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Vadonut', 'images/vadonut.png', 'appetizer', 'New', 1.99, 'False',  'A quintessential ConFusion experience, is it a vada or is it a donut?');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('ElaiCheese Cake', 'images/elaicheesecake.png', 'dessert', '', 2.99, 'False',  'A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms');

-- Promotions
-- #################
CREATE TABLE promotions (
  id serial primary key,
  name varchar not null,
  image varchar not null,
  label varchar,
  price float not null,
  featured boolean default false,
  description varchar not null
);
INSERT INTO promotions (name, image, label, price, featured,  description) VALUES ('Weekend Grand Buffet', 'images/buffet.png', 'New', 19.99, 'True',  'Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person ');

-- Comments
-- ################
CREATE TABLE comments (
  id serial primary key,
  dishId integer,
  rating float not null,
  comment varchar not null,
  author varchar not null,
  date timestamptz not null,
  FOREIGN KEY (dishId) REFERENCES dishes(id) ON DELETE SET NULL
);
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (1, 5, 'Imagine all the eatables, living in conFusion!', 'John Lemon',  '2012-10-16T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (1, 4, 'Sends anyone to heaven, I wish I could get my mother-in-law to eat it!', 'Paul McVites',  '2014-09-05T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (1, 3, 'Eat it, just eat it!', 'Michael Jaikishan',  '2015-02-13T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (1, 4, 'Ultimate, Reaching for the stars!', 'Ringo Starry',  '2013-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (1, 2, 'It is your birthday, we are gonna party!', '25 Cent',  '2011-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (2, 5, 'Imagine all the eatables, living in conFusion!', 'John Lemon',  '2012-10-16T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (2, 4, 'Sends anyone to heaven, I wish I could get my mother-in-law to eat it!', 'Paul McVites',  '2014-09-05T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (2, 3, 'Eat it, just eat it!', 'Michael Jaikishan',  '2015-02-13T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (2, 4, 'Ultimate, Reaching for the stars!', 'Ringo Starry',  '2013-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (2, 2, 'It is your birthday, we are gonna party!', '25 Cent',  '2011-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (3, 5, 'Imagine all the eatables, living in conFusion!', 'John Lemon',  '2012-10-16T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (3, 4, 'Sends anyone to heaven, I wish I could get my mother-in-law to eat it!', 'Paul McVites',  '2014-09-05T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (3, 3, 'Eat it, just eat it!', 'Michael Jaikishan',  '2015-02-13T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (3, 4, 'Ultimate, Reaching for the stars!', 'Ringo Starry',  '2013-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (3, 2, 'It is your birthday, we are gonna party!', '25 Cent',  '2011-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (4, 5, 'Imagine all the eatables, living in conFusion!', 'John Lemon',  '2012-10-16T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (4, 4, 'Sends anyone to heaven, I wish I could get my mother-in-law to eat it!', 'Paul McVites',  '2014-09-05T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (4, 3, 'Eat it, just eat it!', 'Michael Jaikishan',  '2015-02-13T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (4, 4, 'Ultimate, Reaching for the stars!', 'Ringo Starry',  '2013-12-02T17:57:28.556094');
INSERT INTO comments (dishId, rating, comment, author,  date) VALUES (4, 2, 'It is your birthday, we are gonna party!', '25 Cent',  '2011-12-02T17:57:28.556094');