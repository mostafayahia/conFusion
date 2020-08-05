-- DISHES
-- ########

DELETE FROM dishes;

INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Uthappizza', 'images/uthappizza.png', 'mains', 'Hot', 4.99, 'True',  'A unique combination of Indian Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer.');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Zucchipakoda', 'images/zucchipakoda.png', 'appetizer', '', 1.99, 'False',  'Deep fried Zucchini coated with mildly spiced Chickpea flour batter accompanied with a sweet-tangy tamarind sauce');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('Vadonut', 'images/vadonut.png', 'appetizer', 'New', 1.99, 'False',  'A quintessential ConFusion experience, is it a vada or is it a donut?');
INSERT INTO dishes (name, image, category, label, price, featured,  description) VALUES ('ElaiCheese Cake', 'images/elaicheesecake.png', 'dessert', '', 2.99, 'False',  'A delectable, semi-sweet New York Style Cheese Cake, with Graham cracker crust and spiced with Indian cardamoms');

-- PROMOTIONS
-- ############

DELETE FROM promotions;

INSERT INTO promotions (name, image, label, price, featured,  description) VALUES ('Weekend Grand Buffet', 'images/buffet.png', 'New', 19.99, 'True',  'Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person ');


