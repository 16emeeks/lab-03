# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Elliott Meeks

## Lab Question Answers

### Question 1: Why are RESTful APIs scalable?
Rest APIs optimize client-server interactions. The server does not have to retain past client requests. 

### Question 2: According to the definition of “resources” provided in the AWS article above, what are the resources the mail server is providing to clients?

"Resources are the information that different applications provide to their clients." In our case the server is providing email information: subject, inbox, sent, etc.

### Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

Uniform Interface: Formates the information sent back in HTML. This could be used to create a more interactive mail server.

### Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

API keys can be used as am identifier for a particular client. It can be used to monitize a certain API or ensure the API is only accesed by authorized users. 

   - https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-key-source.html
...
