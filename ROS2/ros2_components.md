Parameter server is a shared, multi-variate dictionary that is accessible via network APIs. It is used to store parameters
that are accessible via the network. The parameter server is a key-value store, where the key is a string and the value is
a parameter value. 

For example, the parameter server can be used to store the maximum speed of a robot. The key is the name of the parameter
(e.g. max_speed) and the value is the value of the parameter (e.g. 0.5 m/s).


Services are a way for nodes to communicate with each other. A service is a named set of requests and responses. A node
can send a request to a service and receive a response. A service is defined by a service type. A service type is a
message type that defines the request and response. A service type is defined in a .srv file. A .srv file is similar to
a .msg file, but it defines a request and response instead of a message.