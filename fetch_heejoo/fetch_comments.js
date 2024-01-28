fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((comment) => {
            const { postId } = comment;
            const { name } = comment;
            const { email } = comment;
            const { body } = comment;
            console.log(postId, name, email, body);
        });
    });
