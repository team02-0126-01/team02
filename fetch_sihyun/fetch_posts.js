fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            get_title(post.title);
        });
    });

const getTitle = (title) => {
    console.log(title);
};