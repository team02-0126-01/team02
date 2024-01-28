fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        comments.forEach((comment) => {
            const { email, name, body } = comment;
            get_comment(email, name, body);
        });
    });

const getComment = (email, name, body) => {
    console.log(`email: ${email}, name: ${name}, body: ${body}`);
};