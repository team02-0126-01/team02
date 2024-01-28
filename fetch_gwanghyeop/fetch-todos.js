fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => {
        // completed 가 false 인 요소의 title만 출력
        for (i of todos) {
            // 우선 completed 가 false인지 검사
            if (!i.completed) {
                // false라면 아래에서 만든 함수 실행
                uncompletedTodo = refinedTodos(i.id, i.title);

                // 반환된 문자열 출력
                console.log(uncompletedTodo);
            }
        }
    });

// id와 title을 입력받아 알기 쉽게끔 문장으로 반환해주는 함수
const refinedTodos = (id, title) => {
    return `ID: ${id}   제목: ${title}`;
};
