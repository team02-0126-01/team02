fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            get_name(user.name);
        });
    });

const getName = (name) => {
    console.log(name);
};