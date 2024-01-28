fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        posts.forEach((post) => {
            const { userId } = post;
            const { title } = post;
            const { body } = post;
            console.log(userId, title, body);
        });
    });
