FastAPI - Python Framework
--------------------------
FastAPI is a modern Python web framework for building APIs. It's built on Starlette (web layer) and Pydantic (data validation), and it's known for being fast, both in runtime performance and in development speed.

Uvicorn
-------

Http Server just like Apache Tomcat Server
       Client / Browser
              |
              | HTTP Request
              |
              v
       +-------------+
       |   Uvicorn   |
       |  Web Server |
       +-------------+
              |
              v
       +-------------+
       |   FastAPI   |
       | Application |
       +-------------+
              |
              v
       JSON Response

- FastAPI handles your API logic.
- Uvicorn receives HTTP requests and communicates with FastAPI.
- Uvicorn sends the HTTP response back to the client.
commands 
- pip install "uvicorn[standard]"