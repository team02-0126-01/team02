fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) => {
        // 각 user별 company의 name, catchPhrase 구하기
        for (i of users) {
            // 가져온 데이터들을 변수에 담음
            username = i.username;
            companyName = i.company.name;
            catchPhrase = i.company.catchPhrase;

            // 아래의 함수 사용
            userInfo = userAndCompany(username, companyName, catchPhrase);

            // 유저 정보 출력
            console.log(userInfo);
        }
    });

// 인자로 전달받은 요소들로 문자열로 만들어 반환하는 함수
const userAndCompany = (user, company, phrase) => {
    return `이름: ${user}\n회사명: ${company}\n캐치프레이즈: ${phrase}\n`;
};
