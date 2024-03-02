=======
Node.js
=======
Node.js is a cross-platform, open-source JavaScript runtime environment that can run on Windows, Linux, Unix, macOS, and more. 
Node.js runs on the V8 JavaScript engine, and executes JavaScript code outside a web browser.

Node.js uses an asynchronous event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time 
applications that run across distributed devices. Upon each connection, the callback is fired, but if there is no work to be done, Node.js will sleep.

`Official Website <https://nodejs.org/en/>`_


npm
===
npm is the default package manager for Node.js and is written entirely in JavaScript. It is used for managing and sharing 
packages of code with other developers.

npm is the world's largest Software Registry.

Installation and Usage
======================

To install Node.js and npm, run the following command:

.. code-block:: bash

   sudo apt-get install nodejs npm


To install a package, run the following command:

.. code-block:: bash

   npm install <package_name>


Create Hello World Application
==============================

Simple console application that prints "Hello, World!" to the console.
-----------------------------------------------------------------------

1. ``mkdir hello-world`` - Create a new directory

2. ``cd hello-world`` - Change to the new directory

3. ``npm init -y`` - Create a new package.json file (-y flag will skip the questionnaire)

4. ``nano index.js`` - Create and open a new file

5. Add the following code to the file 

.. code-block:: javascript

    console.log('Hello, World!');

6. ``node index.js`` - Run the file


Web application that prints "Hello, World!" to the browser.
-----------------------------------------------------------

1. ``nano server.js`` - Create a new file
2. Add the following code to the file

.. code-block:: javascript

    const http = require('http');
    const hostname = '

    const server = http.createServer((req, res) => {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Hello, World!\n');
    });

    server.listen(port, hostname, () => {
      console.log(`Server running at http://${hostname}:${port}/`);
    });

3. ``node server.js`` - Run the file

Open a web browser and navigate to http://localhost:3000. You should see the message "Hello, World!".