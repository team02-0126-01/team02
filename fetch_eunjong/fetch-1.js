fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const { name } = user;
            console.log(name);
        });
    });

fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const { phone, company } = user;
            console.log(`Phone: ${phone}, Company: ${company.name}`);
        });
    });

fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { title, body } = post;
            console.log(`Title: ${title}\nBody: ${body}\n`);
        });
    });

fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { title, completed } = todo;
            console.log(`Title: ${title}, Completed: ${completed}`);
        });
    });

fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            const { title, userId } = album;
            console.log(`Title: ${title}, User ID: ${userId}`);
        });
    });
