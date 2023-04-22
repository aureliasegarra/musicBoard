[![Front](https://img.shields.io/badge/Framework-Fastapi-green?style=flat)](https://)
[![Front](https://img.shields.io/badge/Language-Python-blue?style=flat)](https://)

<br/>
<br/>
<div align="center">
    <img src="./resources/fastapi.png" alt="Logo" width="60%">
    <br/>
    <br/>
    <h1 align="center">Fastapi Application</h1>
</div>
  <p align="center">
    Application of musical tracks
    <br />
    <br />
  </p>


<br/>
<br/>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>

  <ol>
    <li><a href="#illustration">Illustration</a></li>
    <li><a href="#description">Description</a></li>
    <li><a href="#languages">Languages & tools</a></li>
    <li><a href="#objectives">Objectives</a></li>
    <li><a href="#setup">SetUp</a></li>
    <li><a href="#status">Status</a></li>
    <li><a href="#context">Context</a></li>
  </ol>
</details>

<br>
<br>



## Illustration <a id="illustration"></a>
![illustration](./resources/screenshot.png)


## Description <a id="description"></a>
Practical project to improve Fastapi skills
- Create a backend application with Fastapi
- Create a frontend application with jinja2 template
- Interact with a database (PostgreSQL)


## Languages/tools <a id="languages"></a>
- Python
- Fastapi
- Jinja2/HTML/CSS
- PostgreSQL/SQLAlchemy/Pydantic
- JWT/Passlib/Bcrypt

## Objectives <a id="objectives"></a>
<details close="close">
<summary>Create routes with Fastapi</summary>

![illustration](./resources/docs.png)
</details>

<details close="close">
<summary>Create & connect a PostgresSQL DB</summary>

![illustration](./resources/pgadmin.png)
</details>

<details close="close">
<summary>Create a frontend application with Jinja2</summary>

![illustration](./resources/template.png)
</details>

<details close="close">
<summary>Manage user authentication with JWT</summary>

![illustration](./resources/flowAuthentication.png)
</details>

<details close="close">
<summary>Manage user authorization with JWT</summary>

![illustration](./resources/flowAuthorization.png)
</details>


<details close="close">
<summary>Manage user password with Bcrypt</summary>

![illustration](./resources/bcrypt.png)
</details>


<details close="close">
<summary>Manage validation with Pydantic</summary>

![illustration](./resources/pydanticShemas.png)
</details>



## SetUp <a id="setup"></a>
- Clone the repository
- Create a virtual environment
- Install the requirements
- Create a database with PostgreSQL
- Create a .env file with the following variables:
```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/database_name
```
- Run the application
```
uvicorn main:app --reload
```


## Status <a id="status"></a>

Project in progress ... 


## Context <a id="context"> </a>
I realized this practical work during my bachelor of computer science in the Institute of technology of Vannes


