fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { userId } = todo;
            const { title } = todo;
            const { completed } = todo;
            console.log(userId, title, completed);
        });
    });
