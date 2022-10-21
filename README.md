# flaska-pro-pokrocile

~~Just read the code bro?~~

### Dates and stuff:
* GET datetime links: ```/restapi/v1/datetime```
  * All the documentation you'll need is there

### Messages:
* GET all messages: ```/restapi/v1/messages```
* GET, DELETE or PUT (edit) a message by id: ```/restapi/v1/messages/<id>```
    * When editing attach the new message text as {"message":\<message\>}
* POST a message: ```/restapi/v1/messages/send```
    * POST the message text as {"msg":\<message\>}

# 🤓