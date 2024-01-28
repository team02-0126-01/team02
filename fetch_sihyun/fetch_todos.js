fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { title, completed } = todo;
            get_todo(title, completed);
        });
    });

const getTodo = (title, completed) => {
    console.log(`title: ${title} completed: ${completed}`);
};