// 아래 url에서 가져온 JSON 데이터를 JS 객체로 변환(Array)
fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((posts) => {
        resultArr = [];
        // for ... of 를 사용해서 가져온 데이터의 인덱스 하나하나(Object)를 순회
        for (i of posts) {
            /* 
                각 객체의 thumbnailUrl 키의 값(https://via.placeholder.com/150/92c952 등)을
                '/' 를 기준으로 분리해서 Array로 만들고,
                그 중 가장 마지막에 있는 문자열 추출
            */
            keyword = i.thumbnailUrl.split("/").at(-1);

            /*
                위에서 추출한 문자열을 split을 사용해서 다시 배열로 만들고,
                filter 함수로 숫자인 요소들만 남겨서 numCount에 할당(현재 Array 타입) 
            */
            numCount = keyword.split("").filter((el) => !isNaN(el));

            // 그렇게 만들어진 배열의 길이를 resultArr에 추가
            resultArr.push(numCount.length);
        }

        console.log(resultArr);
    });
