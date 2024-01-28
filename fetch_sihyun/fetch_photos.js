fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        photos.forEach((photo) => {
            get_url(photo.url);
        });
    });

const getUrl = (url) => {
    console.log(url);
};