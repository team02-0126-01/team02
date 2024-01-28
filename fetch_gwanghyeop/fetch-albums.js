fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => {
        // 가져온 데이터에서 title의 첫 마디만 출력
        // 데이터를 담을 빈 배열 선언
        resultArr = [];

        albums.forEach((album) => {
            // albums의 각 요소에서 'title' 키의 값을 변수에 할당
            const title = album.title;

            // 위에서 구한 title 변수에 아래에서 만든 함수 사용
            targetQuote = getFirstQuote(title);

            // 그헐게 구한 첫 마디를 resultArr에 추가
            resultArr.push(targetQuote);
        });

        // resultArr 출력
        console.log(resultArr);
    });

/*
    문자열을 입력받아 공백(" ")을 기준으로 나눠서 배열화하고,
    가장 처음에 있는 값을 반환하는 함수
*/
const getFirstQuote = (str) => {
    firstWord = str.split(" ")[0];
    return firstWord;
};
