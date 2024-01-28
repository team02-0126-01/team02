fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            const { userId } = album;
            const { title } = album;
            console.log(userId, title);
        });
    });
