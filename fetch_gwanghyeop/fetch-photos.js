// 아래 url에서 가져온 JSON 데이터를 JS 객체로 변환(Array)
fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => {
        /*
            thumbnailUrl 부분의 마지막에 있는 문자열에서, 숫자의 개수를 구하고
            모든 객체에 대해 같은 연산을 진행 한 뒤, 그 결과값들을 배열에 담아 출력
        */

        // 결과값을 저장할 빈 배열 생성
        resultArr = [];

        // for ... of 를 사용해서 가져온 데이터의 인덱스 하나하나(Object)를 순회
        for (i of photos) {
            // 아래에서 만든 함수를 사용하고, 리턴값 저장
            const finalNumbers = numbersInUrl(i);

            // 위의 리턴값을 배열에 추가
            resultArr.push(finalNumbers);
        }

        // 완성된 배열 출력
        console.log(resultArr);
    });

/* 
    각 객체의 thumbnailUrl 키의 값(https://via.placeholder.com/150/92c952 등)을
    '/' 를 기준으로 분리해서 Array로 만들고, 그 중 가장 마지막에 있는 문자열 추출

    그 후, 해당 문자열에서 숫자의 개수를 반환하는 함수
*/
const numbersInUrl = (url) => {
    // '/' 을 기준으로 분리해서 나온 마지막 문자열을 keyword에 할당
    keyword = url.thumbnailUrl.split("/").at(-1);

    // 위의 문자열을 한 글자씩 배열화, 그 중 숫자인 것들만 모아서 또 다른 배열 생성
    numArr = keyword.split("").filter((el) => !isNaN(el));

    // 배열의 길이(숫자 개수) 반환
    return numArr.length;
};
