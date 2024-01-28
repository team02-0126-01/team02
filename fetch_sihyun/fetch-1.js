fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            get_title(post.title);
        });
    });

const get_title = (title) => {
    console.log(title);
};

fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((comment) => {
            const { email, name, body } = comment;
            get_comment(email, name, body);
        });
    });

const get_comment = (email, name, body) => {
    console.log(`email: ${email}, name: ${name}, body: ${body}`);
};

fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            get_album_title(album.title);
        });
    });

const get_album_title = (title) => {
    console.log(title);
};

fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            get_url(photo.url);
        });
    });

const get_url = (url) => {
    console.log(url);
};

fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const { title, completed } = todo;
            get_todo(title, completed);
        });
    });

const get_todo = (title, completed) => {
    console.log(`title: ${title} completed: ${completed}`);
};

fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            get_name(user.name);
        });
    });

const get_name = (name) => {
    console.log(name);
};
