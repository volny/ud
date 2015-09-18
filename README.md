## Overview
This app implements the basic functionality of a FOOD DELIVERY NETWORK like mjam.net.
There are restaurants, each has a menu. People can put items in their 'cart', prices are added up. Upon checkout there is just a splashscreen saying "You've ordered X,Y and Z for A$".

## 0.1 Specs (Restaurants, no menu items yet)
- opening /restaurants lists all restaurants
- ajax links to edit/delete each restaurant
- /restaurants/new has a form to add a new restaurant
- edit goes to /restaurant/<id>/edit to rename a restaurant
- delete reveals a confirmation dialog (like pinboard) before taking to DB

## Moar
- 0.2 menus. Restaurant detail pages display the menu. Users can change their menus. - 
- 0.3 users. there are 'restaurants', 'admins' and 'users'. restaurant owner can change their info, but not others.
- 0.4 cart. users can add menu items to a shopping cart, get order summary.
