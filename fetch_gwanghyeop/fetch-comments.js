fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then((comments) => {
        // 가져온 데이터의 email을 각 줄에 차례대로 출력
        for (i of comments) {
            // 아래 함수의 리턴값을 변수의 저장
            const reply = userAndComment(i.email, i.body);

            // 내용 출력
            console.log(reply);
        }
    });

// email과 body(댓글)를 전달받아 문장을 만들어주는 함수
const userAndComment = (email, comment) => {
    return `작성자: ${email}\n내용: ${comment}\n`;
};
