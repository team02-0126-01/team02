fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        albums.forEach((album) => {
            get_album_title(album.title);
        });
    });

const getAlbumTitle = (title) => {
    console.log(title);
};