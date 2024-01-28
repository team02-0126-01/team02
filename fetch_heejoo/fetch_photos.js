fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            const { albumId } = photo;
            const { title } = photo;
            const { url } = photo;
            const { thumbnailUrl } = photo;
            console.log(albumId, title, url, thumbnailUrl);
        });
    });
