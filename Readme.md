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
python -m uvicorn FastApiTest:app --reload
- 
ASGI = Asynchronous Server Gateway Interface
-----------------------------------------

It is a standard interface between a Python web application (FastAPI) and a web server (Uvicorn).

Think of it as a communication protocol that allows the web server to communicate with your Python application.

Pydantic Model
--------------

FastAPI uses Pydantic models to receive and validate request bodies.

Pydantic is a Python library used for data validation, parsing, and serialization.

| Responsibility | Spring Boot | FastAPI |
|---|---|---|
| DTO | Java class | Pydantic model |
| JSON deserialization | Jackson | Pydantic integration |
| Data validation | Jakarta Validation | Pydantic |
| Type definitions | Java types | Python type hints |
| Serialization | Jackson | Pydantic integration |

Pip
---

It is Python's package manager. You use it to install, upgrade and uninstall external Python libraries (packages).

SQLAlchemy ORM
-------------

- FastAPI – REST API framework.
- SQLAlchemy – ORM (similar to Hibernate/JPA).
- PostgreSQL – Relational database.
- Psycopg – PostgreSQL database driver.
- Pydantic – Request and response validation.