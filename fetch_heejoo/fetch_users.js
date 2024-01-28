fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => {
            const { name } = user;
            const { username } = user;
            const { email } = user;
            const { street } = user.address;
            const { suite } = user.address;
            const { city } = user.address;
            const { zipcode } = user.address;
            const { lat } = user.address.geo;
            const { lng } = user.address.geo;
            const { phone } = user;
            const { website } = user;
            console.log(
                name,
                username,
                email,
                street,
                suite,
                city,
                zipcode,
                lat,
                lng,
                phone,
                website
            );
        });
    });
