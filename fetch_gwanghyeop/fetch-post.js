fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        // id가 짝수인 것들의 제목만 출력
        posts.forEach((post) => {
            // id가 짝수일 때만 아래 함수 실행
            if (post.id % 2 == 0) {
                evenPost = refinedPosts(post.id, post.title);

                // 리턴된 문자열 출력
                console.log(evenPost);
            }
        });
    });

// id와 title을 입력받아 문장으로 리턴
const refinedPosts = (id, title) => {
    return `ID: ${id}   제목: ${title}`;
};
